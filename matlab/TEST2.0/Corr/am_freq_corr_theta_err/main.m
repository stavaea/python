% 该程序主要应用于RTS的平坦度指标测试
instrreset;
clc ; clear ; close all;
%% RTS 模拟器型号参数
% RTS 序列号
RTS_number   = 'SN_bk24062';
% RTS 最小频率(射频) 单位:GHZ
RTS_min_freq = '76';
% RTS 最大频率(射频) 单位:GHZ
RTS_max_freq = '81';
% RTS 类型
% D：数字型 FC：光纤步进型 FS：光纤分段型
RTS_mode     = 'D';
% RTS 瞬时带宽
% 04：0.4GHz 10:1GHz 20:2GHz 40:4GHz 50：5GHz
RTS_inst_band= '50';
%% 参数配置
% RTS IP 地址
RTS_ip   = '192.168.1.10';
% RTS IP 端口号
RTS_port = 7;
% 矢网GPIB
GPIB          = 'GPIB2::16::INSTR'                  ;
% RTS 本振
freq_lo              = [77000 79000 80000];
freq_center          = freq_lo;
% 模拟器工作频段
waveband             = 1;
% 矢网起始频率
start_freq  = 7.6e9;
% 矢网结束频率
stop_freq   = 9.6e9;

% % 频率步进
% step_freq       = 50;
% % RTS 瞬时带宽
% rts_band        = 2000;
% % 下载数据大小
% size_data       = 1001*4 ;
%矢网输出功率
amp_set              = -40  ;
% 矢网信号点数
point = 20001;
%% 连接矢网、RTS
rts            = client_sever(RTS_ip,RTS_port);
N5230C = visa('agilent',GPIB);  % 创建仪器连接对象
set(N5230C,'InputBufferSize',60e4);
fopen(N5230C);                                % 连接仪器
clrdevice(N5230C);                            % 清空
get(N5230C,'Status');                         % 获取仪器状态
fprintf(N5230C, '*IDN?');                     % 询问IDN
idn = fscanf(N5230C);                         % 读取IDN
%% 矢网配置
fprintf(N5230C,'SOUR:POW1 %sdBm',num2str(amp_set));
fprintf(N5230C,'CALCulate:PARameter:DEFine "TEST", S21');  % 定义S21为测试参数
fprintf(N5230C,'DISPlay:WINDow1:TRACe1:FEED "TEST"');
fprintf(N5230C,'DISPlay:WINDow1:TRACe1:STATe ON');
fprintf(N5230C,sprintf('SENSe:FREQuency:STARt %s Hz',num2str(start_freq))); % 设置频率范围高端
fprintf(N5230C,sprintf('SENSe:FREQuency:STOP %s Hz',num2str(stop_freq)));  % 设置频率范围低端
fprintf(N5230C,sprintf('SENSe:SWEep:POINts %s',num2str(point)));  % 设置频率分析点数
% fprintf(N5230C,'CALC:TRAN:TIME:STATe ON');
fprintf(N5230C,'CALC:TRAN:TIME:STATe OFF');
fprintf(N5230C,'DISP:WIND:Y:AUTO');
fprintf(N5230C,'CALC:MARK ON');
fprintf(N5230C,'DISP:WIND:ANN:MARK:RES:STIM 9');
fprintf(N5230C,'DISP:WIND:ANN:MARK:RES:RESP 4');
fprintf(N5230C,'CALC:MARK1:FUNC:EXEC MAX');
fprintf(N5230C,'CALC:MARK:FUNC:TRAC ON');					%开关跟踪
fprintf(N5230C,'CALC:TRAN:TIME:MARK:MODE REFL');
fprintf(N5230C, 'FORM REAL,64');
fprintf(N5230C, 'FORM:BORD SWAP');

%% 幅频修正
pause(1)
power_err1 = 10;
fprintf(N5230C,'CALC:FORM MLOGarithmic');
for i = 1:length(freq_lo)
    power1 = zeros(1001,1)+32767;        %初始表，数值都是32767
    load_am_freq_table(rts,power1);      %下载初始表
    fprintf(N5230C,'DISP:WIND:Y:AUTO');
    fprintf(N5230C,':CALCulate:DATA? FDATA ');
    trace = binblockread(N5230C,'double');
