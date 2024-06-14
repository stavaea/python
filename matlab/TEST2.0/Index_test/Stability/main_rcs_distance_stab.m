% 该程序主要应用于RTS的距离、RCS稳定性指标测试
% 程序使用矢网N5230C。
instrreset;
clc ; clear ; close all;
%% RTS 模拟器型号参数
% RTS 序列号
RTS_number   = 'SN2402006';
% RTS 最小频率(射频) 单位:GHZ
RTS_min_freq = '76';
% RTS 最大频率(射频) 单位:GHZ
RTS_max_freq = '81';
% RTS 类型
% D：数字型 FC：光纤步进型 FS：光纤分段型
RTS_mode     = 'D';
% RTS 工作带宽
% 04：0.4GHz 10:1GHz 20:2GHz 40:4GHz 50：5GHz
RTS_inst_band= '50';
%% 参数配置
% RTS IP 地址
RTS_ip   = '192.168.1.10';
% RTS IP 端口号
RTS_port = 7;
% 矢网GPIB
GPIB_N5230C          = 'GPIB2::16::INSTR' ;
% 雷达与模拟器距离
% Rrts                 = 1.019;
% % 系统延时
% rts_delay            = 76.66;
% 模拟目标距离
tar_dis              = 50;
% 矢网起始频率
start_freq  = 7.6e9;
% 矢网结束频率
stop_freq   = 9.6e9;
%矢网输出功率
amp_set              = -40  ;
% 矢网信号点数
point = 20001;
% 矢网时间span 单位：s
span_time = 1e-9;
%% 保存文件名称
File_path            = '..\Data\';
File                 = strcat(File_path,'RTS',RTS_min_freq,RTS_max_freq,RTS_mode,'_',RTS_inst_band);
File_data            = strcat(File,'\',RTS_number);
Creat_File(File); % 创建保存数据的文件夹
Creat_File(File_data);
%% 距离延时计算
center=(tar_dis)*2./2.997924580000000e+08;    %% 2*s/C换算时间
start_time = center-span_time;                       %% 矢网起始时间 单位：Hz
stop_time = center+span_time;
%% 连接矢网、RTS
rts            = client_sever(RTS_ip,RTS_port);
N5230C = visa('agilent',GPIB_N5230C);  % 创建仪器连接对象
set(N5230C,'InputBufferSize',60e4);
fopen(N5230C);                                % 连接仪器
clrdevice(N5230C);                            % 清空
get(N5230C,'Status');                         % 获取仪器状态
fprintf(N5230C, '*IDN?');                     % 询问IDN
idn = fscanf(N5230C);                         % 读取IDN
%% 矢网配置
fprintf(N5230C,'SOUR:POW1 %sdBm',num2str(amp_set));
fprintf(N5230C,'CALCulate:PARameter:DEFine "TEST", S21');  % 定义S21为测试参数
fprintf(N5230C,'DISPlay:WINDow1:TRACe1:FEED "TEST"');
fprintf(N5230C,'DISPlay:WINDow1:TRACe1:STATe ON');
fprintf(N5230C,sprintf('SENSe:FREQuency:STARt %s Hz',num2str(start_freq))); % 设置频率范围高端
fprintf(N5230C,sprintf('SENSe:FREQuency:STOP %s Hz',num2str(stop_freq)));  % 设置频率范围低端
fprintf(N5230C,sprintf('SENSe:SWEep:POINts %s',num2str(point)));  % 设置频率分析点数
fprintf(N5230C,'CALC:TRAN:TIME:STATe ON');
fprintf(N5230C,'CALC:TRAN:TIME:STAR %s ',num2str(start_time(1)));%any number between:(number of points-1) / frequency span
fprintf(N5230C,'CALC:TRAN:TIME:STOP %s ',num2str(stop_time(1))); %Choose any number between:.45 / frequency span and 1.48 / frequency span
fprintf(N5230C,'DISP:WIND:Y:AUTO');
fprintf(N5230C,'CALC:MARK ON');
fprintf(N5230C,'DISP:WIND:ANN:MARK:RES:STIM 9');
fprintf(N5230C,'DISP:WIND:ANN:MARK:RES:RESP 4');
fprintf(N5230C,'CALC:MARK1:FUNC:EXEC MAX');
fprintf(N5230C,'CALC:MARK:FUNC:TRAC ON');					%开关跟踪
fprintf(N5230C,'CALC:TRAN:TIME:MARK:MODE REFL');
%% 采集数据
test = 24*60 + 60 + 1;
distance = zeros(1,test);
power    = zeros(1,test);
delay    = zeros(1,test);
time     = zeros(1,test);
freq_temp = zeros(1,test);
up_temp   = zeros(1,test);
down_temp = zeros(1,test);
tic;
for i = 1:test
    if i <= 61
        pause(1)
    else
        pause(60)
    end
    fprintf(N5230C,'CALC:MARK:Dist?');  distance(i) = str2num(fscanf(N5230C));
    fprintf(N5230C,'CALC:MARK1:X?');    delay(i) = str2num(fscanf(N5230C));
    fprintf(N5230C,'CALC:MARK1:Y?');    t= str2num(fscanf(N5230C));power(i) = t(1);

    time(i) = toc;

    x = time(1:i)/60;
    y = distance(1:i);
    y1 = power(1:i);

    return_data     = sim_para(rts);
    freq_temp(i)    = return_data(1);
    up_temp(i)      = return_data(2);
    down_temp(i)    = return_data(3);
    freq_temp       = freq_temp(1:i);
    up_temp         = up_temp(1:i);
    down_temp       = down_temp(1:i);

    subplot(121)
    plot(x,y);
    grid minor;
    xlabel('Time (min)','FontSize',15);ylabel('Distance Error (mm)','FontSize',15);
    title(sprintf('Dis Jitter Range :%.3f mm',range(y)*1e3),'FontSize',15);

    subplot(122);
    hold on;
    plot(x,y1,'k-o', 'LineWidth', 1);hold on;
    plot(x,freq_temp,'r-', 'LineWidth', 2);hold on;
    plot(x,up_temp, 'g--', 'LineWidth', 1.5);hold on;
    plot(x,down_temp, 'b:', 'LineWidth', 1);

    grid minor;
    xlabel('Time (min)','FontSize',15);ylabel('Coll Power (dB) & Coll Temp','FontSize',15);
    title(sprintf('Power Jitter Range : %.3f dB',range(y1)),'FontSize',15);

    legend('power','syn_temp','up_temp','down_temp')
end

%% 保存文件
clock1 = clock;
savefile1 = strcat(File_data,'\',sprintf('%04d%02d%02d_%02d%02d%02.0f_距离RCS稳定性测试',clock1(1),clock1(2), ...
    clock1(3),clock1(4),clock1(5),clock1(6)))
save(savefile1,'distance','power','tar_dis','amp_set',"delay","RTS_number",'time','i',"test",'freq_temp','up_temp','down_temp');
instrreset;
