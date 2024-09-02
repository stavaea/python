% 该程序用于采集初始化数据
instrreset;
clc ; clear ; close all;

%% 参数设置
% 信号起始频率
start_freq      = 4540;
% 信号结束频率
stop_freq       = 9540;
% 频率步进
step_freq       = 50;
% 衰减设置
Att             = 0:5:100;%0:0.5:100
% 输出信号功率
amp_set         = -40;
% RTS IP
rts_ip          = '192.168.1.10';
% RTS IP 端口号
rts_port        = 7;
% 信号源GPIB
% GPIB_83630B     = 'GPIB0::1::INSTR' ;
GPIB_83630B     = 'GPIB1::20::INSTR' ;
% 频谱仪IP
ip_spec         = ['TCPIP0::','192.168.1.6','::INSTR'];
%% 生成参数
fre_set = start_freq:step_freq:stop_freq;
% fre_set(1) = fre_set(1)+10;
spec_fre_set = fre_set;
span    = 100;
rbw     = 10;
y_ref   = 20;
y_div   = 12;
point   = 1001;
%% 连接仪器
rts = client_sever(rts_ip,rts_port);
keysight83630B = visa('agilent', GPIB_83630B);
fopen(keysight83630B);
N9020A       = visa('agilent',ip_spec);
fopen(N9020A);
%% 初始化信号源
fprintf(keysight83630B,'FREQuency %f MHz',fre_set(1));
fprintf(keysight83630B,'POWer %f dbm',amp_set);
fprintf(keysight83630B,'POWer:STATe ON');
%% 初始化频谱仪
fprintf(N9020A,'SYST:PRES');
pause(1)
fprintf(N9020A,'FREQ:CENT %f MHz',spec_fre_set(1));
fprintf(N9020A,'FREQ:SPAN %f Hz',span);
fprintf(N9020A,'BAND %f HZ',rbw);
fprintf(N9020A,'SWE:POIN %d',point);
fprintf(N9020A,'DISP:WIND1:TRAC:Y:RLEV %f dBm',y_ref);
fprintf(N9020A,'DISP:WIND:TRAC:Y:PDIV %f DB',y_div);
% fprintf(N9020A,'*CAL?');
% % pause(60);
fprintf(N9020A,':CAL:AUTO OFF');
% fprintf(N9020A,':TRACe:TYPE AVERage');
% fprintf(N9020A,':INIT:CONT OFF');
%% 采集数据
amp_meas = zeros(length(fre_set),length(Att));
fre_meas = zeros(length(fre_set),length(Att));
len_fre  = length(fre_set);
len_att  = length(Att);
len_coll = 8;

freq_temp = zeros(1,length(fre_set));
up_temp   = zeros(1,length(fre_set));
down_temp = zeros(1,length(fre_set));

down_corr_table_init(rts);
down_cont_table_init(rts);
% x1 = (0:1:255)/8;
for i = 1:len_fre
    fprintf(N9020A,'DISP:WIND1:TRAC:Y:RLEV %f dBm',y_ref);
    fprintf(keysight83630B,'FREQuency %f MHz',fre_set(i));
    att_control(rts,0);
    fprintf(N9020A,'FREQ:CENT %f MHz',spec_fre_set(i));
%     fprintf(N9020A,':INITiate:RESTart');pause(2)
    pause(1)
    fprintf(N9020A,'CALC:MARK1:MAX');
    fprintf(N9020A,'CALC:MARK1:Y?');y_ref_temp = str2double(fscanf(N9020A));
    fprintf(N9020A,'DISP:WIND1:TRAC:Y:RLEV %f dBm',y_ref_temp+3);

	return_data     = sim_para(rts);
	freq_temp(i)    = return_data(1);
	up_temp(i)      = return_data(2);
	down_temp(i)    = return_data(3);
	freq_temp       = freq_temp(1:i);
	up_temp         = up_temp(1:i);
	down_temp       = down_temp(1:i);
    for j = 1:len_att
        att_control(rts,Att(j));
%         pause(0.3)
%         fprintf(N9020A,':INITiate:RESTart');
%         pause(2)
%         fprintf(N9020A,'CALC:MARK1:MAX');
%         fprintf(N9020A,'CALC:MARK1:X?');fre_meas(i,j)=str2double(fscanf(N9020A));
%         fprintf(N9020A,'CALC:MARK1:Y?');amp_meas(i,j)=str2double(fscanf(N9020A));
        [fre_meas(i,j),amp_meas(i,j),coll] = spec_coll(N9020A,len_coll);
        x = Att(1:j);
%         x = x1(1:j);
        y = amp_meas(i,1:j);
        subplot(121)
        plot(x,y,'LineWidth',1.5);
        xlabel('Set Att (dB)','FontSize',15);ylabel('Coll Power (dB)','FontSize',15);
        title(sprintf('Power Jitter Range : %.3f dB',range(y)),'FontSize',15);
        grid minor;
        subplot(122)
        y = y - y(1);
        error = y + x;
        plot(x,error,'LineWidth',1.5);
        xlabel('Set Att (dB)','FontSize',15);ylabel('Att Error (dB)','FontSize',15);
        grid minor;
    end
