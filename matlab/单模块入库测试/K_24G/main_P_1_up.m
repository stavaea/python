%%
instrreset ; clc ; clear ; close all;

%%
fre_start            = 4600  ;
fre_end              = 6600  ;
amp_set              = -25:0.2:0   ; %% 接收-35dBm 发射是-45dBm
Lf_freq              = 9213  ;
number = 'rs_k_up_230914003' ;

% P_1_down
%% Signal Source 83630B program
mult                 = 6   ;
GPIB_83630B          = 'GPIB0::0::INSTR' ;
fre_set              = linspace(fre_start,fre_end,5) ;

%% Spec Program
ip_spec = ['TCPIP0::','192.168.1.6','::INSTR'];
% point                = 2001;
spec_fre_set = fre_set + Lf_freq * 2 ;
span    = 100 ;
rbw     = 10  ;
y_ref   = 10 ;
y_div   = 10  ;

%% Connect Signal source Spec
keysight83630B = visa('agilent', GPIB_83630B);
fopen(keysight83630B);fprintf(keysight83630B,'*IDN?');fscanf(keysight83630B);

N9020A       = visa('agilent',ip_spec); %设置频谱仪ip
set(N9020A,'InputBufferSize',60e4);
fopen(N9020A);fprintf(N9020A,'*IDN?');fscanf(N9020A) %设置频谱仪

%% Initial spec
fprintf(N9020A,'SYST:PRES'); %重置
pause(1)
fprintf(N9020A,'FREQ:CENT %f MHz',spec_fre_set(1));
fprintf(N9020A,'FREQ:SPAN %f Hz',span);
fprintf(N9020A,'BAND %f HZ',rbw);
fprintf(N9020A,'DISP:WIND:TRAC:Y:PDIV %f DB',y_div);
fprintf(N9020A,'DISP:WIND:TRAC:Y:RLEV %f dBm',y_ref);
% fprintf(N9020A,'TRAC:TYPE MAXH');

%% Initial 83630B
fprintf(keysight83630B,'FREQuency %f MHz',fre_set(1));
fprintf(keysight83630B,'POWer %f dbm',amp_set(1));
fprintf(keysight83630B,'POWer:STATe ON');
% fprintf(keysight83630B,':OUTPut ON'); % 83712B

%% Coll Data
fre_meas = zeros (length(fre_set),length(amp_set));
amp_meas = zeros (length(fre_set),length(amp_set));
len_coll = 4;

bar = waitbar(0,'Please wait ...');
for i = 1:length(fre_set)
    fprintf(N9020A,'FREQ:CENT %f MHz',spec_fre_set(i));
    fprintf(keysight83630B,'FREQuency %f MHz',fre_set(i));
    for j = 1:length(amp_set)
        pre = ((i-1)*length(amp_set)+j)/(length(fre_set)*length(amp_set));
        waitbar(pre,bar,sprintf('Freq：%3.0f MHZ Power : %3.3f dB\n%3.1f%%%',fre_set(i),amp_set(j),pre*100));

        fprintf(keysight83630B,'POWer %f dbm',amp_set(j));
        coll = zeros(1,len_coll);
        for m = 1:len_coll
            pause(0.5)
            fprintf(N9020A,'CALC:MARK1:MAX');         %将mark1设置为最大值
            fprintf(N9020A,'CALC:MARK1:X?');fre_meas(i,j)=str2double(fscanf(N9020A));
            fprintf(N9020A,'CALC:MARK1:Y?');coll(m)=str2double(fscanf(N9020A));
        end
        amp_meas(i,j) = mean(coll,"all");
        x = amp_set(1:j);
        y = amp_meas(i,1:j);
        plot(x,y);
    end
end

% fprintf(keysight83630B,'POWer:STATe OFF');
fprintf(keysight83630B,':OUTPut OFF');

%% save
close(bar)
clock1 = clock;

savefile = strcat('data\P_1_up\',sprintf('%04d%02d%02d_%02d%02d%02.0f_trace_%s',clock1(1),clock1(2), ...
    clock1(3),clock1(4),clock1(5),clock1(6),number))
save(savefile,'fre_set',"amp_set","fre_meas","amp_meas");

%% close
instrreset

% run main_sur_up.m
