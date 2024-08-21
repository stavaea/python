clear
clc
close all;
%%Edited by JHQ, 20230215, LCRT
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%需手动设置部分
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% f=fopen('D:\Project\matlab\TimeFreqFigRead\短距.txt'); %路径+
mode = 2 ; % 模拟器瞬时工作带宽   1:1G 2 ：2G
f=fopen('000.dat', 'r'); %路径
fc=77; %显控软件系统参数设置的本振GHz
length_timefreqq = 100; %时长 		单位：ms
ratio_timefreq = 1.008; %时间分辨率 	单位：us
Rrts = 2;			% 雷达与模拟器距离
Gr0 = 50;			% 模拟器设置最大接收通道增益 默认值：50dB
rece_power  = -25;	% 接收衰减量
EIRP_yita  = -5 ;   % EIRP 校正值
Gr = 15;			% 模拟器接收天线增益
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% a = fread(f, inf, 'int16');
% data = a';
% a=textscan(f,'%s');
% Tc=a{1,1}(3,1);
% dtc=a{1,1}(6,1);
% T=str2num(cell2mat(Tc));
% dt=str2num(cell2mat(dtc));
% datac=a{1,1}(8:end,1);
% data=zeros(length(datac),1);
% for i=1:length(datac)
% data(i,1)=str2num(cell2mat(datac(i,1)));
% end
data = fread(f, inf, 'uint16')';


%% freq
if mode == 1
	fq = 0.6 + fc - data(6:2:end)/32/1000;
else
	fq = 1.24 + fc - data(6:2:end)/16/1000;
end

%% power
power_data = data(5:2:end)/10;%功率
% EIRP = Pr - Gr - Gra - Gr0 - rece_power - Lcabler + EIRP_yita;
Pyita = 0;
Pr=power_data*0.0625+Pyita;
% Pr = 3 - 20 * log10(2047./power_data) + Pyita;
Lcabler = 0;
Gra=10*log10((3*10^8/(fc*10^9))^2/((4*pi*Rrts)^2));

EIRP = Pr - Gr - Gra - Gr0 - rece_power - Lcabler + EIRP_yita;
%% time
t = (1:length(power_data)) .* ratio_timefreq ;

%% figure
figure('Color',[1,1,1]);
% yyaxis left
fq_fig = plot(t,fq);
fq_fig.LineStyle = '-.';
fq_fig.Color = 'b';
fq_fig.LineWidth = 2;
xlabel('时间/us');
ylabel('频率/GHz','Color','b');
title('时频图');
grid on;


figure('Color',[1,1,1]);
% yyaxis right;
power_fig = plot(t,EIRP,'Color','r');
power_fig.LineStyle = ':';
power_fig.Color = 'r';
power_fig.LineWidth = 2;
xlabel('时间/us');
ylabel('功率/dBm');
title('功率图');
grid on;