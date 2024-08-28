clc ; clear ; close all;

% data = load("data\colldata\20240726_192656_Dis_Power_Corr.mat"); % 0206
% data = load("data\verdata\20240726_212334_Dis_Power_Corr_ver.mat"); % 0206
% data = load("data\colldata\20240727_075547_Dis_Power_Corr.mat"); % 0101
% data = load("data\verdata\20240727_092414_Dis_Power_Corr_ver.mat"); % 0101
% data = load("data\verdata\20240727_141510_Dis_Power_Corr_ver_E.mat"); % 0101
data = load("data\verdata\20240727_003303_Dis_Power_Corr_ver.mat"); % 0101

dis = data.dis;
distance = data.distance;
error = data.error;
power = data.power;
fig = figure;
fig.Color = [ 1 1 1];
% fig.Position = [-2559 1 2560 1362];
temp = 5;
dis = dis(temp:end);
power = power(temp:end);
span_x = range(dis)/50;
span_y = range(power)/5;
plot(dis,power);
axis 'auto xy'
axis([min(dis)-span_x max(dis)+span_x min(power)-span_y max(power)+span_y])
grid minor
xlabel('Tar Distance (m)',"FontSize",20,'FontWeight','bold');
ylabel('Tar Gain (dB)','FontSize',20,'FontWeight','bold');
title(sprintf('Gain Jitter Range : %3.3f dB',range(power)),'FontSize',20,'FontWeight','bold');
copygraphics(fig)



