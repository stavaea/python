clc ; clear ; close all;

%% parameter set
tpye         = '202311001-JL-MMWTR-2309';                        % 测试模块名称
com_num      = 'com7';                          % 串口号
bps          = 1000000;                         % 波特率
att_add_down = hex2dec('02');                   % 下变频衰减器地址
att_down     = 120;                             % 下变频衰减器衰减范围
att_add_up1  = hex2dec('20');                   % 上变频压控衰减器地址
att_add_up2  = hex2dec('21');                   % 上变频数控衰减器地址
att_add_up3  = hex2dec('22');                   % 上变频固定衰减器地址
att_up1      = 0:200:4000;                      % 上变频压控衰减器衰减范围
att_up2      = (0:1:63)*4;                       % 上变频数控衰减器衰减范围
att_up3      = 100;                             % 上变频固定衰减器衰减范围
fre_set      = 400:50:5400        ;             % 测试频率范围
amp_set      = -30                ;             % 测试时输出功率
%% 测试参数，勿动
len_coll= 1;

%% connect com
com          = serialport(com_num,bps);
com.Parity   = 'none';
com.DataBits = 8;

%% Signal Source 83630B program
mult                 = 6;
GPIB_83630B          = 'GPIB1::20::INSTR' ;

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
para_down(1) = att_add_down;
para_down(2) = 120;
para_down(3) = 0;
para_down(4) = mod(para_down(1) + para_down(2) +para_down(3),256);

para_up(1) = att_add_up3;
para_up(2) = 100;
para_up(3) = 0;
para_up(4) = mod(para_up(1) + para_up(2) +para_up(3),256);

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

%% Coll data
len_freq = length(fre_set);
len_att_up1 = length(att_up1);
len_att_up2 = length(att_up2);

amp_meas_down = zeros(1,len_freq);
amp_meas_up3  = zeros(1,len_freq);
amp_meas_zero = zeros(1,len_freq);
para = zeros(4,1);
cnt  = 1;

com.write(para_up_zero2,"uint8");
com.write(para_down_zero,"uint8");
com.write(para_up_zero3,"uint8");
com.write(para_up_zero1,"uint8");




%% att_down & att_up3
for i = 1:len_freq
    fprintf(keysight83630B,'FREQuency %f MHz',fre_set(i));
    fprintf(N9020A,'FREQ:CENT %f MHz',spec_fre_set(i));
    pause(1)
    %% rf_down
    com.write(para_down,"uint8");
    pause(1)
    fprintf(N9020A,'CALC:MARK1:MAX');         %将mark1设置为最大值
    fprintf(N9020A,'CALC:MARK1:Y?');amp_meas_down(1,i)=str2double(fscanf(N9020A));
    com.write(para_down_zero,"uint8");
    pause(1)
    fprintf(N9020A,'CALC:MARK1:MAX');         %将mark1设置为最大值
    fprintf(N9020A,'CALC:MARK1:Y?');amp_meas_zero(1,i)=str2double(fscanf(N9020A));
    %% rf_up_3
    com.write(para_up,"uint8");
    pause(1)
    fprintf(N9020A,'CALC:MARK1:MAX');         %将mark1设置为最大值
    fprintf(N9020A,'CALC:MARK1:Y?');amp_meas_up3(1,i)=str2double(fscanf(N9020A));
    com.write(para_up_zero3,"uint8");
    pause(1)
end

%% att_up1 & up2
fre_set  = 400:400:5400;
spec_fre_set = fre_set;
len_freq = length(fre_set);
amp_meas_up1 = zeros(len_freq,len_att_up1);
amp_meas_up2 = zeros(len_freq,len_att_up2);

for i = 1:len_freq
    fprintf(keysight83630B,'FREQuency %f MHz',fre_set(i));
    fprintf(N9020A,'FREQ:CENT %f MHz',spec_fre_set(i));
    pause(1)
    %% rf_up_1
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
    com.write(para_up_zero1,"uint8");
    pause(1)
    %% rf_up_2
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
    com.write(para_up_zero2,"uint8");
    pause(1)
end
fprintf(keysight83630B,'POWer:STATe OFF');
%% save

clock1 = clock;
savefile = strcat('data\rf_att\',sprintf('%04d%02d%02d_%02d%02d%02.0f_RF_att_%s',clock1(1),clock1(2), ...
    clock1(3),clock1(4),clock1(5),clock1(6),tpye))
save(savefile,'att_add_up1',"att_add_up2","att_add_up3",'att_add_down','att_up1','att_up2',"att_up3",'att_down' ...
    ,"amp_meas_down","amp_meas_up1",'amp_meas_up2',"amp_meas_up3","fre_set","amp_set","amp_meas_zero");

%% close
instrreset
