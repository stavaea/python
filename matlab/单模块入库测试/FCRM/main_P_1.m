instrreset
clc ; clear ; close all;
%% Program Set
number               = '_231009004';
mode                 = 1   ; % 0 : 接收通道 1 : 发射通道
if ~mode
    fre_start            = 4600 ;
    fre_end              = 9600 ;
    amp_set              = -45:0.2:-20  ;
    fre_set              = linspace(fre_start,fre_end,6);
    Lf_freq              = 12040  ;
%     spec_fre_set         = fre_set - Lf_freq * 2;
%     spec_fre_set         = 11868 - (fre_set - 6868);
    spec_fre_set = fre_set;
    temp = strcat('E_fcrm_5G_down',number);
else
    fre_start            = 4600  ;
    fre_end              = 9600 ;
    amp_set              =-55:0.2:-30;
    fre_set              = linspace(fre_start,fre_end,6) ;
    Lf_freq              = 12040  ;
%     spec_fre_set         = fre_set + Lf_freq * 2;
%     spec_fre_set         = 6868 - (fre_set - 11868);
    spec_fre_set = fre_set;
    temp = strcat('E_fcrm_5G_up',number);
end
%% Signal Source 83630B program
mult                  = 1;
GPIB_83712B           = 'GPIB0::0::INSTR' ;

%% Spec Program
ip_spec = ['TCPIP0::','192.168.1.6','::INSTR'];
span    = 1000;
rbw     = 100;
y_ref   = 30;
y_div   = 10;

%% Connect Signal source Spec
hp83712B = visa('agilent', GPIB_83712B);
fopen(hp83712B);fprintf(hp83712B,'*IDN?');fscanf(hp83712B);

N9020A       = visa('agilent',ip_spec); %设置频谱仪ip
set(N9020A,'InputBufferSize',60e4);
fopen(N9020A);fprintf(N9020A,'*IDN?');fscanf(N9020A) %设置频谱仪
%% Initial spec
fprintf(N9020A,'SYST:PRES'); %重置
pause(1)
fprintf(N9020A,'FREQ:CENT %f MHz',spec_fre_set(1));
fprintf(N9020A,'FREQ:SPAN %f Hz',span);
fprintf(N9020A,'BAND %f HZ',rbw);                     % 设置频谱仪RBW
fprintf(N9020A,'DISP:WIND:TRAC:Y:PDIV %f DB',y_div);        % 设置频谱仪y轴一格代表表示多少dB。
fprintf(N9020A,'DISP:WIND1:TRAC:Y:RLEV %f dBm',y_ref);


% %% Initial 83630B
fprintf(hp83712B,'FREQuency:MULTiplier %d',mult);
fprintf(hp83712B,'FREQuency %f MHz',fre_set(1));
fprintf(hp83712B,'POWer %f dbm',amp_set(1));
% fprintf(keysight83630B,'POWer:STATe ON');
fprintf(hp83712B,':OUTPut ON');

%%Coll
fre_meas = zeros (length(fre_set),length(amp_set));
amp_meas = zeros (length(fre_set),length(amp_set));
len_coll = 6;
bar = waitbar(0,'Please wait ...')
for i = 1:length(fre_set)
    fprintf(hp83712B,'FREQuency %f MHz',fre_set(i));
    fprintf(N9020A,'FREQ:CENT %f MHz',spec_fre_set(i));
%     fprintf(keysight83630B,'FREQuency %f MHz',fre_set1(i));
    for j = 1:length(amp_set)
        pre = ((i-1)*length(amp_set)+j)/(length(fre_set)*length(amp_set));
         waitbar(pre,bar,sprintf('Freq：%3.0f MHZ Power : %3.3f dB\n%3.1f%%%',fre_set(i),amp_set(j),pre*100));

        fprintf(hp83712B,'POWER %f dBm',amp_set(j));
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

% fprintf(hp83712B,'POWer:STATe OFF');
fprintf(hp83712B,':OUTPut OFF');
%% save
close(bar)
clock1 = clock;

savefile = strcat('data\rf_p_1\',sprintf('%04d%02d%02d_%02d%02d%02.0f_trace_%s',clock1(1),clock1(2), ...
    clock1(3),clock1(4),clock1(5),clock1(6),temp))
save(savefile);

%% close

instrreset

% pause(2)
% run main_gain.m