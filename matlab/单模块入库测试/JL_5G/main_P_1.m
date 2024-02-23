clc ; clear ; close all;

%%
temp = '7202311001-JL-MMWTR-2309';
%% parameter set

com_num = 'com7';
bps     = 1e6;
att_add_down = hex2dec('02');
att_add_up   = hex2dec('21'); %% 压控 数控 固定
len_coll= 1;
%% connect com
com          = serialport(com_num,bps);
com.Parity   = 'none';
com.DataBits = 8;

%% Signal Source 83630B program
mult                 = 6;
GPIB_83630B          = 'GPIB1::20::INSTR' ;
fre_set              = 400:500:5400       ;
amp_set1             = -30:0.2:-8        ;
amp_set2             = -20:0.2:10          ;
amp_set3             = -20:0.2:10          ;
%% Spec Program
ip_spec = ['TCPIP0::','192.168.1.6','::INSTR'];
spec_fre_set = fre_set;
span    = 100;
rbw     = 10;
y_ref   = 20;
y_div   = 10;

%% Connect Signal source Spec
keysight83630B = visa('agilent', GPIB_83630B);
fopen(keysight83630B);fprintf(keysight83630B,'*IDN?');fscanf(keysight83630B);

N9020A       = visa('agilent',ip_spec);
fopen(N9020A);fprintf(N9020A,'*IDN?');fscanf(N9020A);
%% Initial spec
fprintf(N9020A,'SYST:PRES'); %重置
pause(1)
fprintf(N9020A,'FREQ:CENT %f MHz',spec_fre_set(1));
fprintf(N9020A,'FREQ:SPAN %f Hz',span);
fprintf(N9020A,'BAND %f HZ',rbw);                     % 设置频谱仪RBW
fprintf(N9020A,'DISP:WIND:TRAC:Y:PDIV %f DB',y_div);        % 设置频谱仪y轴一格代表表示多少dB。
fprintf(N9020A,'DISP:WIND1:TRAC:Y:RLEV %f dBm',y_ref);
% fprintf(N9020A,'*CAL?');
% pause(60);
% fprintf(N9020A,':CAL:AUTO OFF');

%% Initial 83630B

fprintf(keysight83630B,'FREQuency %f MHz',fre_set(1));
fprintf(keysight83630B,'POWer %f dbm',amp_set1(1));
fprintf(keysight83630B,'POWer:STATe ON');

%% para_att
para_down(1) = att_add_down;
para_down(2) = 120;
para_down(3) = 0;
para_down(4) = mod(para_down(1) + para_down(2) +para_down(3),256);

para_up(1) = att_add_up;
para_up(2) = 40;
para_up(3) = 0;
para_up(4) = mod(para_up(1) + para_up(2) +para_up(3),256);

para_down_zero(1) = att_add_down;
para_down_zero(2) = 0;
para_down_zero(3) = 0;
para_down_zero(4) = mod(para_down_zero(1) + para_down_zero(2) +para_down_zero(3),256);

para_up_zero(1) = att_add_up;
para_up_zero(2) = 0;
para_up_zero(3) = 0;
para_up_zero(4) = mod(para_up_zero(1) + para_up_zero(2) +para_up_zero(3),256);
%% Coll Data
len_freq = length(fre_set);
len_amp1 = length(amp_set1);
len_amp2 = length(amp_set2);
len_amp3 = length(amp_set3);
len      = len_amp3 + len_amp2 + len_amp1;
amp_meas = zeros(len_freq,len);
fre_meas = zeros(len_freq,len);
com.write(para_up_zero,"uint8");
pause(1)
com.write(para_down_zero,"uint8");
pause(1)
for i = 1:len_freq
    fprintf(keysight83630B,'FREQuency %f MHz',fre_set(i));
    fprintf(N9020A,'FREQ:CENT %f MHz',spec_fre_set(i));
    for j = 1:len_amp1
        fprintf(keysight83630B,'POWer %f dbm',amp_set1(j));
        pause(1)
        fprintf(N9020A,'CALC:MARK1:MAX');         %将mark1设置为最大值
        fprintf(N9020A,'CALC:MARK1:X?');fre_meas(i,j)=str2double(fscanf(N9020A));
        fprintf(N9020A,'CALC:MARK1:Y?');amp_meas(i,j)=str2double(fscanf(N9020A));
    end
    %     disp('切换接收射频头串口，即将控制衰减');
    %     pause
    com.write(para_down,"uint8");
    pause(1)
    for k = 1:len_amp2
        fprintf(keysight83630B,'POWer %f dbm',amp_set2(k));
        pause(1)
        fprintf(N9020A,'CALC:MARK1:MAX');         %将mark1设置为最大值
        fprintf(N9020A,'CALC:MARK1:X?');fre_meas(i,j+k)=str2double(fscanf(N9020A));
        fprintf(N9020A,'CALC:MARK1:Y?');amp_meas(i,j+k)=str2double(fscanf(N9020A));
    end
    %     disp('切换发射射频头串口，即将控制衰减');
    %     pause(1)
    com.write(para_up,"uint8");
    pause(1)
    for l = 1:len_amp2
        fprintf(keysight83630B,'POWer %f dbm',amp_set3(l));
        pause(1)
        fprintf(N9020A,'CALC:MARK1:MAX');         %将mark1设置为最大值
        fprintf(N9020A,'CALC:MARK1:X?');fre_meas(i,j+k+l)=str2double(fscanf(N9020A));
        fprintf(N9020A,'CALC:MARK1:Y?');amp_meas(i,j+k+l)=str2double(fscanf(N9020A));
    end
    com.write(para_up_zero,"uint8");
    pause(1)
    com.write(para_down_zero,"uint8");
    pause(1)
    j = 0 ; k = 0 ; l = 0;
end
fprintf(keysight83630B,'POWer:STATe OFF');

%% save

clock1 = clock;
savefile = strcat('data\rf_p_1\',sprintf('%04d%02d%02d_%02d%02d%02.0f_rf_p_1_%s',clock1(1),clock1(2), ...
    clock1(3),clock1(4),clock1(5),clock1(6),temp))
save(savefile,'amp_meas','fre_meas',"amp_set3","amp_set2","amp_set1","fre_set");

%% close

instrreset


