instrreset;
clc ; clear ; close all;

% temp = 'PZ5G2309001_Fix_out1';
% temp = 'PZ5G2309001_NoFix_out1';
% temp = 'PZ5G2309002_Fix_out1';
% temp = 'PZ5G2309002_NoFix_out1';
% temp = 'PZ5G2309003_Fix_out1';
% temp = 'PZ5G2309003_NoFix_out1';
% temp = 'PZ2G2309003_Fix_out1';
% temp = 'PZ2G2309003_Fix_out2';
% temp = 'PZ2G2309003_NoFix_out1';
% temp = 'PZ2G2309003_NoFix_out2';
% temp   = '022_Fix_out1'; % 12370
temp = '022_NoFix_out1'; % 12370

%% Spec Program
freq    = 13533;
% freq    = 9840;
% freq    = 11450;


ip_spec = ['TCPIP0::','192.168.1.6','::INSTR'];
spec_fre_set = [freq-5000 freq+5000] ;
span    = 100;
rbw     = 10;
y_ref   = 10;
y_div   = 10;
point   = 1001;

%% Connect
N9020A       = visa('agilent',ip_spec); %设置频谱仪ip
set(N9020A,'InputBufferSize',60e4);
fopen(N9020A);fprintf(N9020A,'*IDN?');fscanf(N9020A) %设置频谱仪

fprintf(N9020A,'SYST:PRES'); %重置
pause(1)
fprintf(N9020A,'FREQ:STAR %f MHz',spec_fre_set(1)-20);pause(1)
fprintf(N9020A,'FREQ:STOP %f MHz',spec_fre_set(end)+20);pause(1)
fprintf(N9020A,'SWE:POIN %d',point);
% fprintf(N9020A,'TRAC:TYPE MAXH');
fprintf(N9020A,'DISP:WIND:TRAC:Y:PDIV %f DB',y_div);        % 设置频谱仪y轴一格代表表示多少dB。
fprintf(N9020A,'DISP:WIND1:TRAC:Y:RLEV %f dBm',y_ref);

%%
[fre_meas, amp_meas, amp_meas1, spurious,trace] = spurious_data1(N9020A,point,0,freq);

clock1 = clock;

savefile = strcat('data\spurious\',sprintf('%04d%02d%02d_%02d%02d%02.0f_spurious_%s',clock1(1),clock1(2), ...
    clock1(3),clock1(4),clock1(5),clock1(6),temp))
save(savefile,'fre_meas','amp_meas',"amp_meas1","spurious","trace");
copygraphics(gcf);
instrreset