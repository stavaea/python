instrreset
clc ; clear ; close all;

%% parameter set
number               = '_230704002';  %  202309003
mode         = 0     ;                        % 模式选择 mode == 1  发射 mode == 0 接收
% % tpye         = 'RS_up';                        % 测试模块名称
% tpye         = 'RS_down';                      % 测试模块名称
com_num      = 'com3';                          % 串口号
bps          = 1000000;                         % 波特率
att_add_down = hex2dec('21');                   % 下变频衰减器地址
att_down     = 30/0.125;                        % 下变频衰减器衰减范围
att_add_up1  = hex2dec('22');                   % 上变频衰减器1地址
att_add_up2  = hex2dec('23');                   % 上变频衰减器2地址
att_add_up3  = hex2dec('24');                   % 上变频衰减器3地址
att_add_up4  = hex2dec('25');                   % 上变频衰减器4地址
att_add_up5  = hex2dec('26');                   % 上变频衰减器5地址
att_up1      = (0:0.5:31.5)/0.125;              % 上变频衰减器1衰减范围
att_up2      = (0:0.125:15.875)/0.125;          % 上变频衰减器2衰减范围
att_up3      = 20/0.125;                        % 上变频衰减器3衰减范围
att_up4      = 20/0.125;                        % 上变频衰减器4衰减范围
att_up5      = 32/0.125;                        % 上变频衰减器5衰减范围
if ~mode
    fre_start            = 9800 ;
    fre_end              = 11800 ;
    amp_set              = -55;
    fre_set              = linspace(fre_start,fre_end,11) ;
    spec_fre_set         = 2240 - (fre_set - 7600);
    temp = strcat('rs_fcrm_2G_down',number);
else
    fre_start            = 240  ;
    fre_end              = 2240 ;
    amp_set              = -10;
    fre_set              = linspace(fre_start,fre_end,11) ;
    spec_fre_set         = 7600 - (fre_set - 2240);
    temp = strcat('rs_fcrm_2G_up',number);
end
%% 测试参数，勿动
len_coll= 1;

%% connect com
com          = serialport(com_num,bps);
com.Parity   = 'none';
com.DataBits = 8;

%% Signal Source 83630B program
mult                 = 1;
GPIB_83630B          = 'GPIB1::20::INSTR' ;

%% Spec Program
ip_spec = ['TCPIP0::','192.168.1.6','::INSTR'];
span    = 100;
rbw     = 10;
y_ref   = 0;
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
% fprintf(keysight83630B,'POWer:STATe ON');
fprintf(keysight83630B,':OUTPut ON');
%% Initial att
% 接收通道
para_down(1) = att_add_down;
para_down(2) = att_down;
para_down(3) = 0;
para_down(4) = mod(para_down(1) + para_down(2) +para_down(3),256);

% 发射通道3
para_up3(1) = att_add_up3;
para_up3(2) = att_up3;
para_up3(3) = 0;
para_up3(4) = mod(para_up3(1) + para_up3(2) +para_up3(3),256);

% 发射通道4
para_up4(1) = att_add_up4;
para_up4(2) = att_up4;
para_up4(3) = 0;
para_up4(4) = mod(para_up4(1) + para_up4(2) +para_up4(3),256);

% 发射通道5
para_up5(1) = att_add_up5;
para_up5(2) =  mod(att_up5,256);
para_up5(3) =  (att_up5 - para_up5(2))/256;
para_up5(4) = mod(para_up5(1) + para_up5(2) +para_up5(3),256);

para_down_zero(1) = att_add_down;
para_down_zero(2) = 0;
para_down_zero(3) = 0;
para_down_zero(4) = mod(para_down_zero(1) + para_down_zero(2) +para_down_zero(3),256);

para_up1_zero(1) = att_add_up1;
para_up1_zero(2) = 0;
para_up1_zero(3) = 0;
para_up1_zero(4) = mod(para_up1_zero(1) + para_up1_zero(2) +para_up1_zero(3),256);

