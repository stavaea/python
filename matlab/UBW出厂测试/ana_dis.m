clc ; clear ; close all;
data = load("20231220_171029_ubw距离指标测试.mat");
dis = data.dis;
distance = data.distance;
error = data.error;

fig = figure;
fig.Color = [1 1 1];
fig.Position = [-1919 1 1920 1002];

% plot_x = dis(1:20:end);
% plot_y = error(1:20:end)*1e3;
plot_x = dis(801:981);
plot_y = error(801:981)*1e3;

span_x = range(plot_x)/50;
span_y = range(plot_y)/20;

minn = min(plot_y);
maxx = max(plot_y);


plot(plot_x,plot_y);
axis([min(plot_x)-span_x max(plot_x)+span_x min(plot_y)-span_y max(plot_y)+span_y])
grid minor
xlabel('Set Distance (m)',"FontSize",15);
ylabel('Distance Error (mm)','FontSize',15);
% title(sprintf('Distance Error Range : %3.3f mm',range(error*1e3)),'FontSize',15);
text(max(plot_x)*0.95,maxx+0.25,sprintf(['Distance Jitter Range：%.3f mm\n' ...
                                         'Standard Deviation    ：%.3f mm'], ...
                                        range(plot_y),std(plot_y)),'FontSize',15);
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
copygraphics(fig);


