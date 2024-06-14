%% 画图函数
function am_freq_corr_plot(plot_x,plot_y,plot_y1)
fig = figure;
% fig.Position = [-1919 1 1920 1002];
fig.Color = [1 1 1];

subplot(121)
plot(plot_x,plot_y);
title(sprintf('修正前平坦度为：%3.3fdB',range(plot_y)),FontSize=15);
xlabel('Freq (MHZ)',FontSize=15);
ylabel('Power (dB)',FontSize=15);
grid minor

subplot(122)
plot(plot_x,plot_y1);
title(sprintf('修正后平坦度为：%3.3fdB',range(plot_y1)),FontSize=15);
xlabel('Freq (MHZ)',FontSize=15);
ylabel('Power (dB)',FontSize=15);
grid minor
end