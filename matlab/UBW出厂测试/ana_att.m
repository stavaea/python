clc ; clear ; close all

data = load("20231217_125658_ubw衰减指标测试.mat");

att1 = 0:0.25:30;
att2 = data.att;
att  = [att1(1:end-1) att2+att1(end)];

power = data.amp_meas(5,:);
power = power - power(1);
power = [power(1:120) power(122:end)];

fig = figure;
fig.Color = [1 1 1];
fig.Position = [1 1 1920 1002];

att_error = power + att;

plot_x = att(121:161);
plot_y = att_error(121:161);
plot_y = plot_y - plot_y(1);
minn = min(plot_y);
maxx = max(plot_y);
plot(plot_x,plot_y,'LineWidth',1.5);
t = 0.02;
axis([min(plot_x) max(plot_x) minn-t maxx+t]);
text(max(plot_x)*0.92,maxx,sprintf(['RCS Jitter Range    ：%.5f dB\n' ...
                                       'Standard Deviation ：%.5f dB'], ...
                                   range(plot_y),std(plot_y)),'FontSize',15);
grid on ; hold on;

xlabel('Target RCS (dBsm)','FontSize',15);ylabel('RCS  (dBsm)','FontSize',15);

x1 = yline(maxx);
x1.LineWidth = 1.5;
x1.FontSize = 15;
x1.Color = 'black';
x1.LineStyle = '-.';
x1.Label = sprintf('Max RCS Error %.5f dBsm',maxx);
x1.LabelHorizontalAlignment = 'left';
x1.LabelVerticalAlignment = 'top';
x2 = yline(minn);
x2.LineWidth = 1.5;
x2.FontSize = 15;
x2.Color = 'black';
x2.LineStyle = '-.';
x2.Label = sprintf('Min RCS Error %.5f dBsm',minn);
x2.LabelHorizontalAlignment = 'left';
x2.LabelVerticalAlignment = 'bottom';
copygraphics(fig);


