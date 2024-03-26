clc ; clear ; close all;
%% 文件路径
DataFile_path = '..\Data\RTS7681D_50\SN2402006\20240323_183540_距离RCS稳定性测试';
% DataFile_path = 'D:\work\bit\20240305_160339_距离指标测试';
%% 加载数据
data = load(DataFile_path);
%% 数据加载及处理
% 设置距离 单位：m
set_distance = data.tar_dis;
% 采集距离 单位：m
coll_distance = data.distance;
% 距离误差 单位：mm
error_distance = coll_distance - set_distance;
error_distance = error_distance * 1e3;

time = data.time / 3600;
power = data.power;
x = time;
y = error_distance;
y1 = power;

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


hold on;
figure;
plot(x,y1);
grid minor;
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
