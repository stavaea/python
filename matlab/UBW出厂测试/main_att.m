instrreset;
clc ; clear ; close all;

%% 参数设置
att = 0:0.25:63;
rece_att = 0:0.25:30;
fre_set = (400:1000:5400)+1;
amp_set = -40;
spec_fre_set = fre_set;
% spec
span    = 100;
rbw     = 10;
y_ref   = 15;
y_div   = 14;

%% rts
rts_ip = '192.168.1.10';
rts_port = 7;

rts = client_sever(rts_ip,rts_port);

%% spec & signal
GPIB_83630B          = 'GPIB5::24::INSTR' ;
keysight83630B = visa('agilent', GPIB_83630B);
fopen(keysight83630B);fprintf(keysight83630B,'*IDN?');fscanf(keysight83630B);


ip_spec = ['TCPIP0::','192.168.1.6','::INSTR'];
N9020A       = visa('agilent',ip_spec);
fopen(N9020A);fprintf(N9020A,'*IDN?');fscanf(N9020A)
%% initial signal
fprintf(keysight83630B,'FREQuency %f MHz',fre_set(1));
fprintf(keysight83630B,'POWer %f dbm',amp_set);
fprintf(keysight83630B,'POWer:STATe ON');
fprintf(N9020A,'SYST:PRES'); %重置
pause(1)
fprintf(N9020A,'FREQ:CENT %f MHz',spec_fre_set(1));pause(1)
fprintf(N9020A,'FREQ:SPAN %f Hz',span);
fprintf(N9020A,'BAND %f HZ',rbw);
fprintf(N9020A,'DISP:WIND:TRAC:Y:PDIV %f DB',y_div);        % 设置频谱仪y轴一格代表表示多少dB。
fprintf(N9020A,'DISP:WIND1:TRAC:Y:RLEV %f dBm',y_ref);

%%
len = length(rece_att);
amp_meas = zeros(length(fre_set),length(att)+length(rece_att));
fre_meas = zeros(length(fre_set),length(att)+length(rece_att));
len_coll = 4;
for j = 1:length(fre_set)
    fprintf(keysight83630B,'FREQuency %f MHz',fre_set(j));
    fprintf(N9020A,'FREQ:CENT %f MHz',spec_fre_set(j));
    down_sys_para(rts,0);
    att_control(rts,0)
    pause(1)
    for l = 1:len
        down_sys_para(rts,rece_att(l));
        coll = zeros(1,len_coll);
        for m = 1:len_coll
            pause(0.5)
            fprintf(N9020A,'CALC:MARK1:MAX');
            fprintf(N9020A,'CALC:MARK1:X?');fre_meas(j,l)=str2double(fscanf(N9020A));
            fprintf(N9020A,'CALC:MARK1:Y?');coll(m)=str2double(fscanf(N9020A));
        end
        amp_meas(j,l) = mean(coll,"all");
        x = rece_att(1:l);
        y = amp_meas(j,1:l);
        %     t = spec_fre_set(1:i);
        %     error = y - t .* 1e6;
        plot(x,y,'LineWidth',5);
        xlabel('Att (dB)','FontSize',15);ylabel('Coll Power (dB)','FontSize',15);
        title(sprintf('Power Jitter Range : %.3f dB',range(y)),'FontSize',15);
    end


    for i = 1: length(att)
        %     down_sim_para(rts,dis,speed(i));3
        att_control(rts,att(i));
        coll = zeros(1,len_coll);
        for m = 1:len_coll
            pause(0.5)
            fprintf(N9020A,'CALC:MARK1:MAX');
            fprintf(N9020A,'CALC:MARK1:X?');fre_meas(j,i+len)=str2double(fscanf(N9020A));
            fprintf(N9020A,'CALC:MARK1:Y?');coll(m)=str2double(fscanf(N9020A));
        end
        amp_meas(j,i+len)=mean(coll,"all");
        x = [rece_att att(1:i)+rece_att(end)];

        y = amp_meas(j,1:i+len);
        %     t = spec_fre_set(1:i);
        %     error = y - t .* 1e6;
        plot(x,y,'LineWidth',5);
        xlabel('Att (dB)','FontSize',15);ylabel('Coll Power (dB)','FontSize',15);
        title(sprintf('Power Jitter Range : %.3f dB',range(y)),'FontSize',15);
    end
end

%% save
clock1 = clock;
savefile1 = strcat('data\',sprintf('%04d%02d%02d_%02d%02d%02.0f_ubw衰减指标测试',clock1(1),clock1(2), ...
    clock1(3),clock1(4),clock1(5),clock1(6)))
save(savefile1,'fre_meas','amp_meas','att','spec_fre_set',"fre_set");
