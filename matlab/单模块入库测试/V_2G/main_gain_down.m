clc ; clear ; close all;instrreset
%% Program Set
fre_start            = 58000  ;
fre_end              = 66000  ;
amp_set              = -10     ;
Lf_freq              = 12050;%12783、13033、13283、13533
% temp = '5G231001002_Lf_freq_13533_down';
temp = '2G231001001_down';
%% Signal Source 83630B program
mult                 = 6;
GPIB_83630B          = 'GPIB1::20::INSTR' ;
fre_set              = linspace(fre_start,fre_end,1001) ;
% fre_set              = linspace(fre_start,63000,1001) ;
% fre_set              = linspace(59000,64000,1001) ;
% fre_set              = linspace(60000,65000,1001) ;
% fre_set              = linspace(61000,fre_end,1001) ;
%% Spec Program
ip_spec = ['TCPIP0::','192.168.1.6','::INSTR'];
spec_fre_set = fre_set - Lf_freq * 4;%linspace(7600,9600,1001);
span    = 100;
rbw     = 10;
y_ref   = 20;
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
fprintf(N9020A,'FREQ:SPAN %f Hz',span);
fprintf(N9020A,'BAND %f HZ',rbw);                     % 设置频谱仪RBW
fprintf(N9020A,'DISP:WIND:TRAC:Y:PDIV %f DB',y_div);        % 设置频谱仪y轴一格代表表示多少dB。
fprintf(N9020A,'DISP:WIND1:TRAC:Y:RLEV %f dBm',y_ref);


%% Initial 83630B
fprintf(keysight83630B,'FREQuency:MULTiplier %d',mult);
fprintf(keysight83630B,'FREQuency %f MHz',fre_set(1));
fprintf(keysight83630B,'POWer %f dbm',amp_set(1));
% fprintf(keysight83630B,'POWer:STATe ON');
fprintf(keysight83630B,':OUTPut ON');
%% Coll Data
fre_meas = zeros(1,length(fre_set));
amp_meas = zeros(1,length(fre_set));

for i = 1:length(fre_set)
    fprintf(keysight83630B,'FREQuency %f MHz',fre_set(i));
    fprintf(N9020A,'FREQ:CENT %f MHz',spec_fre_set(i));
    pause(1)
    fprintf(N9020A,'CALC:MARK1:MAX');         %将mark1设置为最大值
    fprintf(N9020A,'CALC:MARK1:X?');fre_meas(1,i)=str2double(fscanf(N9020A));
    fprintf(N9020A,'CALC:MARK1:Y?');amp_meas(1,i)=str2double(fscanf(N9020A));

end
% fprintf(keysight83630B,'POWer:STATe OFF');
fprintf(keysight83630B,':OUTPut OFF');
%% save

clock1 = clock;
savefile = strcat('data\gain_down\',sprintf('%04d%02d%02d_%02d%02d%02.0f_gain_down_%s',clock1(1),clock1(2), ...
    clock1(3),clock1(4),clock1(5),clock1(6),temp))
save(savefile,'amp_meas','fre_meas',"fre_set","amp_set","spec_fre_set");

%% close

instrreset

