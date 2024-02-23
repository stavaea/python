instrreset
clc ; clear ; close all;
%% Program Set
fre_start            = 7600  ;
fre_end              = 9600 ;
amp_set              = -10  ;
Lf_freq              = 11900;%12783、13033、13283、13533
% temp = '5G231001001_Lf_freq_13533_up';
temp = '2G_11900_231009007_up';
%% Signal Source 83630B program
mult                 = 1;
mult1                = 6;
GPIB_83630B          = 'GPIB0::0::INSTR' ;
GPIB_83712B          = 'GPIB1::20::INSTR' ;
fre_set              = linspace(fre_start,fre_end,point) ;
fre_set1              = fre_set - fre_set(1)+ 79000 - 300; %77998
% fre_set1              = fre_set - 300;
amp_set1              = 13              ;

%% Spec Program
ip_spec = ['TCPIP0::','192.168.1.6','::INSTR'];
spec_fre_set = 300; %fre_set + Lf_freq * 4 - fre_set1
span    = 1000;
rbw     = 100;
y_ref   = -10;
y_div   = 10;
point   = 51;
%% Connect Signal source Spec
keysight83630B = visa('agilent', GPIB_83630B);
fopen(keysight83630B);fprintf(keysight83630B,'*IDN?');fscanf(keysight83630B);


hp83712B = visa('agilent', GPIB_83712B);
fopen(hp83712B);fprintf(hp83712B,'*IDN?');fscanf(hp83712B);

N9020A       = visa('agilent',ip_spec); %设置频谱仪ip
set(N9020A,'InputBufferSize',60e4);
fopen(N9020A);fprintf(N9020A,'*IDN?');fscanf(N9020A) %设置频谱仪

%% Initial spec
fprintf(N9020A,'SYST:PRES'); %重置
pause(1)
fprintf(N9020A,'SWE:POIN %d',point);
fprintf(N9020A,'FREQ:CENT %f MHz',spec_fre_set(1));
fprintf(N9020A,'FREQ:SPAN %f Hz',span);
fprintf(N9020A,'BAND %f HZ',rbw);                     % 设置频谱仪RBW
fprintf(N9020A,'DISP:WIND:TRAC:Y:PDIV %f DB',y_div);        % 设置频谱仪y轴一格代表表示多少dB。
fprintf(N9020A,'DISP:WIND1:TRAC:Y:RLEV %f dBm',y_ref);


%% Initial 83630B
fprintf(hp83712B,'FREQuency:MULTiplier %d',mult);
fprintf(hp83712B,'FREQuency %f MHz',fre_set(1));
fprintf(hp83712B,'POWer %f dbm',amp_set(1));
% fprintf(keysight83630B,'POWer:STATe ON');
fprintf(hp83712B,':OUTPut ON');


%%
fprintf(keysight83630B,'FREQuency:MULTiplier  %d',mult1);
fprintf(keysight83630B,'FREQuency:MULTiplier:STATE ON');
fprintf(keysight83630B,'FREQuency %f MHz',fre_set1(1));
fprintf(keysight83630B,'POWer %f dbm',amp_set1(1));
fprintf(keysight83630B,'POWer:STATe ON');
% fprintf(keysight83630B,':OUTPut ON');

%%Coll
fre_meas = zeros (1,length(fre_set));
amp_meas = zeros (1,length(fre_set));
len_coll = 4;
for i = 1:length(fre_set)
    fprintf(hp83712B,'FREQuency %f MHz',fre_set(i));
    fprintf(keysight83630B,'FREQuency %f MHz',fre_set1(i));
    coll = zeros(1,len_coll);
    for j = 1:len_coll
        pause(0.5)
        fprintf(N9020A,'CALC:MARK1:MAX');         %将mark1设置为最大值
        fprintf(N9020A,'CALC:MARK1:X?');fre_meas(1,i)=str2double(fscanf(N9020A));
        fprintf(N9020A,'CALC:MARK1:Y?');coll(j)=str2double(fscanf(N9020A));
    end
    amp_meas(1,i) = mean(coll,'all');
    x = fre_set(1:i);
    y = amp_meas(1:i);
    plot(x,y);
    xlabel('Freq (MHz)');
    ylabel('Power (dB)');
    title(sprintf('Power Jitter Range : %3.3f dB',range(y)));
    grid minor
end

fprintf(N9020A,':TRAC? TRACE1');
trace = str2num(fscanf(N9020A));

fprintf(keysight83630B,'POWer:STATe OFF');
fprintf(hp83712B,':OUTPut OFF');

%% save
clock1 = clock;

savefile = strcat('data\trace_up\',sprintf('%04d%02d%02d_%02d%02d%02.0f_trace_%s',clock1(1),clock1(2), ...
    clock1(3),clock1(4),clock1(5),clock1(6),temp))
save(savefile,'fre_set',"amp_set","fre_meas","amp_meas","spec_fre_set",'trace');

%% close

instrreset

