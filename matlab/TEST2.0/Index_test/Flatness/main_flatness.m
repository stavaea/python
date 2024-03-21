% 该程序主要应用于RTS的平坦度指标测试
% 使用矢网N5230C。
instrreset;
clc ; clear ; close all;
%% RTS 模拟器型号参数
% RTS 序列号
RTS_number   = 'SN2402001';
% RTS 最小频率(射频) 单位:GHZ
RTS_min_freq = '76';
% RTS 最大频率(射频) 单位:GHZ
RTS_max_freq = '81';
% RTS 类型
% D：数字型 FC：光纤步进型 FS：光纤分段型
RTS_mode     = 'D';
% RTS 瞬时带宽
% 04：0.4GHz 10:1GHz 20:2GHz 40:4GHz 50：5GHz
RTS_inst_band= '20';
%% 参数配置
% RTS IP 地址
RTS_ip   = '192.168.1.10';
% RTS IP 端口号
RTS_port = 7;
% 系统本振 K: 9213 E:11910
freq_lo              = [77000 79000 80000];
% 中心频率
freq_center          = [77000 79000 80000];
% 工作频段选择 0：24G 1：77G 2：60G;
waveband             = 1;
% 矢网GPIB
GPIB_N5230C          = 'GPIB2::16::INSTR'                  ;
% 雷达与模拟器距离
Rrts                 = 0;
% 系统延时
rts_delay            = 87.94;
% 模拟目标距离
tar_dis              =10;
% 矢网起始频率
start_freq  = 7.6e9;
% 矢网结束频率
stop_freq   = 9.6e9;
%矢网输出功率
amp_set              = -40  ;
% 矢网信号点数
point = 20001;
% 矢网时间span 单位：ns
span_time = 4e-9;
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
% fprintf(N5230C,'CALC:TRAN:TIME:STATe ON');
fprintf(N5230C,'CALC:TRAN:TIME:STATe OFF');
fprintf(N5230C,'CALC:TRAN:TIME:STAR %s ',num2str(start_time(1)));%any number between:(number of points-1) / frequency span
fprintf(N5230C,'CALC:TRAN:TIME:STOP %s ',num2str(stop_time(1))); %Choose any number between:.45 / frequency span and 1.48 / frequency span
fprintf(N5230C,'DISP:WIND:Y:AUTO');
fprintf(N5230C,'CALC:MARK ON');
fprintf(N5230C,'DISP:WIND:ANN:MARK:RES:STIM 9');
fprintf(N5230C,'DISP:WIND:ANN:MARK:RES:RESP 4');
fprintf(N5230C,'CALC:MARK1:FUNC:EXEC MAX');
fprintf(N5230C,'CALC:MARK:FUNC:TRAC ON');					%开关跟踪
fprintf(N5230C,'CALC:TRAN:TIME:MARK:MODE REFL');
fprintf(N5230C, 'FORM REAL,64');
fprintf(N5230C, 'FORM:BORD SWAP');
%% 采集数据
len_lo = length(freq_lo);
trace   = zeros(len_lo,point);
for i = 1:len_lo
    down_sys_para(rts,freq_lo(i),freq_center(i),waveband,Rrts,rts_delay);
    if strcmp(RTS_mode,'D')
        down_file  = sprintf('am_freq\\%d',freq_lo(i)/1e3);
        load_am_freq_table(rts,down_file);
    end
    pause(4);
    fprintf(N5230C,'DISP:WIND:Y:AUTO');
    fprintf(N5230C,':CALCulate:DATA? FDATA ');
    temp = binblockread(N5230C,'double');
    trace(i,:) = temp;
end

%% 保存文件
clock1 = clock;
savefile1 = strcat(File_data,'\',sprintf('%04d%02d%02d_%02d%02d%02.0f_平坦度指标测试',clock1(1),clock1(2), ...
    clock1(3),clock1(4),clock1(5),clock1(6)))
save(savefile1,'trace','amp_set',"freq_lo","RTS_number","start_freq","stop_freq","point","Rrts","rts_delay","tar_dis");
instrreset;











