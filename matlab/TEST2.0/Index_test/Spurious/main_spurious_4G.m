% 该程序主要应用于模块的RTSz杂散
% 程序使用信号源83630B、频谱仪N9020A。
instrreset;
clc ; clear ; close all;
%% RTS 模拟器型号参数
% RTS 序列号
RTS_number   = 'SN_bk24058';
% RTS 最小频率(射频) 单位:GHZ
RTS_min_freq = '76';
% RTS 最大频率(射频) 单位:GHZ
RTS_max_freq = '81';
% RTS 类型
% D：数字型 FC：光纤步进型 FS：光纤分段型
RTS_mode     = 'D';
% RTS 瞬时带宽
% 04：0.4GHz 10:1GHz 20:2GHz 40:4GHz 50：5GHz
RTS_inst_band= '50';
%% 参数配置
% RTS IP 地址
RTS_ip   = '192.168.1.10';
% RTS IP 端口号
RTS_port = 7;
% 系统本振 K: 9213 E:11910
freq_lo              = [78000 79000];
% freq_lo              = 24000;
% 中心频率 与测试频率相对应的射频频率
% freq_center          = [77000 79000 81000] ;
freq_center          = freq_lo ;
% 工作频段选择 0：24G 1：77G 2：60G
waveband             = 1;
% RTS接收衰减
rece                 = 0;
% 测试频率
fre_set1              = 5500:500:9500 ;
fre_set2              = 5480:500:9480 ;
% 信号源输出功率
amp_set              = -40  ;
% 信号源GPIB
GPIB_83630B          = 'GPIB0::1::INSTR'                  ;
% 频谱仪IP
ip_spec              = ['TCPIP0::','192.168.1.6','::INSTR'];
% 频谱仪span
span                 = 5e3;
% 频谱仪rbw
rbw                  = 20e3;
% 频谱仪中心频率
% spec_fre_set = fre_set;
% 频谱仪点数
% point                = max(fre_set)-min(fre_set) + 1;
% 频谱仪功率参考
y_ref                = 20;
% 频谱仪span时间
time_delay           = 16;
% 频谱仪频率span
spec_freq_span       = 10;
% point                = point + (spec_freq_span)*2;
%% 保存文件名称
File_path            = '..\Data\';
File                 = strcat(File_path,'RTS',RTS_min_freq,RTS_max_freq,RTS_mode,'_',RTS_inst_band);
File_data            = strcat(File,'\',RTS_number);
Creat_File(File); % 创建保存数据的文件夹
Creat_File(File_data);

%% 连接信号源、频谱仪、RTS
rts            = client_sever(RTS_ip,RTS_port);
keysight83630B = visa('agilent', GPIB_83630B);
fopen(keysight83630B);
N9020A         = visa('agilent',ip_spec);
set(N9020A,'InputBufferSize',60e4);
fopen(N9020A);
%% 信号源配置
% fprintf(keysight83630B,'FREQuency %f MHz',fre_set(1));
fprintf(keysight83630B,'POWer %f dbm',amp_set);
fprintf(keysight83630B,'POWer:STATe ON');
%% 频谱仪配置
fprintf(N9020A,'SYST:PRES');
pause(1)
% fprintf(N9020A,'FREQ:STAR %f MHz',min(spec_fre_set(1),spec_fre_set(end))-spec_freq_span);pause(1)
% fprintf(N9020A,'FREQ:STOP %f MHz',max(spec_fre_set(1),spec_fre_set(end))+spec_freq_span);pause(1)
fprintf(N9020A,'BWID:AUTO ON');
% fprintf(N9020A,'SWE:POIN %d',point);
fprintf(N9020A,'DISP:WIND1:TRAC:Y:RLEV %f dBm',y_ref);

%% 寻找合适的功率参考点
fprintf(N9020A,'DISP:WIND1:TRAC:Y:RLEV %f dBm',y_ref);
% fprintf(keysight83630B,'FREQuency %f MHz',fre_set(1));
pause(2)
fprintf(N9020A,'CALC:MARK1:MAX');
fprintf(N9020A,'CALC:MARK1:Y?');y_ref_temp=str2double(fscanf(N9020A));
fprintf(N9020A,'DISP:WIND1:TRAC:Y:RLEV %f dBm',y_ref_temp+10);
%% 采集数据
% len_fre  = length(fre_set);
len_lo   = length(freq_lo);
fprintf(N9020A,'BAND %f HZ',rbw);
fprintf(N9020A,'BAND:VID %f HZ',rbw);
fprintf(N9020A,':TRACe:TYPE MAXH');

len_freq_lo = length(freq_lo);
for i = 1:len_freq_lo
    if freq_lo(i) == freq_lo(1)
        fre_set = fre_set1;
        freq_center(i) = freq_center(1);
    elseif freq_lo(i) == freq_lo(2)
        fre_set = fre_set2;
        freq_center(i) = freq_center(2);
    end
    spec_fre_set = fre_set;
    point                = max(fre_set)-min(fre_set) + 1;
    point                = point + (spec_freq_span)*2;
    fprintf(N9020A,'SWE:POIN %d',point);
    fprintf(keysight83630B,'FREQuency %f MHz',fre_set(1));
    fprintf(N9020A,'FREQ:STAR %f MHz',min(spec_fre_set(1),spec_fre_set(end))-spec_freq_span);pause(10)
    fprintf(N9020A,'FREQ:STOP %f MHz',max(spec_fre_set(1),spec_fre_set(end))+spec_freq_span);pause(10)
    fprintf(keysight83630B,'FREQuency %f MHz',fre_set(1));
    len_fre  = length(fre_set);
    for j = 1:len_fre
        down_sys_para(rts,freq_lo(i),freq_center(i),rece,waveband);
%         for k = 1:len_fre
        fprintf(keysight83630B,'FREQuency %f MHz',fre_set(j));
        pause(time_delay);
%         end
        fprintf(N9020A,':TRAC? TRACE1');
        trace = str2num(fscanf(N9020A));
        spurious(i,:) = trace;
    end
end

fprintf(keysight83630B,'POWer:STATe OFF');
%% 保存文件
clock1 = clock;
savefile1 = strcat(File_data,'\',sprintf('%04d%02d%02d_%02d%02d%02.0f_杂散指标测试',clock1(1),clock1(2), ...
    clock1(3),clock1(4),clock1(5),clock1(6)))
save(savefile1,'spurious',"fre_set","fre_set1","fre_set2","rbw","RTS_number","spec_freq_span","point","span","freq_lo");
instrreset;











