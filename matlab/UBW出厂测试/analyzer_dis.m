clc; clear all; close all;

data = load('20231217_145804_ubw距离指标测试.mat');

x=data.x;
y=(data.error)/1e3;  %y1,error
plot(x, y,'.-');  %'LineWidth',1.5,
xlabel('Set Dis (m)','FontSize',10);
ylabel('Speed Dis Error (m)','FontSize',10);
title(sprintf('Dis Error Jitter Range:%3.3f m',range(y)));

% figure;
% plotx = data.x;ploty = data.error;
% plot(plotx, ploty);

minn = min(y);
maxx = max(y);
grid on ; hold on;


x1 = yline(maxx);
x1.LineWidth = 1.5;
x1.FontSize = 10;
x1.Color = 'black';
x1.LineStyle = '-.';
x1.Label = sprintf('Max Dis Error %.5f m',maxx);
x1.LabelHorizontalAlignment = 'left';
x1.LabelVerticalAlignment = 'top';
x2 = yline(minn);
x2.LineWidth = 1.5;
x2.FontSize = 10;
x2.Color = 'black';
x2.LineStyle = '-.';
x2.Label = sprintf('Min Dis Error %.5f m',minn);
x2.LabelHorizontalAlignment = 'left';
x2.LabelVerticalAlignment = 'bottom';