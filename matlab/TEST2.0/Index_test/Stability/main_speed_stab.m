% 该程序主要应用于RTS的速度稳定性指标测试
% 程序使用信号源83630B、频谱仪N9020A。
instrreset;
clc ; clear ; close all;
%% RTS 模拟器型号参数
% RTS 序列号
RTS_number   = 'SN2402001';
% RTS 最小频率(射频) 单位:GHZ
RTS_min_freq = '23';
% RTS 最大频率(射频) 单位:GHZ
RTS_max_freq = '25';
% RTS 类型
% D：数字型 FC：光纤步进型 FS：光纤分段型
RTS_mode     = 'FC';
% RTS 瞬时带宽
% 04：0.4GHz 10:1GHz 20:2GHz 40:4GHz 50：5GHz
RTS_inst_band= '50';
%% 参数配置
% 测试频率
fre_set              = 24000 ;
% 信号源输出功率
amp_set              = -40  ;
% 系统本振 K: 9213 E:11910
freq_lo              = 9213;
% 中心频率 与测试频率相对应的射频频率
freq_center          = 24000 ;
% 工作频段选择 0：24G 1：77G 2：60G
waveband             = 0;
% 速度测试点
speed                = 100/3.6;
% 信号源GPIB
GPIB_83630B          = 'GPIB1::1::INSTR'                  ;
% 频谱仪IP
ip_spec              = ['TCPIP0::','192.168.1.5','::INSTR'];
% 频谱仪span
span                 = 100;
% 频谱仪rbw
rbw                  = 10;
% 模拟目标距离
tar_dis              = 0;
% RTS接收衰减
rece                 = 30;
% 频谱仪点数
point                = 1001;
% 频谱仪功率参考
y_ref                = 20;
%% 保存文件名称
File_path            = '..\Data\';
File                 = strcat(File_path,'RTS',RTS_min_freq,RTS_max_freq,RTS_mode,'_',RTS_inst_band);
File_data            = strcat(File,'\',RTS_number);
Creat_File(File); % 创建保存数据的文件夹
Creat_File(File_data);
%% Doppler 计算
len_fre   = length(fre_set);
len_speed = length(speed);
fd =-1 * 2.*speed.*freq_center'.*1e6./299792458;
fd = fd * 10;
fd = fd / 1e7;
spec_fre_set = repmat(fre_set',1,len_speed) + fd;
%% 连接信号源、频谱仪、RTS
keysight83630B = visa('agilent', GPIB_83630B);
fopen(keysight83630B);
N9020A         = visa('agilent',ip_spec);
set(N9020A,'InputBufferSize',60e4);
fopen(N9020A);
%% 信号源配置
fprintf(keysight83630B,'FREQuency %f MHz',fre_set(1));
fprintf(keysight83630B,'POWer %f dbm',amp_set);
fprintf(keysight83630B,'POWer:STATe ON');
%% 频谱仪配置
fprintf(N9020A,'SYST:PRES');
pause(1)
fprintf(N9020A,'FREQ:CENT %f MHz',spec_fre_set(1));
fprintf(N9020A,'FREQ:SPAN %f Hz',span);
fprintf(N9020A,'BAND %f HZ',rbw);
fprintf(N9020A,'SWE:POIN %d',point);
fprintf(N9020A,'DISP:WIND1:TRAC:Y:RLEV %f dBm',y_ref);
%% 采集数据
test     = 24*60+60+1;
amp_meas = zeros(1,test);
fre_meas = zeros(1,test);
time     = zeros(1,test);
tic;

for i = 1:len_speed  %1min,24h需将len_speed替换为test
    if i <= 61
        pause(1)
    else
        pause(60)
    end
    fprintf(N9020A,'CALC:MARK1:MAX');
    fprintf(N9020A,'CALC:MARK1:X?');fre_meas(i)=str2double(fscanf(N9020A));
    fprintf(N9020A,'CALC:MARK1:Y?');amp_meas(i)=str2double(fscanf(N9020A));

    time(i) = toc;

    x = time(1:i)/60;
    y = fre_meas(1:i)-fre_set;

    plot(x,y);
    xlabel('time (min)','FontSize',15);ylabel('Speed (Hz)','FontSize',15);
    title(sprintf('Speed Jitter Range :%.3f Hz',range(y)),'FontSize',15);
end

fprintf(keysight83630B,'POWer:STATe OFF');
%% 保存文件
clock1 = clock;
savefile1 = strcat(File_data,'\',sprintf('%04d%02d%02d_%02d%02d%02.0f_速度稳定性指标测试',clock1(1),clock1(2), ...
    clock1(3),clock1(4),clock1(5),clock1(6)))
save(savefile1,'fre_meas','amp_meas','speed','tar_dis','spec_fre_set',"fre_set",'fd',"RTS_number");
instrreset;
