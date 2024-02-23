instrreset
clc ; clear ; close all;
%% Program Set
% number               = 'CKD-231101-变频器';
% mode                 = 1    ; % 0 : 接收通道 1 : 发射通道
% if ~mode
%     fre_start            = 7000 ;
%     fre_end              = 12000 ;
%     amp_set              = -20  ;
%     fre_set              = linspace(fre_start,fre_end,1001) ;
%     Lf_freq              = 12370  ;
% %     spec_fre_set         = fre_set - Lf_freq * 2;
%     spec_fre_set         = 5370 - (fre_set - 7000) ;
%     temp = strcat('down_',number);
% else
%     fre_start            = 370 ;
%     fre_end              = 5370 ;
%     amp_set              = -20  ;
%     fre_set              = linspace(fre_start,fre_end,1001) ;
%     Lf_freq              = 12370  ;
% %     spec_fre_set         = fre_set + Lf_freq * 2;
%     spec_fre_set         = 7000 - (fre_set - 5370) ;
%     temp = strcat('up_',number);
% end
% number               = '002-放大衰减';
fre_start            = 370 ;
fre_end              = 5370 ;
% % amp_set              = -20  ;
% temp = strcat('002-放大衰减');
temp = strcat('CKD-231101-变频器')
%% Signal Source 83630B program
mult                 = 6;
GPIB_83630B          = 'GPIB0::0::INSTR' ;
fre_set              = linspace(fre_start,fre_end,1001) ;
amp_set              = -20  ;
%% Spec Program
ip_spec = ['TCPIP0::','192.168.1.6','::INSTR'];
spec_fre_set   = fre_set;
span    = 100;
rbw     = 10;
y_ref   = 0;
y_div   = 10;

%% Connect Signal source Spec
keysight83630B = visa('agilent', GPIB_83630B);
fopen(keysight83630B);fprintf(keysight83630B,'*IDN?');fscanf(keysight83630B);

N9020A       = visa('agilent',ip_spec); %设置频谱仪ip
% set(N9020A,'InputBufferSize',60e4);
fopen(N9020A);fprintf(N9020A,'*IDN?');fscanf(N9020A) %设置频谱仪
%% Initial spec
fprintf(N9020A,'SYST:PRES'); %重置
pause(1)
fprintf(N9020A,'FREQ:CENT %f MHz',spec_fre_set(1));
% fprintf(N9020A,'FREQ:CENT %f MHz',spec_fre_set(end));
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
fre_meas = zeros(1,length(fre_set));
amp_meas = zeros(1,length(fre_set));

% bar = waitbar(0,'Please wait ...')
for i = 1:length(fre_set)
    fprintf(keysight83630B,'FREQuency %f MHz',fre_set(i));
    fprintf(N9020A,'FREQ:CENT %f MHz',spec_fre_set(i));
%     pre = ((i-1)*length(fre_set))/(length(fre_set)*length(fre_set));
%     waitbar(pre,bar,sprintf('Freq：%3.0f MHZ Power : %3.3f dB\n%3.1f%%%',fre_set(i),amp_set(i),pre*100));
    pause(1)
    fprintf(N9020A,'CALC:MARK1:MAX');         %将mark1设置为最大值
    fprintf(N9020A,'CALC:MARK1:X?');fre_meas(1,i)=str2double(fscanf(N9020A));
    fprintf(N9020A,'CALC:MARK1:Y?');amp_meas(1,i)=str2double(fscanf(N9020A));
    x = fre_set(1:i);
    y = amp_meas(1:i);
    plot(x,y);
end
% fprintf(keysight83630B,'POWer:STATe OFF');
fprintf(keysight83630B,':OUTPut OFF');
%% save

clock1 = clock;
savefile = strcat('data\gain\',sprintf('%04d%02d%02d_%02d%02d%02.0f_gain_%s',clock1(1),clock1(2), ...
    clock1(3),clock1(4),clock1(5),clock1(6),temp))
save(savefile);

%% close

instrreset

% pause(2)
% run main_spurious.m