instrreset;
clc ; clear ; close all;
%% Program Set
fre_start            = 200  ;
fre_end              = 2300 ;
amp_set              = -40  ;
Lf_freq              = 11400;%12783、13033、13283、13533
temp = 'RCS_shake';%001
% temp = '2G231001001_down';

% RTS IP 地址
RTS_ip   = '192.168.1.10';
% RTS IP 端口号
RTS_port = 7;

%% Signal Source 83630B program
mult                 = 6;
GPIB_83630B          = 'GPIB0::1::INSTR' ;
% fre_set              = linspace(fre_start,fre_end,1001) ;
fre_set              = 7540 ;
% fre_set              = linspace(fre_start,63000,1001) ;
% fre_set              = linspace(59000,64000,1001) ;
% fre_set              = linspace(60000,65000,1001) ;
% fre_set              = linspace(61000,fre_end,1001) ;

%% Spec Program
ip_spec = ['TCPIP0::','192.168.1.6','::INSTR'];
spec_fre_set = fre_set;
span    = 100;
rbw     = 10;
y_ref   = 0;
y_div   = 10;

%% Connect Signal source Spec
rts            = client_sever(RTS_ip,RTS_port);

keysight83630B = visa('agilent', GPIB_83630B);
fopen(keysight83630B);fprintf(keysight83630B,'*IDN?');fscanf(keysight83630B);

N9020A       = visa('agilent',ip_spec); %设置频谱仪ip
% set(N9020A,'InputBufferSize',60e4);
fopen(N9020A);fprintf(N9020A,'*IDN?');fscanf(N9020A) %设置频谱仪
%% Initial spec
fprintf(N9020A,'SYST:PRES'); %重置
pause(1)
fprintf(N9020A,'FREQ:CENT %f MHz',spec_fre_set(1));
fprintf(N9020A,'FREQ:SPAN %f Hz',span);
fprintf(N9020A,'BAND %f HZ',rbw);                     % 设置频谱仪RBW
fprintf(N9020A,'DISP:WIND:TRAC:Y:PDIV %f DB',y_div);        % 设置频谱仪y轴一格代表表示多少dB。
fprintf(N9020A,'DISP:WIND1:TRAC:Y:RLEV %f dBm',y_ref);


%% Initial 83630B

fprintf(keysight83630B,'FREQuency %f MHz',fre_set(1));
fprintf(keysight83630B,'POWer %f dbm',amp_set(1));
% fprintf(keysight83630B,'POWer:STATe ON');
fprintf(keysight83630B,':OUTPut ON');
%% Coll Data
test = 24*60 + 60 + 1;
% test = 5400;
fre_meas = zeros(1,length(fre_set));
amp_meas = zeros(1,length(fre_set));

power = zeros(1,test);
time = zeros(1,test);
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
    fprintf(keysight83630B,'FREQuency %f MHz',fre_set);pause(1)
    fprintf(N9020A,'FREQ:CENT %f MHz',spec_fre_set);
%     fprintf(keysight83630B,'FREQuency %f MHz',fre_set(1));
%     fprintf(N9020A,'FREQ:CENT %f MHz',spec_fre_set(1));
%     pause(1)
%     if i <= 5 * 60
%         pause(1)
%     else
%         pause(60)
%     end

    fprintf(N9020A,'CALC:MARK1:MAX');         %将mark1设置为最大值
    fprintf(N9020A,'CALC:MARK1:X?');fre_meas(1,i)=str2double(fscanf(N9020A));
%     fprintf(N9020A,'CALC:MARK1:Y?');amp_meas(1,i)=str2double(fscanf(N9020A));

    return_data     = sim_para(rts);
    freq_temp(i)    = return_data(1);
    up_temp(i)      = return_data(2);
    down_temp(i)    = return_data(3);
    freq_temp       = freq_temp(1:i);
    up_temp         = up_temp(1:i);
    down_temp       = down_temp(1:i);



    fprintf(N9020A,'CALC:MARK1:Y?');t=str2double(fscanf(N9020A));
    power(i) = t(1);
    time(i) = toc;
    x = time(1:i)/60;
    y = power(1:i);
    subplot(121)
%     plot(x,y,'k-o', 'LineWidth', 1);
%     xlabel('Time (min)','FontSize',15);ylabel('Coll Power (dB)','FontSize',15);
%     title(sprintf('Power Jitter Range : %.3f dB',range(y)),'FontSize',15);
%     grid minor;
%     hold on;
    plot(x,freq_temp,'r-', 'LineWidth', 2);
    grid minor;
    xlabel('Time (min)','FontSize',15);ylabel('Coll syn_Temp (℃)','FontSize',15);
    title(sprintf('Temp Jitter Range : %.3f ℃',range(down_temp)),'FontSize',15);
    hold on;
    subplot(122)
    plot(x,up_temp, 'g--', 'LineWidth', 1.5);
    hold on;
    plot(x,down_temp, 'b:', 'LineWidth', 1);
    grid minor;
    xlabel('Time (min)','FontSize',15);ylabel('Coll Temp (℃)','FontSize',15);
    title(sprintf('Temp Jitter Range : %.3f ℃',range(down_temp)),'FontSize',15);

    legend('up_temp','down_temp')
end
% fprintf(keysight83630B,'POWer:STATe OFF');
fprintf(keysight83630B,':OUTPut OFF');

%% save

clock1 = clock;
savefile = strcat('data\',sprintf('%04d%02d%02d_%02d%02d%02.0f_%s',clock1(1),clock1(2), ...
    clock1(3),clock1(4),clock1(5),clock1(6),temp))
save(savefile,'amp_meas','fre_meas',"fre_set","amp_set","spec_fre_set",'power','time','i',"test",'freq_temp','up_temp','down_temp');

%% close

instrreset;

