clc ; clear ; close all;
instrreset
%% parameter set
mode         = 1                           ;    % 1 发射 0 接收
tpye         = 'K波段24GHz上下变频230914002';    % 测试模块名称
com_num      = 'com3';                          % 串口号
bps          = 1000000;                         % 波特率
att_add_down = hex2dec('01');                   % 下变频衰减器地址
att_down     = 0:1:31;                          % 下变频衰减器衰减范围
att_add_up1  = hex2dec('11');                   % 上变频压控衰减器地址
att_add_up2  = hex2dec('12');                   % 上变频数控衰减器地址
att_add_up3  = hex2dec('13');                   % 上变频固定衰减器地址
att_add_up4  = hex2dec('14');                   % 上变频固定衰减器地址
att_add_up5  = hex2dec('15');                   % 上变频固定衰减器地址
att_up1      = 0:0.5:31.5;                      % 上变频压控衰减器衰减范围
att_up2      = 0:0.125:15.875;                  % 上变频数控衰减器衰减范围
att_up3      = 20;                              % 上变频固定衰减器衰减范围
att_up4      = 20;                              % 上变频固定衰减器衰减范围
att_up5      = 35;                              % 上变频固定衰减器衰减范围
fre_set     = 23000:50 :25000        ;             % 测试频率范围
fre_set1     = 23000:500:25000        ;             % 测试频率范围
amp_set      = -40                    ;             % 测试时输出功率
precision    = 0.125;
att_down     = att_down / precision ;
att_up1      = att_up1  / precision ;
att_up2      = att_up2  / precision ;
att_up3      = att_up3  / precision ;
att_up4      = att_up4  / precision ;
att_up5      = att_up5  / precision ;
%% 测试参数，勿动
len_coll= 4;

%% connect com
com          = serialport(com_num,bps);
com.Parity   = 'none';
com.DataBits = 8;

%% Signal Source 83630B program
mult                 = 6;
GPIB_83630B          = 'GPIB0::24::INSTR' ;

%% Spec Program
ip_spec = ['TCPIP0::','192.168.1.6','::INSTR'];
spec_fre_set = fre_set;
span    = 100;
rbw     = 10;
y_ref   = 8;
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
fprintf(N9020A,':CAL:AUTO OFF');

%% Initial 83630B
fprintf(keysight83630B,'FREQuency %f MHz',fre_set(1));
fprintf(keysight83630B,'POWer %f dbm',amp_set);
fprintf(keysight83630B,'POWer:STATe ON');

%% para_att_init

para_up3(1) = att_add_up3;
para_up3(2) = mod(att_up3,256);
para_up3(3) = (att_up3 - para_up3(2))/256;
para_up3(4) = mod(para_up3(1) + para_up3(2) +para_up3(3),256);

para_up4(1) = att_add_up4;
para_up4(2) =mod(att_up4,256);
para_up4(3) =(att_up4 - para_up4(2))/256;
para_up4(4) = mod(para_up4(1) + para_up4(2) +para_up4(3),256);

para_up5(1) = att_add_up5;
para_up5(2) = mod(att_up5,256);
para_up5(3) = (att_up5 - para_up5(2))/256;
para_up5(4) = mod(para_up5(1) + para_up5(2) +para_up5(3),256);

para_down_zero(1) = att_add_down;
para_down_zero(2) = 0;
para_down_zero(3) = 0;
para_down_zero(4) = mod(para_down_zero(1) + para_down_zero(2) +para_down_zero(3),256);

para_up_zero1(1) = att_add_up1;
para_up_zero1(2) = 0;
para_up_zero1(3) = 0;
para_up_zero1(4) = mod(para_up_zero1(1) + para_up_zero1(2) +para_up_zero1(3),256);

para_up_zero2(1) = att_add_up2;
para_up_zero2(2) = 0;
para_up_zero2(3) = 0;
para_up_zero2(4) = mod(para_up_zero2(1) + para_up_zero2(2) +para_up_zero2(3),256);

para_up_zero3(1) = att_add_up3;
para_up_zero3(2) = 0;
para_up_zero3(3) = 0;
para_up_zero3(4) = mod(para_up_zero3(1) + para_up_zero3(2) +para_up_zero3(3),256);

para_up_zero4(1) = att_add_up4;
para_up_zero4(2) = 0;
para_up_zero4(3) = 0;
para_up_zero4(4) = mod(para_up_zero4(1) + para_up_zero4(2) +para_up_zero4(3),256);

para_up_zero5(1) = att_add_up5;
para_up_zero5(2) = 0;
para_up_zero5(3) = 0;
para_up_zero5(4) = mod(para_up_zero5(1) + para_up_zero5(2) +para_up_zero5(3),256);

%% Coll data
len_freq      = length(fre_set);
amp_meas_up3  = zeros(1,len_freq);
amp_meas_up4  = zeros(1,len_freq);
amp_meas_up5  = zeros(1,len_freq);
amp_meas_zero = zeros(1,len_freq);

com.write(para_down_zero,"uint8");
com.write(para_up_zero1 ,"uint8");
com.write(para_up_zero2 ,"uint8");
com.write(para_up_zero3 ,"uint8");
com.write(para_up_zero4 ,"uint8");
com.write(para_up_zero5 ,"uint8");



