clc ; clear ; close all;

data = load("20231216_173022_ubw速度指标测试.mat");
fre_set = 2900;

set_speed = data.speed;
coll_fre  = data.fre_meas;

fd = 1 * 2*set_speed*fre_set*1e6/299792458;

fre_speed = fre_set*1e6 + fd;

fre_error = coll_fre - fre_speed;

v_error  = (299792458.*fre_error) / (2*fre_set*1e6);

% plot_x = [set_speed(1:10:1001) set_speed(1002:1800) set_speed(1801:10:2801) set_speed(2802:end)];
% plot_y = [v_error(1:10:1001) v_error(1002:1800) v_error(1801:10:2801) v_error(2802:end)];
plot_x = set_speed(1:10:1001);
plot_y = v_error(1:10:1001);
% plot_x = set_speed(1801:10:2801);
% plot_y = v_error(1801:10:2801);

fig = figure;
fig.Color = [1 1 1];
fig.Position = [-1919 1 1920 1002];

minn = min(plot_y);
maxx = max(plot_y);

span_x = range(plot_x)/50;
span_y = range(plot_y)/15;

plot(plot_x,plot_y,'LineWidth',1.5);
% set(gca,'XTick',[100:50:1500]);
axis([min(plot_x)-span_x max(plot_x)+span_x min(plot_y)-span_y max(plot_y)+span_y])
text(max(plot_x)*0.98,maxx,sprintf(['Speed Jitter Range ：%.5f m/s\n' ...
                                           'Standard Deviation ：%.5f m/s'], ...
                                   range(plot_y),std(plot_y)),'FontSize',15);
grid on ; hold on;

xlabel('Target Speed (m/s)','FontSize',15);ylabel('Speed Error (m/s)','FontSize',15);

x1 = yline(maxx);
x1.LineWidth = 1.5;
x1.FontSize = 15;
x1.Color = 'black';
x1.LineStyle = '-.';
x1.Label = sprintf('Max Speed Error %.5f m/s',maxx);
x1.LabelHorizontalAlignment = 'left';
x1.LabelVerticalAlignment = 'top';
x2 = yline(minn);
x2.LineWidth = 1.5;
x2.FontSize = 15;
x2.Color = 'black';
x2.LineStyle = '-.';
x2.Label = sprintf('Min Speed Error %.5f m/s',minn);
x2.LabelHorizontalAlignment = 'left';
x2.LabelVerticalAlignment = 'bottom';
copygraphics(fig);