%     temperature = up_temp;
%     len_temperature = length(temperature) ;
% 	clock1 = clock;
% 	temp = 1:len_temperature; % 测试用
%     file = strcat('data\corr_data\',sprintf('dca_coll_%d.mat',temperature(temp))); % temp(p):测试用，采集时为temp
%
%     savefile = strcat('data\back_up\',sprintf('%04d%02d%02d_%02d%02d%02.0f_dca_coll_%d.mat',clock1(1),clock1(2), ...
%         clock1(3),clock1(4),clock1(5),clock1(6),temperature(temp)))       % temp(p):测试用，采集时为temp
%     save(file    ,"fre_meas","amp_meas","fre_set","amp_set","temperature","Att");
%     save(savefile,"fre_meas","amp_meas","fre_set","amp_set","temperature","Att");
end
fprintf(keysight83630B,'POWer:STATe OFF');
%% 保存数据
% temperature     = freq_temp                 ;
temp1     = down_temp                 ;
temperature     = -10:4:74                ;
len_temperature = length(temperature)      ;
clock1 = clock;
if min(temp1) > 14 && max(temp1) < 50
     %温度区间大于14小于50
    temperature1 = temperature(8:15)
    len_temperature1 = length(temperature1)
    for temp = 1:len_temperature1

        file = strcat('data\corr_data\',sprintf('dca_coll_%d.mat',temperature1(temp))); % temp(p):测试用，采集时为temp

        savefile = strcat('data\back_up\',sprintf('%04d%02d%02d_%02d%02d%02.0f_dca_coll_%d.mat',clock1(1),clock1(2), ...
            clock1(3),clock1(4),clock1(5),clock1(6),temperature1(temp)))       % temp(p):测试用，采集时为temp
        save(file    ,"fre_meas","amp_meas","fre_set","amp_set","temperature","Att",'temp1');
        save(savefile,"fre_meas","amp_meas","fre_set","amp_set","temperature","Att",'temp1');

    end
elseif max(temp1) < 18
     %温度区间小于18，处于-10~14之间
    temperature2 = temperature(1:7)
    len_temperature2 = length(temperature2)
    for temp = 1:len_temperature2

            file = strcat('data\corr_data\',sprintf('dca_coll_%d.mat',temperature2(temp))); % temp(p):测试用，采集时为temp

            savefile = strcat('data\back_up\',sprintf('%04d%02d%02d_%02d%02d%02.0f_dca_coll_%d.mat',clock1(1),clock1(2), ...
                clock1(3),clock1(4),clock1(5),clock1(6),temperature2(temp)))       % temp(p):测试用，采集时为temp
            save(file    ,"fre_meas","amp_meas","fre_set","amp_set","temperature","Att",'temp1');
            save(savefile,"fre_meas","amp_meas","fre_set","amp_set","temperature","Att",'temp1');

    end
else
    %温度区间大于50，处于50~74之间
    temperature3 = temperature(16:end)
    len_temperature3 = length(temperature3)
    for temp = 1:len_temperature3
            file = strcat('data\corr_data\',sprintf('dca_coll_%d.mat',temperature3(temp))); % temp(p):测试用，采集时为temp

            savefile = strcat('data\back_up\',sprintf('%04d%02d%02d_%02d%02d%02.0f_dca_coll_%d.mat',clock1(1),clock1(2), ...
                clock1(3),clock1(4),clock1(5),clock1(6),temperature3(temp)))       % temp(p):测试用，采集时为temp
            save(file    ,"fre_meas","amp_meas","fre_set","amp_set","temperature","Att",'temp1');
            save(savefile,"fre_meas","amp_meas","fre_set","amp_set","temperature","Att",'temp1');

    end