%% att_up3 att_up4 att_up5
delay_time = 0.5;
if mode ==  0
    for i = 1:len_freq
        fprintf(keysight83630B,'FREQuency %f MHz',fre_set(i));
        fprintf(N9020A,'FREQ:CENT %f MHz',spec_fre_set(i));
        pause(delay_time)

        %% att_up3
        com.write(para_up3,"uint8");
        pause(delay_time)
        fprintf(N9020A,'CALC:MARK1:MAX') ;         %将mark1设置为最大值
        fprintf(N9020A,'CALC:MARK1:Y?')  ;amp_meas_up3(1,i)=str2double(fscanf(N9020A));

        %% Coll zero
        com.write(para_up_zero3,"uint8");
        pause(delay_time)
        fprintf(N9020A,'CALC:MARK1:MAX');         %将mark1设置为最大值
        fprintf(N9020A,'CALC:MARK1:Y?') ;amp_meas_zero(1,i)=str2double(fscanf(N9020A));

        %% att_up4
        com.write(para_up4,"uint8");
        pause(delay_time)
        fprintf(N9020A,'CALC:MARK1:MAX') ;         %将mark1设置为最大值
        fprintf(N9020A,'CALC:MARK1:Y?')  ;amp_meas_up4(1,i)=str2double(fscanf(N9020A));
        com.write(para_up_zero4,"uint8");

        %% att_up5
        com.write(para_up5,"uint8");
        pause(delay_time)
        fprintf(N9020A,'CALC:MARK1:MAX');         %将mark1设置为最大值
        fprintf(N9020A,'CALC:MARK1:Y?') ;amp_meas_up5(1,i)=str2double(fscanf(N9020A));
        com.write(para_up_zero5,"uint8");

        pause(delay_time)
    end
end
%% att_down att_up1 att_up2
com.write(para_down_zero,"uint8");
com.write(para_up_zero1 ,"uint8");
com.write(para_up_zero2 ,"uint8");
com.write(para_up_zero3 ,"uint8");
com.write(para_up_zero4 ,"uint8");
com.write(para_up_zero5 ,"uint8");

len_att_up1  = length(att_up1 );
len_att_up2  = length(att_up2 );
len_att_down = length(att_down);

spec_fre_set = fre_set1;
len_freq     = length(fre_set1);
amp_meas_down = zeros(len_freq,len_att_down);
amp_meas_up1  = zeros(len_freq,len_att_up1);
amp_meas_up2  = zeros(len_freq,len_att_up2);

para = zeros(4,1);

for i = 1:len_freq
    fprintf(keysight83630B,'FREQuency %f MHz',fre_set1(i));
    fprintf(N9020A,'FREQ:CENT %f MHz',spec_fre_set(i));
    pause(1)
    %% rf_up_1
    if mode == 1
        para(1) = att_add_up1;
        for j = 1:len_att_up1
            para(2) = mod(att_up1(j),256);
            para(3) = (att_up1(j) - para(2))/256;
            para(4) = mod(para(1) + para(2) +para(3),256);
            com.write(para,"uint8");
            pause(delay_time)
            fprintf(N9020A,'CALC:MARK1:MAX');         %将mark1设置为最大值
            fprintf(N9020A,'CALC:MARK1:Y?');amp_meas_up1(i,j)=str2double(fscanf(N9020A));
        end
        com.write(para_up_zero1,"uint8");
        pause(delay_time)
        %% rf_up_2
        para(1) = att_add_up2;
        for k = 1:len_att_up2
            para(2) = mod(att_up2(k),256);
            para(3) = (att_up2(k) - para(2))/256;
            para(4) = mod(para(1) + para(2) +para(3),256);
            com.write(para,"uint8");
            pause(delay_time)
            fprintf(N9020A,'CALC:MARK1:MAX');         %将mark1设置为最大值
            fprintf(N9020A,'CALC:MARK1:Y?');amp_meas_up2(i,k)=str2double(fscanf(N9020A));
        end
        com.write(para_up_zero2,"uint8");
        pause(delay_time)
    end
    %% att_down
    if mode == 0
        para(1) = att_add_down;
        for l = 1:len_att_down
            para(2) = mod(att_down(l),256);
            para(3) = (att_down(l) - para(2))/256;
            para(4) = mod(para(1) + para(2) +para(3),256);
            com.write(para,"uint8");
            pause(delay_time)
            fprintf(N9020A,'CALC:MARK1:MAX');         %将mark1设置为最大值
            fprintf(N9020A,'CALC:MARK1:Y?');amp_meas_down(i,l)=str2double(fscanf(N9020A));
        end
        com.write(para_down_zero,"uint8");
        pause(delay_time)
    end
end
fprintf(keysight83630B,'POWer:STATe OFF');
%% save

clock1 = clock;
savefile = strcat('data\rf_att\',sprintf('%04d%02d%02d_%02d%02d%02.0f_RF_att_%s',clock1(1),clock1(2), ...
    clock1(3),clock1(4),clock1(5),clock1(6),tpye))
save(savefile);

%% close
instrreset
