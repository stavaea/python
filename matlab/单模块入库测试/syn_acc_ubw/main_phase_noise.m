clc ;clear ; close all;
instrreset
%% Program
spec_fre_set      =  13533 ;
% spec_fre_set      =  9840 ;
spec_fre_set_diff =  [0.1 1 10 100 1000]; % 单位KHz 13533
% file_name         =  'PZ5G2309001_NoFix_out1'; % 11450
% file_name         =  'PZ5G2309001_Fix_out1'; % 9840

% file_name         =  'PZ5G2309002_NoFix_out1'; % 11450
% file_name         =  'PZ5G2309002_Fix_out1'; % 9840

% file_name         =  'PZ2G2309003_NoFix_out1'; % 11450
% file_name         =  'PZ2G2309003_Fix_out1'; % 9840

% file_name         =  'PZ2G2309003_NoFix_out2'; % 11450
% file_name         =  'PZ2G2309003_Fix_out2'; % 9840
% file_name         =  '022_Fix_out1'; % 12370
file_name         =  '022_NoFix_out1'; % 12370

spec_ip           =  ['TCPIP0::','192.168.1.6','::INSTR'];


%%
spec_point        =  10001;
spec_y_ref   = 14;%-20
spec_y_div   = 12;

%% Connect Spec
N9020A       = visa('agilent',spec_ip);
set(N9020A,'InputBufferSize',60e4);
fopen(N9020A);fprintf(N9020A,'*IDN?');fscanf(N9020A);

%% Initial
fprintf(N9020A,'SYST:PRES'); %重置
pause(1)
fprintf(N9020A,'FREQuency:TUNE:IMMediate');  pause(3);
fprintf(N9020A,'DISP:WIND:TRAC:Y:PDIV %f DB',spec_y_div);
fprintf(N9020A,'DISP:WIND1:TRAC:Y:RLEV %f dBm',spec_y_ref);
fprintf(N9020A,'SWE:POIN %d',spec_point);
% fprintf(N9020A,'*CAL?');
% pause(40);
fprintf(N9020A,':CAL:AUTO OFF');

%% Coll Data
[freq_power,phasenoise_power,phasenoise,phasenoise_trace,phasenoise_trace_x]= get_phasenoise(N9020A,spec_fre_set,spec_fre_set_diff,spec_point);

%% Save Data
clock1 = clock;
savefile = strcat(sprintf('data\\Phasenoise\\%04d%02d%02d_%02d%02d%02.0f_%s.mat', ...
    clock1(1),clock1(2),clock1(3),clock1(4),clock1(5),clock1(6),file_name))

save(savefile,"freq_power",'phasenoise_power',"phasenoise","spec_fre_set_diff","phasenoise_trace","phasenoise_trace_x","spec_fre_set");
save("data\Phasenoise\Phasenoise.mat","freq_power",'phasenoise_power',"phasenoise","spec_fre_set_diff","phasenoise_trace","phasenoise_trace_x","spec_fre_set");

%% Export to excel
% writematrix(round(phasenoise_trace_x'),'相噪.xls','Sheet',1,'range','A2');
% writematrix(phasenoise_trace','相噪.xls','Sheet',1,'range','B2');

%% Clear Matlab object
instrreset

run ana_phas.m