%     power_before = trace(1:20:end);
    power_before = trace;
    File                 = strcat('RTS',RTS_min_freq,RTS_max_freq,RTS_mode,'_',RTS_inst_band);
    File_data            = strcat(File,'_',RTS_number);
    savefile = strcat('data','\',sprintf('%s_幅频修正原始数据',File_data));
    save(savefile,'amp_set','freq_lo','RTS_number','start_freq','stop_freq','power1','power_before');
    pause(1)
%     figure;
    while 1                              %对幅度平坦度反复修正
        % Corr
        fprintf(N5230C,'DISP:WIND:Y:AUTO');
        fprintf(N5230C,':CALCulate:DATA? FDATA ');
        trace_before = binblockread(N5230C,'double');
        power = trace(1:20:end);
%         plot(start_freq/1e6:2:stop_freq/1e6,power);xlabel('频率/ MHz');ylabel('功率/ dBm');
%         title (sprintf('功率抖动 ：%3.2f dB',range(power)));
        power = power - min (power);
        power=10.^(power/20);
        power=1./power;
        power=power*32767;
        power = fliplr(power')';
        power1 = power.*power1;
        power1 = power1*32767/max(power1);     %保证最大修正值为32767
        power1 = round(power1);
        % 下载校正表
        load_am_freq_table(rts,power1);
        pause(1)
        fprintf(N5230C,'DISP:WIND:Y:AUTO');
        fprintf(N5230C,':CALCulate:DATA? FDATA ');
        trace = binblockread(N5230C,'double');
        trace_corr_temp = trace;
        power_err = range(trace);
        trace_corr(i,:) = trace';
%         plot(start_freq/1e6:2:stop_freq/1e6,trace(1:20:end));xlabel('频率/ MHz');ylabel('功率/ dBm');
%         title (sprintf('功率抖动 ：%3.2f dB',power_err));
        am_freq_corr_plot(linspace(start_freq/1e6,stop_freq/1e6,point),trace_before,trace_corr_temp);
        if power_err < power_err1
            power_err1 = power_err;
            %  保存数据
            save power.mat power1;
        end
        if(power_err<0.5)                            %当误差小于0.5db时，保存幅频修正文件，退出修正，否则继续修正
            file = sprintf('amp_corr_table\\%0d\\AmpFreqtable1.dat',freq_lo(i)/1e3);
            fid=fopen(file,'w');
            for j=1:length(power1)
                fwrite(fid,power1(j,:),'uint32');
            end
            fclose(fid);
            file1 = sprintf('amp_corr_table\\%0d\\AmpFreqtable2.dat',freq_lo(i)/1e3);
            fid=fopen(file1,'w');
            for j=1:length(power1)
                fwrite(fid,power1(j,:),'uint32');
            end
            fclose (fid);
            break;
        else
            continue;
        end
    end
end
%% 相频修正
pause(1)
fprintf(N5230C,'CALC:FORM PHASe');
Theta_err1 = 360;
load power;
figure;
for i = 1:length(freq_lo)
    amp_Theta_corr1 = power1;                     %初始表
    Theta1 = zeros(1001,1);
    num = 0;
    load_am_freq_table(rts,amp_Theta_corr1);      %下载初始表
    pause(1)
    while 1                              %对相位坦度反复修正
        % Corr
        fprintf(N5230C,'DISP:WIND:Y:AUTO');
        fprintf(N5230C,':CALCulate:DATA? FDATA ');
        trace = binblockread(N5230C,'double');
        Theta = trace(1:20:end);
%         plot(start_freq/1e6:2:stop_freq/1e6,Theta);xlabel('频率/ MHz');ylabel('相位/ °');
%         title (sprintf('相位抖动 ：%3.2f °',range(Theta)));
        if num == 0
            Theta1 = Theta1 - Theta;
            num =1;
        else
            Theta1 = Theta1 + Theta;
        end
        for k=1:length(Theta1)
            if Theta1(k) > 180
                Theta1(k) = Theta1(k) - 360;
            end
            if Theta1(k) < -180
                Theta1(k) = Theta1(k) + 360;
            end
        end
        amp_Theta_corr = power1.*exp(1i*Theta1*pi/180);
        imag_amp_Theta_corr=imag(amp_Theta_corr);
        real_amp_Theta_corr=real(amp_Theta_corr);
        for k=1:length(Theta1)
            if imag_amp_Theta_corr(k)<0
                imag_amp_Theta_corr(k) = 65536+imag_amp_Theta_corr(k);
            end
            if real_amp_Theta_corr(k)<0
                real_amp_Theta_corr(k) = 65536+real_amp_Theta_corr(k);
            end
        end
        amp_Theta_corr = 65536*round(imag_amp_Theta_corr)+round(real_amp_Theta_corr);
        % 下载校正表
        load_am_freq_table(rts,amp_Theta_corr);
        pause(1)
        fprintf(N5230C,'DISP:WIND:Y:AUTO');
        fprintf(N5230C,':CALCulate:DATA? FDATA ');
        trace = binblockread(N5230C,'double');
        Theta_err = std(trace);
        plot(start_freq/1e6:2:stop_freq/1e6,trace(1:20:end));xlabel('频率/ MHz');ylabel('相位/ °');
        title (sprintf('相位方差 ：%3.2f °',Theta_err));
        if Theta_err < Theta_err1
            Theta_err1 = Theta_err;
            %  保存数据
            save Theta.mat Theta1;
            save amp_Theta_corr.mat amp_Theta_corr;
        end
        if(Theta_err<1)                            %当方差小于1°时，保存幅频修正文件，退出修正，否则继续修正

%             amp_Theta_dat             = [ step_freq , rts_band , size_data , amp_Theta_corr];
            file = sprintf('corr_table\\%0d\\AmpFreqtable1.dat',freq_lo(i)/1e3);
            fid=fopen(file,'w');
            for j=1:length(amp_Theta_corr)
                fwrite(fid,amp_Theta_corr(j,:),'uint32');
            end
            fclose(fid);
            file1 = sprintf('corr_table\\%0d\\AmpFreqtable2.dat',freq_lo(i)/1e3);
            fid=fopen(file1,'w');
            for j=1:length(amp_Theta_corr)
                fwrite(fid,amp_Theta_corr(j,:),'uint32');
            end
            fclose (fid);
            break;
        else
            continue;
        end
    end
end

%% 保存文件
File                 = strcat('RTS',RTS_min_freq,RTS_max_freq,RTS_mode,'_',RTS_inst_band);
File_data            = strcat(File,'_',RTS_number);
clock1 = clock;
savefile = strcat('data','\',sprintf('%s_幅频修正数据',File_data));
save(savefile,'amp_set','freq_lo','RTS_number','start_freq','stop_freq','power1','Theta1',"trace_corr");

savefile1 = strcat('data\back_up\',sprintf('%04d%02d%02d_%02d%02d%02.0f_%s_幅频修正数据',clock1(1),clock1(2), ...
    clock1(3),clock1(4),clock1(5),clock1(6),File_data))
save(savefile1,'trace_before','amp_set','freq_lo','RTS_number','start_freq','stop_freq','power','trace_corr','power1','Theta1');
instrreset;


