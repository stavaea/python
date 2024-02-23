%%
instrreset ; clc ; clear ; close all;

%%
fre_start            = 23000 ;
fre_end              = 25000 ;
amp_set              = -25   ; %% 接收-35dBm 发射是-45dBm
Lf_freq              = 9213  ;
number = 'rs_k_down_230914003';

%% Signal Source 83630B program
point                = 2001;
mult                 = 6   ;
GPIB_83630B          = 'GPIB0::0::INSTR' ;
fre_set              = linspace(fre_start,fre_end,point) ;

%% Spec Program
ip_spec = ['TCPIP0::','192.168.1.6','::INSTR'];
spec_fre_set = fre_set - Lf_freq * 2 ;
% span    = 100;
% rbw     = 10;
y_ref   = -15;
y_div   = 1  ;

%% Connect Signal source Spec
keysight83630B = visa('agilent', GPIB_83630B);
fopen(keysight83630B);fprintf(keysight83630B,'*IDN?');fscanf(keysight83630B);

N9020A       = visa('agilent',ip_spec); %设置频谱仪ip
set(N9020A,'InputBufferSize',60e4);
fopen(N9020A);fprintf(N9020A,'*IDN?');fscanf(N9020A) %设置频谱仪

%% Initial spec
fprintf(N9020A,'SYST:PRES'); %重置
pause(1)
fprintf(N9020A,'FREQ:STAR %f MHz',spec_fre_set(1));
fprintf(N9020A,'FREQ:STOP %f MHz',spec_fre_set(end));
fprintf(N9020A,'SWE:POIN %d',point);
fprintf(N9020A,'DISP:WIND:TRAC:Y:PDIV %f DB',y_div);
fprintf(N9020A,'DISP:WIND1:TRAC:Y:RLEV %f dBm',y_ref);
fprintf(N9020A,'TRAC:TYPE MAXH');

%% Initial 83630B
fprintf(keysight83630B,'FREQuency %f MHz',fre_set(1));
fprintf(keysight83630B,'POWer %f dbm',amp_set(1));
fprintf(keysight83630B,'POWer:STATe ON');
% fprintf(keysight83630B,':OUTPut ON'); % 83712B

%% Coll Data
for i = 1:length(fre_set)
    fprintf(keysight83630B,'FREQuency %f MHz',fre_set(i));
    pause(0.5);
end

fprintf(N9020A,':TRAC? TRACE1');

trace = str2num(fscanf(N9020A));
fprintf(keysight83630B,'POWer:STATe OFF');

% fprintf(keysight83630B,':OUTPut ON'); % 83712B
%% save
clock1 = clock;

savefile = strcat('data\trace_down\',sprintf('%04d%02d%02d_%02d%02d%02.0f_trace_%s',clock1(1),clock1(2), ...
    clock1(3),clock1(4),clock1(5),clock1(6),number))
save(savefile,'fre_set',"amp_set","trace");

%% close

instrreset














