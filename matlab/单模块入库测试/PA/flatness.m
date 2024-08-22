% 该程序主要应用于RTS的平坦度指标测试
instrreset;
clc ; clear ; close all;
%% RTS 模拟器型号参数
% RTS 序列号
PA_number   = 'SN_bk24023';
% 矢网GPIB
GPIB          = 'GPIB2::16::INSTR'                  ;
% 矢网起始频率
start_freq  = 0.2e9;
% 矢网结束频率
stop_freq   = 2.3e9;
%矢网输出功率
amp_set              = -40  ;
% 矢网信号点数
point = 20001;
%% 连接矢网、RTS
N5230C = visa('agilent',GPIB);  % 创建仪器连接对象
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
fprintf(N5230C,'DISP:WIND:Y:AUTO');
fprintf(N5230C,'CALC:MARK ON');
fprintf(N5230C,'DISP:WIND:ANN:MARK:RES:STIM 9');
fprintf(N5230C,'DISP:WIND:ANN:MARK:RES:RESP 4');
fprintf(N5230C,'CALC:MARK1:FUNC:EXEC MAX');
fprintf(N5230C,'CALC:MARK:FUNC:TRAC ON');					%开关跟踪
fprintf(N5230C,'CALC:TRAN:TIME:MARK:MODE REFL');
fprintf(N5230C, 'FORM REAL,64');
fprintf(N5230C, 'FORM:BORD SWAP');

%%
fprintf(N5230C,'DISP:WIND:Y:AUTO');
fprintf(N5230C,':CALCulate:DATA? FDATA ');
trace = binblockread(N5230C,'double');
trace(1,:) = trace';

%% 保存文件
clock1 = clock;
savefile = strcat('data','\',sprintf('%s_幅频修正数据',File_data))
save(savefile,'trace','amp_set','freq_lo','RTS_number','start_freq','stop_freq','power','trace_corr_temp');

savefile1 = strcat('data\back_up\',sprintf('%04d%02d%02d_%02d%02d%02.0f_%s_幅频修正数据',clock1(1),clock1(2), ...
    clock1(3),clock1(4),clock1(5),clock1(6),File_data))
save(savefile1,'trace_before','amp_set','freq_lo','RTS_number','start_freq','stop_freq','power','trace_corr');
instrreset;
