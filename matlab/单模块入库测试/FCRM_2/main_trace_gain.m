instrreset
clc ; clear ; close all;
%% Program Set
number               = '_231009007';
mode                 = 1    ; % 0 : 接收通道 1 : 发射通道
if ~mode
    fre_start            = 7600 ;
    fre_end              = 9600 ;
    amp_set              = -50;
    fre_set              = linspace(fre_start,fre_end,51) ;
    Lf_freq              = 9840  ;
%     spec_fre_set         = fre_set - Lf_freq * 2;
    spec_fre_set         = 2240 - (fre_set - 7600);
    temp = strcat('E_fcrm_2G_down',number);
else
    fre_start            = 240  ;
    fre_end              = 2240 ;
    amp_set              = -20;
    fre_set              = linspace(fre_start,fre_end,51) ;
    Lf_freq              = 9840  ;
%     spec_fre_set         = fre_set + Lf_freq * 2;
    spec_fre_set         = 7600 - (fre_set - 2240);
    temp = strcat('E_fcrm_2G_up',number);
end
%% Signal Source 83630B program
mult                 = 6;
GPIB_83630B          = 'GPIB0::0::INSTR' ;
%% Spec Program
ip_spec = ['TCPIP0::','192.168.1.6','::INSTR'];
% spec_fre_set = fre_set - Lf_freq * 6 ;
span    = 100;
rbw     = 10;
y_ref   = -14;
y_div   = 1;
point   = 51;
%% Connect Signal source Spec
keysight83630B = visa('agilent', GPIB_83630B);
fopen(keysight83630B);fprintf(keysight83630B,'*IDN?');fscanf(keysight83630B);

N9020A       = visa('agilent',ip_spec); %设置频谱仪ip
set(N9020A,'InputBufferSize',60e4);
fopen(N9020A);fprintf(N9020A,'*IDN?');fscanf(N9020A) %设置频谱仪
%% Initial spec
fprintf(N9020A,'SYST:PRES'); %重置
pause(1)
fprintf(N9020A,'FREQ:STAR %f MHz',spec_fre_set(end));
fprintf(N9020A,'FREQ:STOP %f MHz',spec_fre_set(1));
fprintf(N9020A,'SWE:POIN %d',point);
fprintf(N9020A,'TRAC:TYPE MAXH');
fprintf(N9020A,'DISP:WIND:TRAC:Y:PDIV %f DB',y_div);        % 设置频谱仪y轴一格代表表示多少dB。
fprintf(N9020A,'DISP:WIND1:TRAC:Y:RLEV %f dBm',y_ref);


%% Initial 83630B
% fprintf(keysight83630B,'FREQuency:MULTiplier %d',mult);
fprintf(keysight83630B,'FREQuency %f MHz',fre_set(1));
fprintf(keysight83630B,'POWer %f dbm',amp_set(1));
% fprintf(keysight83630B,'POWer:STATe ON');
fprintf(keysight83630B,':OUTPut ON');

%%
for i = 1:length(fre_set)
    fprintf(keysight83630B,'FREQuency %f MHz',fre_set(i));
    pause(0.5);
end
% for i = 1:length(fre_set)
%     fprintf(keysight83630B,'FREQuency %f MHz',fre_set(i));
%     pause(0.5);
% end

fprintf(N9020A,':TRAC? TRACE1');
trace = str2num(fscanf(N9020A));
% fprintf(keysight83630B,'POWer:STATe OFF');
fprintf(keysight83630B,':OUTPut OFF');
%% save
clock1 = clock;

savefile = strcat('data\trace\',sprintf('%04d%02d%02d_%02d%02d%02.0f_trace_%s',clock1(1),clock1(2), ...
    clock1(3),clock1(4),clock1(5),clock1(6),temp))
save(savefile,'fre_set',"amp_set","trace","spec_fre_set");

%% close

instrreset

% pause(2)
% run main_sur_down.m