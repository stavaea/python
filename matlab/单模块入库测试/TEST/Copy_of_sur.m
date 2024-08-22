instrreset;
clc ; clear ; close all;


% RTS IP 地址
RTS_ip   = '192.168.1.10';
% RTS IP 端口号
RTS_port = 7;
% 工作频段选择 0：24G 1：77G 2：60G
waveband             = 1;
% RTS接收衰减
rece                 = 0;

amp_set              = -40;
fre_set              = 7600:500:9600 ;
% fre_set              = 240:500:2240 ;
spec_fre_set         =   fre_set;
% spec_fre_set         =   fre_set;
temp = strcat('RTS');


freq_lo = 77000;
freq_center          = freq_lo ;
% 信号源GPIB
GPIB_83630B          = 'GPIB0::4::INSTR'                  ;
% 频谱仪IP
ip_spec              = ['TCPIP0::','192.168.1.6','::INSTR'];
% 频谱仪span
span                 = 5e3;
% 频谱仪rbw
rbw                  = 20e3;
% 频谱仪点数
point                = max(fre_set)-min(fre_set) + 1;
% 频谱仪功率参考
y_ref                = 20;
% 频谱仪span时间
time_delay           = 16;
% 频谱仪频率span
spec_freq_span       = 10;
point                = point + (spec_freq_span)*2;


%% 连接信号源、频谱仪、RTS
rts            = client_sever(RTS_ip,RTS_port);
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
fprintf(N9020A,'FREQ:STAR %f MHz',min(spec_fre_set(1),spec_fre_set(end))-spec_freq_span);pause(1)
fprintf(N9020A,'FREQ:STOP %f MHz',max(spec_fre_set(1),spec_fre_set(end))+spec_freq_span);pause(1)
fprintf(N9020A,'BWID:AUTO ON');
fprintf(N9020A,'SWE:POIN %d',point);
fprintf(N9020A,'DISP:WIND1:TRAC:Y:RLEV %f dBm',y_ref);

%% 寻找合适的功率参考点
fprintf(N9020A,'DISP:WIND1:TRAC:Y:RLEV %f dBm',y_ref);
fprintf(keysight83630B,'FREQuency %f MHz',fre_set(1));
pause(2)
fprintf(N9020A,'CALC:MARK1:MAX');
fprintf(N9020A,'CALC:MARK1:Y?');y_ref_temp=str2double(fscanf(N9020A));
fprintf(N9020A,'DISP:WIND1:TRAC:Y:RLEV %f dBm',y_ref_temp+10);
%% 采集数据
len_fre  = length(fre_set);
len_lo   = length(freq_lo);
fprintf(N9020A,'BAND %f HZ',rbw);
fprintf(N9020A,'BAND:VID %f HZ',rbw);
fprintf(N9020A,':TRACe:TYPE MAXH');
for i = 1:len_lo
    down_sys_para(rts,freq_lo(i),freq_center(i),rece,waveband);
    for j = 1:len_fre
       fprintf(keysight83630B,'FREQuency %f MHz',fre_set(j));
       pause(time_delay);
    end
    fprintf(N9020A,':TRAC? TRACE1');
    trace = str2num(fscanf(N9020A));
    spurious(i,:) = trace;


    start_freq = 7600 - spec_freq_span;
    stop_freq  = 9600 + spec_freq_span;
    point = stop_freq -  start_freq + 1;
    x = linspace(start_freq,stop_freq,point);
    y = spurious;
    plot(x,y)
end



%% save

clock1 = clock;
savefile = strcat('data\spurious\',sprintf('%04d%02d%02d_%02d%02d%02.0f_spurious_%s',clock1(1),clock1(2), ...
    clock1(3),clock1(4),clock1(5),clock1(6),temp))
save(savefile);

instrreset;