end
%
%
%
% if min(temp1) >=38
%     for temp = 1:len_temperature % 测试用
%         temp_idx = temperature(temp)
%         if temp_idx >= 38
%             file = strcat('data\corr_data\',sprintf('dca_coll_%d.mat',temperature(temp))); % temp(p):测试用，采集时为temp
%
%             savefile = strcat('data\back_up\',sprintf('%04d%02d%02d_%02d%02d%02.0f_dca_coll_%d.mat',clock1(1),clock1(2), ...
%                 clock1(3),clock1(4),clock1(5),clock1(6),temperature(temp)))       % temp(p):测试用，采集时为temp
%             save(file    ,"fre_meas","amp_meas","fre_set","amp_set","temperature","Att");
%             save(savefile,"fre_meas","amp_meas","fre_set","amp_set","temperature","Att");
%         end
%     end
% else
%     for i = 1:len_temperature % 测试用
%         temp_idx = temperature(i)
%         if temp_idx >= 38
%             file = strcat('data\corr_data\',sprintf('dca_coll_%d.mat',temperature(temp))); % temp(p):测试用，采集时为temp
%
%             savefile = strcat('data\back_up\',sprintf('%04d%02d%02d_%02d%02d%02.0f_dca_coll_%d.mat',clock1(1),clock1(2), ...
%                 clock1(3),clock1(4),clock1(5),clock1(6),temperature(temp)))       % temp(p):测试用，采集时为temp
%             save(file    ,"fre_meas","amp_meas","fre_set","amp_set","temperature","Att");
%             save(savefile,"fre_meas","amp_meas","fre_set","amp_set","temperature","Att");
%
%         else
%             file = strcat('data\corr_data\',sprintf('dca_coll_%d.mat',temperature(temp))); % temp(p):测试用，采集时为temp
%
%             savefile = strcat('data\back_up\',sprintf('%04d%02d%02d_%02d%02d%02.0f_dca_coll_%d.mat',clock1(1),clock1(2), ...
%                 clock1(3),clock1(4),clock1(5),clock1(6),temperature(temp)))       % temp(p):测试用，采集时为temp
%             save(file    ,"fre_meas","amp_meas","fre_set","amp_set","temperature","Att");
%             save(savefile,"fre_meas","amp_meas","fre_set","amp_set","temperature","Att");
%         end
%     end
% end
%
% % % -10:4:74
% temp = temperature
% if temp >= 20 && temp <= 40
%     file = strcat('data\corr_data\',sprintf('dca_coll_%d.mat',temperature(temp))); % temp(p):测试用，采集时为temp
%
%     savefile = strcat('data\back_up\',sprintf('%04d%02d%02d_%02d%02d%02.0f_dca_coll_%d.mat',clock1(1),clock1(2), ...
%         clock1(3),clock1(4),clock1(5),clock1(6),temperature(temp)))       % temp(p):测试用，采集时为temp
%     save(file    ,"fre_meas","amp_meas","fre_set","amp_set","temperature","Att");
%     save(savefile,"fre_meas","amp_meas","fre_set","amp_set","temperature","Att");
% elseif temp >40 && temp<=60
%     file = strcat('data\corr_data\',sprintf('dca_coll_%d.mat',temperature(temp))); % temp(p):测试用，采集时为temp
%
%     savefile = strcat('data\back_up\',sprintf('%04d%02d%02d_%02d%02d%02.0f_dca_coll_%d.mat',clock1(1),clock1(2), ...
%         clock1(3),clock1(4),clock1(5),clock1(6),temperature(temp)))       % temp(p):测试用，采集时为temp
%     save(file    ,"fre_meas","amp_meas","fre_set","amp_set","temperature","Att");
%     save(savefile,"fre_meas","amp_meas","fre_set","amp_set","temperature","Att");
%
% else
%     file = strcat('data\corr_data\',sprintf('dca_coll_%d.mat',temperature(temp))); % temp(p):测试用，采集时为temp
%
%     savefile = strcat('data\back_up\',sprintf('%04d%02d%02d_%02d%02d%02.0f_dca_coll_%d.mat',clock1(1),clock1(2), ...
%         clock1(3),clock1(4),clock1(5),clock1(6),temperature(temp)))       % temp(p):测试用，采集时为temp
%     save(file    ,"fre_meas","amp_meas","fre_set","amp_set","temperature","Att");
%     save(savefile,"fre_meas","amp_meas","fre_set","amp_set","temperature","Att");
% end



% for temp = 1:len_temperature
    % if temp == 20
        % file = strcat('data\corr_data\',sprintf('dca_coll_%d.mat',temperature(temp))); % temp(p):测试用，采集时为temp

        % savefile = strcat('data\back_up\',sprintf('%04d%02d%02d_%02d%02d%02.0f_dca_coll_%d.mat',clock1(1),clock1(2), ...
            % clock1(3),clock1(4),clock1(5),clock1(6),temperature(temp)))       % temp(p):测试用，采集时为temp
        % save(file    ,"fre_meas","amp_meas","fre_set","amp_set","temperature","Att");
        % save(savefile,"fre_meas","amp_meas","fre_set","amp_set","temperature","Att");
    % elseif temp >=40 && temp<=60
        % file = strcat('data\corr_data\',sprintf('dca_coll_%d.mat',temperature(temp))); % temp(p):测试用，采集时为temp

        % savefile = strcat('data\back_up\',sprintf('%04d%02d%02d_%02d%02d%02.0f_dca_coll_%d.mat',clock1(1),clock1(2), ...
            % clock1(3),clock1(4),clock1(5),clock1(6),temperature(temp)))       % temp(p):测试用，采集时为temp
        % save(file    ,"fre_meas","amp_meas","fre_set","amp_set","temperature","Att");
        % save(savefile,"fre_meas","amp_meas","fre_set","amp_set","temperature","Att");
    % else
        % file = strcat('data\corr_data\',sprintf('dca_coll_%d.mat',temperature(temp))); % temp(p):测试用，采集时为temp

        % savefile = strcat('data\back_up\',sprintf('%04d%02d%02d_%02d%02d%02.0f_dca_coll_%d.mat',clock1(1),clock1(2), ...
            % clock1(3),clock1(4),clock1(5),clock1(6),temperature(temp)))       % temp(p):测试用，采集时为temp
        % save(file    ,"fre_meas","amp_meas","fre_set","amp_set","temperature","Att");
        % save(savefile,"fre_meas","amp_meas","fre_set","amp_set","temperature","Att");
    % end
% end
instrreset