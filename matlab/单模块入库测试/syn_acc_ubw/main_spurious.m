instrreset
clc ; clear ; close all;

%% Program Set
number               = 'CKD-231101-变频器';
mode                 = 1    ; % 0 : 接收通道 1 : 发射通道
if ~mode
    fre_start            = 7000 ;
    fre_end              = 12000 ;
    amp_set              = -20;
    fre_set              = linspace(fre_start,fre_end,11) ;
    Lf_freq              = 12370  ;
%     spec_fre_set         = fre_set - Lf_freq * 2;
    spec_fre_set         = Lf_freq - fre_set;
    temp = strcat('down_',number);
else
    fre_start            = 370  ;
    fre_end              = 5370 ;
    amp_set              = -20;
    fre_set              = linspace(fre_start,fre_end,11) ;
    Lf_freq              = 12370  ;
%     spec_fre_set         = fre_set + Lf_freq * 2;
    spec_fre_set         = Lf_freq - fre_set;
    temp = strcat('up_',number);
end

% fre_start            = 370 ;
% fre_end              = 5370 ;
% % amp_set              = -20  ;
% temp = strcat('002-放大衰减');
%% Signal Source 83630B program
mult                 = 6;
GPIB_83630B          = 'GPIB0::0::INSTR' ;
% fre_set              = linspace(fre_start,fre_end,201) ;
% amp_set             = -30                ;

%% Spec Program
ip_spec = ['TCPIP0::','192.168.1.6','::INSTR'];
% spec_fre_set = 12370 - fre_set;
% spec_fre_set   = fre_set;
span    = 100;
rbw     = 10;
y_ref   = 15;
y_div   = 10;
point   = 1001;

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
% fprintf(N9020A,'FREQ:STAR %f MHz',spec_fre_set(1));
% fprintf(N9020A,'FREQ:STOP %f MHz',spec_fre_set(end));
fprintf(N9020A,'SWE:POIN %d',point);
% fprintf(N9020A,'TRAC:TYPE MAXH');
fprintf(N9020A,'DISP:WIND:TRAC:Y:PDIV %f DB',y_div);        % 设置频谱仪y轴一格代表表示多少dB。
fprintf(N9020A,'DISP:WIND1:TRAC:Y:RLEV %f dBm',y_ref);


%% Initial 83630B

fprintf(keysight83630B,'FREQuency %f MHz',fre_set(1));
fprintf(keysight83630B,'POWer %f dbm',amp_set(1));
% fprintf(keysight83630B,'POWer:STATe ON');
fprintf(keysight83630B,':OUTPut ON');
%%
[fre_meas, amp_meas, amp_meas1, spurious,trace] = spurious_data(keysight83630B,N9020A,fre_set,point);
% fprintf(keysight83630B,'POWer:STATe OFF');
fprintf(keysight83630B,':OUTPut OFF');
%% save

clock1 = clock;
savefile = strcat('data\sur_ubw\',sprintf('%04d%02d%02d_%02d%02d%02.0f_spurious_%s',clock1(1),clock1(2), ...
    clock1(3),clock1(4),clock1(5),clock1(6),temp))
save(savefile,'fre_meas','amp_meas',"amp_meas1","spurious","trace",'fre_set');

%% close

instrreset

