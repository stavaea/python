clc ; clear ; close all;
%% 文件路径
Path = 'data\';
File = dir(fullfile(Path,'*.mat'));
FileNames = {File.name}';
FilePath  = {File.folder}';
temp = 1;
load_File = strcat(cell2mat(FilePath(end-temp,:)),'\',cell2mat(FileNames(end-temp,:)));

%% 加载数据
data = load(load_File);
%% 数据加载及处理

fre_set   = data.fre_set;
fre_meas  = data.fre_meas;
amp_set = data.amp_set;
power = data.power;
up_temp = data.up_temp;
down_temp = data.down_temp;
time = data.time;
time = time / 60;


x     = time;
y     = power;


% 画图
figure;
plot(x, y);
grid minor;
xlabel('Time (min)','FontSize',15);ylabel('Coll Power (dB)','FontSize',15);
title(sprintf('Power Jitter Range : %.3f dB',range(y)),'FontSize',15);
minn = min(y);maxx=max(y);
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