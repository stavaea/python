load('RTS7681D_20_SN2402006_幅频修正数据.mat')
% load('RTS7681D_50_SN_06_幅频修正数据.mat')

x = linspace(76000,81000,20001);

plot(x,trace);


xlabel('Freq (GHz)',FontSize=15);ylabel('Power (dB)',FontSize=15);
title(sprintf('Flatness : %3.3f dB',range(trace)),FontSize=15);
% axis ([min(fre_set)-1 max(fre_set)+1 min(trace)-0.3 max(trace)+0.3]);
minn = min(trace);
maxx = max(trace);
x1 = yline(maxx);
x1.LineWidth = 1.5;
x1.FontSize = 15;
x1.Color = 'black';
x1.LineStyle = '-.';
x1.Label = sprintf('Max Power %.3f dB',maxx);
x1.LabelHorizontalAlignment = 'left';
x1.LabelVerticalAlignment = 'top';
x2 = yline(minn);
x2.LineWidth = 1.5;
x2.FontSize = 15;
x2.Color = 'black';
x2.LineStyle = '-.';
x2.Label = sprintf('Min Power %.3f dB',minn);
x2.LabelHorizontalAlignment = 'left';
x2.LabelVerticalAlignment = 'bottom';