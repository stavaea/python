clc ; clear ; close all;
%% 文件路径
% DataFile_path = '..\Data\RTS7681D_50\SN_bk24056\20240608_184130_距离RCS稳定性测试';
% DataFile_path = '..\Data\RTS7681D_50\SN_bk24056\20240609_092946_距离RCS稳定性测试';
% DataFile_path = '..\Data\RTS7681D_50\SN_bk24056\20240612_094655_距离RCS稳定性测试';
DataFile_path = '..\Data\RTS7681D_50\SN_bk24056\20240613_144207_距离RCS稳定性测试';
% DataFile_path = '..\Data\RTS2325D_20\SN_bk24021\20240606_095235_距离RCS稳定性测试';
% DataFile_path = 'D:\work\bit\20240305_160339_距离指标测试';
%% 加载数据
data = load(DataFile_path);
%% 数据加载及处理
% 设置距离 单位：m
set_distance   = data.tar_dis;
% 采集距离 单位：m
coll_distance  = data.distance(1:360);
% 距离误差 单位：mm
error_distance = coll_distance - set_distance;
error_distance = error_distance * 1e3;
% x-->789
freq_temp      = data.freq_temp(1:360);
up_temp        = data.up_temp(1:360);
down_temp      = data.down_temp(1:360);

time  = data.time(1:360) / 3600;
power = data.power(1:360);
x     = time;
y     = error_distance;
y1    = power;


% 画图
figure;
plot(x, y);
grid minor;
xlabel('Time (hour)','FontSize',15);ylabel('Distance Error (mm)','FontSize',15);
title(sprintf('Dis Jitter Range :%.3f mm',range(y)),'FontSize',15);
minn = min(y);maxx=max(y);
x1 = yline(maxx);
x1.LineWidth = 1.5;
x1.FontSize = 15;
x1.Color = 'black';
x1.LineStyle = '-.';
x1.Label = sprintf('Max Distance Error %.3f mm',maxx);
x1.LabelHorizontalAlignment = 'left';
x1.LabelVerticalAlignment = 'top';
x2 = yline(minn);
x2.LineWidth = 1.5;
x2.FontSize = 15;
x2.Color = 'black';
x2.LineStyle = '-.';
x2.Label = sprintf('Min Distance Error %.3f mm',minn);
x2.LabelHorizontalAlignment = 'left';
x2.LabelVerticalAlignment = 'bottom';


% hold on;
figure;
hold on;
plot(x,y1,'LineWidth', 1.5);hold on;
% plot(x,freq_temp,'r-', 'LineWidth', 2);hold on;
% plot(x,up_temp, 'g--', 'LineWidth', 1.5);hold on;
% plot(x,down_temp, 'b:', 'LineWidth', 1);
xlabel('Time (hour)','FontSize',15);ylabel('Power (dB)','FontSize',15);
title(sprintf('Power Jitter Range : %.3f dB',range(y1)),'FontSize',15);
minn = min(y1);maxx=max(y1);
x1 = yline(maxx);
x1.LineWidth = 1.5;
x1.FontSize = 15;
x1.Color = 'black';
x1.LineStyle = '-.';
x1.Label = sprintf('Max Power %.3f db',maxx);
x1.LabelHorizontalAlignment = 'left';
x1.LabelVerticalAlignment = 'top';
x2 = yline(minn);
x2.LineWidth = 1.5;
x2.FontSize = 15;
x2.Color = 'black';
x2.LineStyle = '-.';
x2.Label = sprintf('Min Power %.3f db',minn);
x2.LabelHorizontalAlignment = 'left';
x2.LabelVerticalAlignment = 'bottom';
% legend('power','syn_temp','up_temp','down_temp')
grid minor;

figure;
hold on;
% plot(x,y1,'k-.', 'LineWidth', 2.5);hold on;
plot(x,freq_temp,'r-', 'LineWidth', 2);hold on;
plot(x,up_temp, 'g--', 'LineWidth', 1.5);hold on;
plot(x,down_temp, 'b:', 'LineWidth', 1);

temp_min = min([min(freq_temp) min(down_temp) min(up_temp)]);
temp_max = max([max(freq_temp) max(down_temp) max(up_temp)]);
temp     = temp_max - temp_min;

xlabel('Time (hour)','FontSize',15);ylabel('Power (dB)','FontSize',15);
title(sprintf('TEMP'),'FontSize',15);
minn = min(temp_min);maxx=max(temp_max);
x1 = yline(maxx);
x1.LineWidth = 1.5;
x1.FontSize = 15;
x1.Color = 'black';
x1.LineStyle = '-.';
x1.Label = sprintf('Max Power %.3f db',maxx);
x1.LabelHorizontalAlignment = 'left';
x1.LabelVerticalAlignment = 'top';
x2 = yline(minn);
x2.LineWidth = 1.5;
x2.FontSize = 15;
x2.Color = 'black';
x2.LineStyle = '-.';
x2.Label = sprintf('Min Power %.3f db',minn);
x2.LabelHorizontalAlignment = 'left';
x2.LabelVerticalAlignment = 'bottom';
legend('syn_temp','up_temp','down_temp')
grid minor;