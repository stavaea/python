instrreset;
clc ; clear ; close all;

%% 参数设置
speed1 = 100:0.1:(200-0.1);
speed2 = 200:1:999;
speed3 = 1000:0.1:1100;
speed4 = 1101:1:1500;
speed  = 1 * [speed1,speed2,speed3,speed4];

dis = 30;

fre_set = 2900;
amp_set = -40;

fd = 1 * 2*speed*fre_set*1e6/299792458;
fd = fd / 10;
% fd = round(fd);
fd = fd / 1e5;

spec_fre_set = fre_set + fd;
% spec
span    = 100;
rbw     = 10;
y_ref   = 15;
y_div   = 10;

%% rts
rts_ip = '192.168.1.10';
rts_port = 7;

rts = client_sever(rts_ip,rts_port);

%% spec & signal
GPIB_83630B          = 'GPIB5::24::INSTR' ;
keysight83630B = visa('agilent', GPIB_83630B);
fopen(keysight83630B);fprintf(keysight83630B,'*IDN?');fscanf(keysight83630B);


ip_spec = ['TCPIP0::','192.168.1.6','::INSTR'];
N9020A       = visa('agilent',ip_spec);
fopen(N9020A);fprintf(N9020A,'*IDN?');fscanf(N9020A)
%% initial signal
fprintf(keysight83630B,'FREQuency %f MHz',fre_set);
fprintf(keysight83630B,'POWer %f dbm',amp_set);
fprintf(keysight83630B,'POWer:STATe ON');
fprintf(N9020A,'SYST:PRES'); %重置
pause(1)
fprintf(N9020A,'FREQ:CENT %f MHz',spec_fre_set(1));pause(1)
fprintf(N9020A,'FREQ:SPAN %f Hz',span);
fprintf(N9020A,'BAND %f HZ',rbw);
fprintf(N9020A,'DISP:WIND:TRAC:Y:PDIV %f DB',y_div);        % 设置频谱仪y轴一格代表表示多少dB。
fprintf(N9020A,'DISP:WIND1:TRAC:Y:RLEV %f dBm',y_ref);

%%
amp_meas = zeros(1,length(speed));
fre_meas = zeros(1,length(speed));

for i = 1: length(speed)
    down_sim_para(rts,dis,speed(i));
    fprintf(N9020A,'FREQ:CENT %f MHz',spec_fre_set(i));
    pause(1)
    fprintf(N9020A,'CALC:MARK1:MAX');
    fprintf(N9020A,'CALC:MARK1:X?');fre_meas(i)=str2double(fscanf(N9020A));
    fprintf(N9020A,'CALC:MARK1:Y?');amp_meas(i)=str2double(fscanf(N9020A));
    x = speed(1:i);
    y = fre_meas(1:i);
    t = spec_fre_set(1:i);
    error = y - t .* 1e6;
    plot(x,error,'LineWidth',5);
    xlabel('速度/m/s','FontSize',15);ylabel('误差/Hz','FontSize',15);
    title(sprintf('误差抖动为:%.3f Hz',range(error)),'FontSize',15);
end

%% save
clock1 = clock;
savefile1 = strcat('data\',sprintf('%04d%02d%02d_%02d%02d%02.0f_ubw速度指标测试',clock1(1),clock1(2), ...
    clock1(3),clock1(4),clock1(5),clock1(6)))
save(savefile1,'fre_meas','amp_meas','speed','dis','spec_fre_set',"fre_set",'fd');