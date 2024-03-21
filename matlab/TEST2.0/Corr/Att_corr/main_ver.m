% 该程序用于采集初始化数据
instrreset;
clc ; clear ; close all;

%% 参数设置
% 信号起始频率
start_freq      = 8600;
% 信号结束频率
stop_freq       = 8600;
% 频率步进
step_freq       = 2000;
% 衰减设置
Att             = 0:5:90;
% 输出信号功率
amp_set         = -40;
% RTS IP
rts_ip          = '192.168.1.10';
% RTS IP 端口号
rts_port        = 7;
% 信号源GPIB
GPIB_83630B     = 'GPIB0::0::INSTR' ;
% 频谱仪IP
ip_spec         = ['TCPIP0::','192.168.1.6','::INSTR'];
%% 生成参数
fre_set = start_freq:step_freq:stop_freq;
spec_fre_set = fre_set;
span    = 100;
rbw     = 10;
y_ref   = 20;
y_div   = 12;
point   = 1001;
%% 连接仪器
rts = client_sever(rts_ip,rts_port);
keysight83630B = visa('agilent', GPIB_83630B);
fopen(keysight83630B);
N9020A       = visa('agilent',ip_spec);
fopen(N9020A);
%% 初始化信号源
fprintf(keysight83630B,'FREQuency %f MHz',fre_set(1));
fprintf(keysight83630B,'POWer %f dbm',amp_set);
fprintf(keysight83630B,'POWer:STATe ON');
%% 初始化频谱仪
fprintf(N9020A,'SYST:PRES');
pause(1)
fprintf(N9020A,'FREQ:CENT %f MHz',spec_fre_set(1));
fprintf(N9020A,'FREQ:SPAN %f Hz',span);
fprintf(N9020A,'BAND %f HZ',rbw);
fprintf(N9020A,'SWE:POIN %d',point);
fprintf(N9020A,'DISP:WIND1:TRAC:Y:RLEV %f dBm',y_ref);
fprintf(N9020A,'DISP:WIND:TRAC:Y:PDIV %f DB',y_div);
% fprintf(N9020A,'*CAL?');
% % pause(60);
fprintf(N9020A,':CAL:AUTO OFF');
fprintf(N9020A,':TRACe:TYPE AVERage');
fprintf(N9020A,':INIT:CONT OFF');
%% 采集数据
amp_meas = zeros(length(fre_set),length(Att));
fre_meas = zeros(length(fre_set),length(Att));
len_fre  = length(fre_set);
len_att  = length(Att);
for i = 1:len_fre

    fprintf(N9020A,'DISP:WIND1:TRAC:Y:RLEV %f dBm',y_ref);
    fprintf(keysight83630B,'FREQuency %f MHz',fre_set(i));
    att_control(rts,0);
    fprintf(N9020A,'FREQ:CENT %f MHz',fre_set(i));
    fprintf(N9020A,':INITiate:RESTart');pause(2)
    fprintf(N9020A,'CALC:MARK1:MAX');pause(1)
    fprintf(N9020A,'CALC:MARK1:Y?');y_ref_temp = str2double(fscanf(N9020A));
    fprintf(N9020A,'DISP:WIND1:TRAC:Y:RLEV %f dBm',y_ref_temp+10);
    for j = 1:len_att
        att_control(rts,Att(j));
        pause(0.3)
        fprintf(N9020A,':INITiate:RESTart');
        pause(2)
        fprintf(N9020A,'CALC:MARK1:MAX');
        fprintf(N9020A,'CALC:MARK1:X?');fre_meas(i,j)=str2double(fscanf(N9020A));
        fprintf(N9020A,'CALC:MARK1:Y?');amp_meas(i,j)=str2double(fscanf(N9020A));

        x = Att(1:j);
        y = amp_meas(i,1:j);
        subplot(121);
        plot(x,y,'LineWidth',1.5);
        xlabel('Set Att (dB)','FontSize',15);ylabel('Coll Power (dB)','FontSize',15);
        title(sprintf('Power Jitter Range : %.3f dB',range(y)),'FontSize',15);
        grid minor;
        subplot(122);
        y = y - y(1);
        error = y + x;
        plot(x,error,'LineWidth',1.5);
        xlabel('Set Att (dB)','FontSize',15);ylabel('Att Error (dB)','FontSize',15);
        grid minor;
    end
end
fprintf(keysight83630B,'POWer:STATe OFF');
%% 保存数据
clock1 = clock;
savefile = strcat('data\ver_data\',sprintf('%04d%02d%02d_%02d%02d%02.0f_Ver_coll.mat',clock1(1),clock1(2), ...
    clock1(3),clock1(4),clock1(5),clock1(6)))       % temp(p):测试用，采集时为temp
save(savefile,"fre_meas","amp_meas","fre_set","amp_set","Att");
instrreset
