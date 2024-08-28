% for tttt = 1:1:4
instrreset;
clc ; clear ; close all;

%%test
file1 = 'DisPow_cor.dat';
file2 = 'DisPow_cor_init.dat';
% down_dis_power_table(rts,file1);
% down_dis_power_table(rts,file2);
%% 参数设置
delay_rts = 0.737; % 0206
% delay_rts = 0.673;
dis = (0:0.128:500)+ delay_rts;
dis1 = dis ;
center=(dis1)*2./2.997924580000000e+08;    %% 2*s/C换算时间
span_time = 1e-9;
start_time = center-span_time;                       %% 矢网起始时间 单位：Hz
end_time = center+span_time;
%% rts
rts_ip = '192.168.1.10';
% rts_ip = '192.168.1.11';
rts_port = 7;

rts = client_sever(rts_ip,rts_port);
rts_reset(rts);
down_sys_para(rts,delay_rts);
down_sim_para(rts,delay_rts,0);
start_simulation(rts,1);
down_dis_power_table(rts,file2);
start_freq = 4.54e9;
end_freq   = 9.54e9;
power = -30 ;                               %矢网输出功率
point = 20001;
%%
GPIB = 'GPIB0::16::INSTR';
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
fprintf(N5230C,'CALC:TRAN:TIME:STAR %s ',num2str(start_time(1)));
fprintf(N5230C,'CALC:TRAN:TIME:STOP %s ',num2str(end_time(1)));
fprintf(N5230C,'DISP:WIND:Y:AUTO');
fprintf(N5230C,'CALC:MARK ON');
fprintf(N5230C,'DISP:WIND:ANN:MARK:RES:STIM 9');
fprintf(N5230C,'DISP:WIND:ANN:MARK:RES:RESP 4');
fprintf(N5230C,'CALC:MARK1:FUNC:EXEC MAX');
fprintf(N5230C,'CALC:MARK:FUNC:TRAC ON');					%开关跟踪
fprintf(N5230C,'CALC:TRAN:TIME:MARK:MODE REFL');
%%
distance = zeros(1,length(dis));
power = zeros(1,length(dis));
delay = zeros(1,length(dis));
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
    plot(x,error*1e3);
    xlabel('Dis (m)','FontSize',15);ylabel('Distance Error (mm)','FontSize',15);
    title(sprintf('Dis Error :%.3f mm',range(error*1e3)),'FontSize',15);
    subplot(122)
    plot(x,y1);
    xlabel('Dis (m)','FontSize',15);ylabel('Coll Power (dB)','FontSize',15);
    title(sprintf('Power Jitter Range : %.3f dB',range(y1)),'FontSize',15);
end

%% test
dis_cont = (0:0.128:500) + delay_rts;
power1 = zeros(1,length(dis_cont));
cnt = 1;
for i = 1:length(dis_cont)
    if(dis(cnt) - dis_cont(i) < 1e-6)
        power1(i) = power(cnt);
%         i
        if (dis(cnt) == dis(end))
            cnt = cnt;
        else
            cnt = cnt + 1;
        end
    else
        power1(i) = 0;
    end
end
power = power1;
%% save
clock1 = clock;
savefile1 = strcat('data\colldata\',sprintf('%04d%02d%02d_%02d%02d%02.0f_Dis_Power_Corr',clock1(1),clock1(2), ...
    clock1(3),clock1(4),clock1(5),clock1(6)))
savefile = strcat('data\',sprintf('Dis_Power_Corr_1'));
save(savefile1,'rts_ip','distance','error','dis','power',"delay");
save(savefile ,'rts_ip','distance','error','dis','power',"delay");
% run mian_dis_corr_table.m
% end