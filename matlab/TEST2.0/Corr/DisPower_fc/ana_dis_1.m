clc; clear ;close all;
file1 = 'data\colldata\20240726_230429_Dis_Power_Corr.mat';
file2 = 'data\colldata\20240727_020138_Dis_Power_Corr.mat';
file3 = 'data\colldata\20240727_045840_Dis_Power_Corr.mat';
file4 = 'data\colldata\20240727_075547_Dis_Power_Corr.mat';

data1 = load(file1);
data2 = load(file2);
data3 = load(file3);
data4 = load(file4);

start = 10;
step  = 20;

dis    = data1.dis  (start:step:end);
power1 = data1.power(start:step:end);
power2 = data2.power(start:step:end);
power3 = data3.power(start:step:end);
power4 = data4.power(start:step:end);
% power  = power1 - power2;
% power  = power2 - power3;
% power  = power3 - power4;
power  = power4 - power1;

fig = figure;
fig.Color = [ 1 1 1];
fig.Position = [-2559 1 2560 1362];
span_x = range(dis)/50;
span_y = range(power1)/5;
% plot(dis,power1,'Color','r','Marker','*'      ,'LineStyle',':' );
% hold on
% plot(dis,power2,'Color','b','Marker','o'      ,'LineStyle','-' );
% plot(dis,power3,'Color','k','Marker','+'      ,'LineStyle','--');
% plot(dis,power4,'Color','g','Marker','diamond','LineStyle','-.');
% hold off
plot(dis,power,'Color','b','Marker','o','LineStyle','-.');
axis 'auto xy'
% axis([min(dis)-span_x max(dis)+span_x min(power)-span_y max(power)+span_y])
grid minor
xlabel('Tar Distance (m)',"FontSize",20,'FontWeight','bold');
ylabel('Tar Gain (dB)','FontSize',20,'FontWeight','bold');
% leg_str       = ['第一次测试' ; '第二次测试'; '第三次测试'; '第四次测试'];
% leg           = legend(leg_str);
% leg.Box       = "off";
% leg.FontSize  = 15;
% leg.LineWidth = 15;
copygraphics(fig)