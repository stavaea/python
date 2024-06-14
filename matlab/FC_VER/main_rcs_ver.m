instrreset;
clc ; clear ; close all;

%% 设置参数
% cont_file  = 'corr_table\dataE\dca_cont.dat';
% error_file = 'corr_table\dataE\dca_err.dat';
% freq_start = 4540;
% freq_stop  = 9540;
% cont_file  = 'corr_table\dataK_0206\dca_cont.dat';
% error_file = 'corr_table\dataK_0206\dca_err.dat';
cont_file  = 'corr_table\dataE\dca_cont.dat';
error_file = 'corr_table\dataE\dca_err.dat';
% freq_start = 23000;
% freq_stop  = 25000;
freq_start = 24125;
freq_stop  = 24125;
freq_step  = 125;
% Att_ref    = [45 40 30 20 10 5 4.5 4 3 2 1 0.5 0 -0.5 -1 ...
%               -2 -3 -4 -4.5 -5 -10 -20 -30 -40 -45 -50];
% Att_ref    = [45 40 30 20 10 5 0.5 0 -0.5 -5 -10 -20 -30 -35 -40 -45 -50];
Att_ref    = [45 40 35  30  20 15 10 5 0.5 0 -0.5 -5 -10 -15 -20 -25 -30 -35 -40 -45 -50];
Att        = 45 - Att_ref;
spec_ip    = ['TCPIP0::','192.168.1.6','::INSTR'];
signal_source_gpib = 'GPIB0::4::INSTR';
%% rts
% rts_ip     = '192.168.1.11';
rts_ip     = '192.168.1.10';
rts_port   = 7;
rts        = client_sever(rts_ip,rts_port);
rts_reset(rts);
down_sys_para(rts,0,0,78.5,76,1);
% down_sys_para(rts,0,0,24,24,0);
down_sim_para(rts,0,0);

%% Signal Source
fre_set        = freq_start:freq_step:freq_stop;
amp_set        = -47;
keysight83630B = visa('agilent', signal_source_gpib);
fopen(keysight83630B);
%% Spec
spec_fre_set = fre_set;
span         = 100;
rbw          = 3;
y_ref        = 20;
y_div        = 12;
N9020A       = visa('agilent',spec_ip);
fopen(N9020A);
%% Initial
% 初始化信号源
fprintf(keysight83630B,'FREQuency %f MHz',fre_set(1));
fprintf(keysight83630B,'POWer %f dbm',amp_set);
fprintf(keysight83630B,'POWer:STATe ON');
% 初始化频谱仪
fprintf(N9020A,'SYST:PRES');
pause(1)
fprintf(N9020A,'FREQ:CENT %f MHz',spec_fre_set(1));
fprintf(N9020A,'FREQ:SPAN %f Hz',span);
fprintf(N9020A,'BAND %f HZ',rbw);
fprintf(N9020A,'DISP:WIND1:TRAC:Y:RLEV %f dBm',y_ref);
fprintf(N9020A,':TRACe:TYPE AVERage');
fprintf(N9020A,':INIT:CONT OFF');
fprintf(N9020A,'DISP:WIND:TRAC:Y:PDIV %f DB',y_div);
fprintf(N9020A,'DISP:WIND:TRAC:Y:RLEV:OFFS %f',0);
% fprintf(N9020A,'*CAL?');
% pause(60);
%% 采集数据
amp_meas = zeros(length(fre_set),length(Att));
fre_meas = zeros(length(fre_set),length(Att));
len_fre  = length(fre_set);
len_att  = length(Att);
start_simulation(rts);
for i = 1:len_fre
    fprintf(N9020A,'DISP:WIND1:TRAC:Y:RLEV %f dBm',y_ref);
    fprintf(keysight83630B,'FREQuency %f MHz',fre_set(i));
    down_cont_table_corr (rts,cont_file ,fre_set(i),7040);
    down_error_table_corr(rts,error_file,fre_set(i),7040);
%     down_cont_table_corr (rts,cont_file ,fre_set(i),24000);
%     down_error_table_corr(rts,error_file,fre_set(i),24000);
    att_control(rts,0);
    fprintf(N9020A,'FREQ:CENT %f MHz',spec_fre_set(i));
    fprintf(N9020A,':INITiate:RESTart');pause(1)
    fprintf(N9020A,'CALC:MARK1:MAX');pause(1)
    fprintf(N9020A,'CALC:MARK1:Y?');y_ref_temp = str2double(fscanf(N9020A));
    fprintf(N9020A,'DISP:WIND1:TRAC:Y:RLEV %f dBm',y_ref_temp+3);
    for j = 1:len_att
        att_control(rts,Att(j));
        fprintf(N9020A,':INITiate:RESTart');
        pause(0.5)
        fprintf(N9020A,':INITiate:RESTart');
        pause(1)
        fprintf(N9020A,'CALC:MARK1:MAX');
        fprintf(N9020A,'CALC:MARK1:X?');fre_meas(i,j)=str2double(fscanf(N9020A));
        fprintf(N9020A,'CALC:MARK1:Y?');amp_meas(i,j)=str2double(fscanf(N9020A));
        x = Att(1:j);
        y = amp_meas(i,1:j);
        subplot(121)
        plot(x,y,'LineWidth',1.5);
        xlabel('Set Att (dB)','FontSize',15);ylabel('Coll Power (dB)','FontSize',15);
        title(sprintf('Power Jitter Range : %.3f dB',range(y)),'FontSize',15);
        grid minor;
        if(j >= 10)
            subplot(122)
%             title(sprintf('Freq is : %3.3f MHz Att Error',spec_fre_set(j)));
            x = Att_ref(1:j);
            y = y - y(10);
            error = y - x; %  +：多衰减 -:少衰减
            plot(x,error,'-o','LineWidth',1.5);
%             ylim([-1.5 1.5]);
            yline(1,'LineWidth',1.5);
            yline(-1,'LineWidth',1.5);
            xlabel('Set Att (dB)','FontSize',15);ylabel('Att Error (dB)','FontSize',15);
            grid minor;
        elseif i>1
            subplot(122)
%             if (j==1 && i > 1)
%                 title(sprintf('Freq is : %3.3f MHz Att Error',spec_fre_set(end)));
%             elseif j>1
%                 title(sprintf('Freq is : %3.3f MHz Att Error',spec_fre_set(j-1)));
%             end
            plot(Att_ref,error,'-o','LineWidth',1.5);
%             ylim([-1.5 1.5]);
            yline(1,'LineWidth',1.5);
            yline(-1,'LineWidth',1.5);
            xlabel('Set Att (dB)','FontSize',15);ylabel('Att Error (dB)','FontSize',15);
            grid minor;
        end
    end
end
fprintf(keysight83630B,'POWer:STATe OFF');
%% 保存数据
clock1 = clock;
file = strcat('data\back_up_data\',sprintf('0206_Att_Error.mat'));
savefile = strcat('data\back_up_data\',sprintf('%04d%02d%02d_%02d%02d%02.0f_0206_Att_Error.mat',clock1(1),clock1(2), ...
clock1(3),clock1(4),clock1(5),clock1(6)))
save(file    ,"fre_meas","amp_meas","fre_set","amp_set","Att");
save(savefile,"fre_meas","amp_meas","fre_set","amp_set","Att");
instrreset



