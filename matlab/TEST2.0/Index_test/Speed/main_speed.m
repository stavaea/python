% 该程序主要应用于RTS的速度指标测试
% 程序使用信号源83630B、频谱仪N9020A。
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
% 测试频率
fre_set              = [8100 8600] ;
% 信号源输出功率
amp_set              = -40  ;
% 系统本振 K: 9213 E:11910
freq_lo              = [77000 79000];
% 中心频率 与测试频率相对应的射频频率
freq_center          = [76500 79000] ;
% 工作频段选择 0：24G 1：77G 2：60G
waveband             = 1;
% 速度测试点
speed                = [-720:36:-36,-0.5:0.01:0.5,36:36:720]/3.6;
% 信号源GPIB
GPIB_83630B          = 'GPIB0::0::INSTR'                  ;
% 频谱仪IP
ip_spec              = ['TCPIP0::','192.168.1.6','::INSTR'];
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
fprintf(N9020A,'FREQ:CENT %f MHz',fre_set(1));
fprintf(N9020A,'FREQ:SPAN %f Hz',span);
fprintf(N9020A,'BAND %f HZ',rbw);
fprintf(N9020A,'SWE:POIN %d',point);
fprintf(N9020A,'DISP:WIND1:TRAC:Y:RLEV %f dBm',y_ref);
%% 采集数据
amp_meas = zeros(len_fre,len_speed);
fre_meas = zeros(len_fre,len_speed);

for i = 1:len_fre
    fprintf(N9020A,'DISP:WIND1:TRAC:Y:RLEV %f dBm',y_ref);
    down_sim_para(rts,tar_dis,0);
    fprintf(keysight83630B,'FREQuency %f MHz',fre_set(i));
    down_sys_para(rts,freq_lo(i),freq_center(i),rece,waveband);
    down_sim_para(rts,tar_dis,0);
    fprintf(N9020A,'FREQ:CENT %f MHz',fre_set(i));
    pause(2)
    fprintf(N9020A,'CALC:MARK1:MAX');
    fprintf(N9020A,'CALC:MARK1:Y?');y_ref_temp=str2double(fscanf(N9020A));
    fprintf(N9020A,'DISP:WIND1:TRAC:Y:RLEV %f dBm',y_ref_temp+10);
    for j = 1:len_speed
        down_sim_para(rts,tar_dis,speed(j));
        fprintf(N9020A,'FREQ:CENT %f MHz',spec_fre_set(i,j));
        pause(1)
        fprintf(N9020A,'CALC:MARK1:MAX');
        fprintf(N9020A,'CALC:MARK1:X?');fre_meas(i,j)=str2double(fscanf(N9020A));
        fprintf(N9020A,'CALC:MARK1:Y?');amp_meas(i,j)=str2double(fscanf(N9020A));
        x = speed(1:j);
        y = fre_meas(i,1:j);
        t = spec_fre_set(i,1:j);
        error = y - t .* 1e6;
        plot(x,error);
        xlabel('速度/m/s','FontSize',15);ylabel('误差/Hz','FontSize',15);
        title(sprintf('误差抖动为:%.3f Hz',range(error)),'FontSize',15);
    end
    fre_error(i,:) = error;
end
fprintf(keysight83630B,'POWer:STATe OFF');
%% 保存文件
clock1 = clock;
savefile1 = strcat(File_data,'\',sprintf('%04d%02d%02d_%02d%02d%02.0f_速度指标测试',clock1(1),clock1(2), ...
    clock1(3),clock1(4),clock1(5),clock1(6)))
save(savefile1,'fre_meas','amp_meas','speed','tar_dis','spec_fre_set',"fre_set",'fd',"fre_error","RTS_number");
instrreset;











