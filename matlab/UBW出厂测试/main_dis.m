instrreset;
clc ; clear ; close all;

%% 参数设置
dis = 0:0.05:60;
dis1 = dis + 1.4123;
center=(dis1)*2./2.997924580000000e+08;    %% 2*s/C换算时间
span_time = 20e-9;
start_time = center-span_time;                       %% 矢网起始时间 单位：Hz
end_time = center+span_time;
%% rts
rts_ip = '192.168.1.10';
rts_port = 7;

rts = client_sever(rts_ip,rts_port);
start_freq = 0.4e9;
end_freq   = 5.4e9;
power = -40 ;                               %矢网输出功率
point = 20001;
%%
GPIB = 'GPIB1::16::INSTR';
N5230C = visa('agilent',GPIB);  % 创建仪器连接对象
fopen(N5230C);                                % 连接仪器
clrdevice(N5230C);                            % 清空
get(N5230C,'Status');                         % 获取仪器状态
fprintf(N5230C, '*IDN?');                     % 询问IDN
idn = fscanf(N5230C);                         % 读取IDN

fprintf(N5230C,'SOUR:POW1 %sdBm',num2str(power));
fprintf(N5230C,'CALCulate:PARameter:DEFine "TEST", S21');  % 定义S21为测试参数
fprintf(N5230C,'DISPlay:WINDow1:TRACe1:FEED "TEST"');
fprintf(N5230C,'DISPlay:WINDow1:TRACe1:STATe ON');
% fprintf(N5230C,'DISPlay:WINDow1:TRACe1:STATe OFF');
fprintf(N5230C,sprintf('SENSe:FREQuency:STARt %s Hz',num2str(start_freq))); % 设置频率范围高端
fprintf(N5230C,sprintf('SENSe:FREQuency:STOP %s Hz',num2str(end_freq)));  % 设置频率范围低端
fprintf(N5230C,sprintf('SENSe:SWEep:POINts %s',num2str(point)));  % 设置频率分析点数
fprintf(N5230C,'CALC:TRAN:TIME:STATe ON');
fprintf(N5230C,'CALC:TRAN:TIME:STAR %s ',num2str(start_time(1)));%any number between:(number of points-1) / frequency span
% pause(1)
fprintf(N5230C,'CALC:TRAN:TIME:STOP %s ',num2str(end_time(1))); %Choose any number between:.45 / frequency span and 1.48 / frequency span
fprintf(N5230C,'DISP:WIND:Y:AUTO');
fprintf(N5230C,'CALC:MARK ON');
fprintf(N5230C,'DISP:WIND:ANN:MARK:RES:STIM 9');
fprintf(N5230C,'DISP:WIND:ANN:MARK:RES:RESP 4');
fprintf(N5230C,'CALC:MARK1:FUNC:EXEC MAX');
fprintf(N5230C,'CALC:MARK:FUNC:TRAC ON');					%开关跟踪
fprintf(N5230C,'CALC:TRAN:TIME:MARK:MODE REFL');
%%
distance = zeros(length(dis));
power = zeros(length(dis));
delay = zeros(length(dis));
for i = 1: length(dis)
    down_sim_para(rts,dis(i),0);
    fprintf(N5230C,'CALC:TRAN:TIME:STAR %s ',num2str(start_time(i)));
    fprintf(N5230C,'CALC:TRAN:TIME:STOP %s ',num2str(end_time(i)));
    pause(1)
    fprintf(N5230C,'DISP:WIND:Y:AUTO');
    fprintf(N5230C,'CALC:MARK:Dist?');  distance(i) = str2num(fscanf(N5230C));
    fprintf(N5230C,'CALC:MARK1:X?');    delay(i) = str2num(fscanf(N5230C));
    fprintf(N5230C,'CALC:MARK1:Y?');    t= str2num(fscanf(N5230C));power(i) = t(1);
    x = dis(1:i);
    y = distance(1:i);
    y1 = power(1:i);
    subplot(121)
    error = dis1(1:i) - y;
    plot(x,error*1e3,'LineWidth',5);
    xlabel('Dis (m)','FontSize',15);ylabel('Distance Error (mm)','FontSize',15);
    title(sprintf('Dis Error :%.3f mm',range(error*1e3)),'FontSize',15);
    subplot(122)
    plot(x,y1,'LineWidth',5);
    xlabel('Dis (m)','FontSize',15);ylabel('Coll Power (dB)','FontSize',15);
    title(sprintf('Power Jitter Range : %.3f dB',range(y1)),'FontSize',15);
end

%% save
clock1 = clock;
savefile1 = strcat('data\',sprintf('%04d%02d%02d_%02d%02d%02.0f_ubw距离指标测试',clock1(1),clock1(2), ...
    clock1(3),clock1(4),clock1(5),clock1(6)))
save(savefile1,'distance','y1','error','dis','power',"delay",'x');