para_up2_zero(1) = att_add_up2;
para_up2_zero(2) = 0;
para_up2_zero(3) = 0;
para_up2_zero(4) = mod(para_up2_zero(1) + para_up2_zero(2) +para_up2_zero(3),256);

para_up3_zero(1) = att_add_up3;
para_up3_zero(2) = 0;
para_up3_zero(3) = 0;
para_up3_zero(4) = mod(para_up3_zero(1) + para_up3_zero(2) +para_up3_zero(3),256);

para_up4_zero(1) = att_add_up4;
para_up4_zero(2) = 0;
para_up4_zero(3) = 0;
para_up4_zero(4) = mod(para_up4_zero(1) + para_up4_zero(2) +para_up4_zero(3),256);

para_up5_zero(1) = att_add_up5;
para_up5_zero(2) = 0;
para_up5_zero(3) = 0;
para_up5_zero(4) = mod(para_up5_zero(1) + para_up5_zero(2) +para_up5_zero(3),256);


com.write(para_down_zero,"uint8");
com.write(para_up1_zero,"uint8");
com.write(para_up2_zero,"uint8");
com.write(para_up3_zero,"uint8");
com.write(para_up4_zero,"uint8");
com.write(para_up5_zero,"uint8");
%% Coll data
len_freq    = length(fre_set);


amp_meas_down       = zeros(1,len_freq);
amp_meas_up3        = zeros(1,len_freq);
amp_meas_up4        = zeros(1,len_freq);
amp_meas_up5        = zeros(1,len_freq);
amp_meas_zero3      = zeros(1,len_freq);
amp_meas_zero4      = zeros(1,len_freq);
amp_meas_zero5      = zeros(1,len_freq);
amp_meas_down_zero  = zeros(1,len_freq);
para = zeros(4,1);
cnt  = 1;

