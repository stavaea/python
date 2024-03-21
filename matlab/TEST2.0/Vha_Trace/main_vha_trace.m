% 该程序主要应用于RTS的平坦度指标测试
% 使用矢网N5230C。
instrreset;
clc ; clear ; close all;
%% 参数配置
% 保存文件名称
data_name = 'RTS7681D_Am_Freq_coll';
% 目标距离
tar_dis = 10;
% 矢网GPIB
GPIB_N5230C          = 'GPIB3::16::INSTR' ;
% 矢网模式选择 0 ： 时域 1：频域
mode = 1;
% 矢网开始频率
start_freq  = 7.6e9;
% 矢网结束频率
stop_freq   = 9.6e9;
%矢网输出功率
amp_set              = -40  ;
% 矢网信号点数
point = 20001;
% 矢网时间span 单位：ns
span_time = 4e-9;

%% 距离延时计算
center=(tar_dis)*2./2.997924580000000e+08;    %% 2*s/C换算时间
start_time = center-span_time;                       %% 矢网起始时间 单位：Hz
stop_time = center+span_time;
%% 连接矢网、RTS
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
if mode == 1
fprintf(N5230C,'CALC:TRAN:TIME:STATe OFF');
else
fprintf(N5230C,'CALC:TRAN:TIME:STATe ON');
end
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

fprintf(N5230C,':CALCulate:DATA? FDATA ');
trace = binblockread(N5230C,'double');

%% 保存文件
clock1 = clock;
savefile1 = strcat('Data\',sprintf('%04d%02d%02d_%02d%02d%02.0f_%s',clock1(1),clock1(2), ...
    clock1(3),clock1(4),clock1(5),clock1(6),data_name))
save(savefile1,'trace','amp_set',"start_freq","stop_freq","point","mode","tar_dis");
instrreset;