%% 固定衰减测试
len_att_up1 = length(att_up1);
len_att_up2 = length(att_up2);
if mode == 1
    for i = 1:len_freq
        fprintf(keysight83630B,'FREQuency %f MHz',fre_set(i));
        fprintf(N9020A,'FREQ:CENT %f MHz',spec_fre_set(i));
        pause(1)
        %% 3
        fprintf(N9020A,'CALC:MARK1:MAX');         %将mark1设置为最大值
        fprintf(N9020A,'CALC:MARK1:Y?');amp_meas_zero3(1,i)=str2double(fscanf(N9020A));

        com.write(para_up3,"uint8");
        pause(1)
        fprintf(N9020A,'CALC:MARK1:MAX') ;         %将mark1设置为最大值
        fprintf(N9020A,'CALC:MARK1:Y?' ) ;amp_meas_up3(1,i)=str2double(fscanf(N9020A));

        com.write(para_up3_zero,"uint8");
        pause(1)

        %% 4
        fprintf(N9020A,'CALC:MARK1:MAX');         %将mark1设置为最大值
        fprintf(N9020A,'CALC:MARK1:Y?');amp_meas_zero4(1,i)=str2double(fscanf(N9020A));

        com.write(para_up4,"uint8");
        pause(1)
        fprintf(N9020A,'CALC:MARK1:MAX') ;         %将mark1设置为最大值
        fprintf(N9020A,'CALC:MARK1:Y?' ) ;amp_meas_up4(1,i)=str2double(fscanf(N9020A));

        com.write(para_up4_zero,"uint8");
        pause(1)
        % 5
        fprintf(N9020A,'CALC:MARK1:MAX');         %将mark1设置为最大值
        fprintf(N9020A,'CALC:MARK1:Y?');amp_meas_zero5(1,i)=str2double(fscanf(N9020A));

        com.write(para_up5,"uint8");
        pause(1)
        fprintf(N9020A,'CALC:MARK1:MAX') ;         %将mark1设置为最大值
        fprintf(N9020A,'CALC:MARK1:Y?' ) ;amp_meas_up5(1,i)=str2double(fscanf(N9020A));

        com.write(para_up5_zero,"uint8");
        pause(1)

    end

    % att_up1 & up2
    fre_set  = 240:100:2240;
    spec_fre_set = 7600 - (fre_set - 2240);
    len_freq = length(fre_set);
    amp_meas_up1 = zeros(len_freq,len_att_up1);
    amp_meas_up2 = zeros(len_freq,len_att_up2);
    amp_meas_up1_zero = zeros(len_freq,1);
    amp_meas_up2_zero = zeros(len_freq,1);

    for i = 1:len_freq
        fprintf(keysight83630B,'FREQuency %f MHz',fre_set(i));
        fprintf(N9020A,'FREQ:CENT %f MHz',spec_fre_set(i));
        pause(1)
        %% rf_up_1
        fprintf(N9020A,'CALC:MARK1:MAX');         %将mark1设置为最大值
        fprintf(N9020A,'CALC:MARK1:Y?');amp_meas_up1_zero(i,1)=str2double(fscanf(N9020A));

        para(1) = att_add_up1;
        for j = 1:len_att_up1
            para(2) = mod(att_up1(j),256);
            para(3) = (att_up1(j) - para(2))/256;
            para(4) = mod(para(1) + para(2) +para(3),256);
            com.write(para,"uint8");
            pause(1)
            fprintf(N9020A,'CALC:MARK1:MAX');         %将mark1设置为最大值
            fprintf(N9020A,'CALC:MARK1:Y?');amp_meas_up1(i,j)=str2double(fscanf(N9020A));
        end
        com.write(para_up1_zero,"uint8");
        pause(1)
        %% rf_up_2
        fprintf(N9020A,'CALC:MARK1:MAX');         %将mark1设置为最大值
        fprintf(N9020A,'CALC:MARK1:Y?');amp_meas_up2_zero(i,1)=str2double(fscanf(N9020A));
        para(1) = att_add_up2;
        for k = 1:len_att_up2
            para(2) = mod(att_up2(k),256);
            para(3) = (att_up2(k) - para(2))/256;
            para(4) = mod(para(1) + para(2) +para(3),256);
            com.write(para,"uint8");
            pause(1)
            fprintf(N9020A,'CALC:MARK1:MAX');         %将mark1设置为最大值
            fprintf(N9020A,'CALC:MARK1:Y?');amp_meas_up2(i,k)=str2double(fscanf(N9020A));
        end
        com.write(para_up2_zero,"uint8");
        pause(1)
    end
    fprintf(keysight83630B,'POWer:STATe OFF');
    %% save

    clock1 = clock;
    savefile = strcat('data\rf_att\',sprintf('%04d%02d%02d_%02d%02d%02.0f_RF_att_up_%s',clock1(1),clock1(2), ...
        clock1(3),clock1(4),clock1(5),clock1(6),number))
    save(savefile);
else


    %% save
    for i = 1:len_freq
        fprintf(keysight83630B,'FREQuency %f MHz',fre_set(i));
        fprintf(N9020A,'FREQ:CENT %f MHz',spec_fre_set(i));
        pause(1)
        %
        fprintf(N9020A,'CALC:MARK1:MAX');         %将mark1设置为最大值
        fprintf(N9020A,'CALC:MARK1:Y?');amp_meas_down_zero(1,i)=str2double(fscanf(N9020A));

        com.write(para_down,"uint8");
        pause(1)
        fprintf(N9020A,'CALC:MARK1:MAX') ;         %将mark1设置为最大值
        fprintf(N9020A,'CALC:MARK1:Y?' ) ;amp_meas_down(1,i)=str2double(fscanf(N9020A));

        com.write(para_down_zero,"uint8");
        pause(1)

    end
    clock1 = clock;
    savefile = strcat('data\rf_att\',sprintf('%04d%02d%02d_%02d%02d%02.0f_RF_att_down_%s',clock1(1),clock1(2), ...
        clock1(3),clock1(4),clock1(5),clock1(6),number))
    save(savefile);
end
%% close
fprintf(keysight83630B,':OUTPut OFF');
instrreset
