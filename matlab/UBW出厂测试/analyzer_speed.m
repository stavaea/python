clc; clear all; close all;

data = load('20231216_173022_ubw速度指标测试.mat');
v = data.speed;
fre_set = 2900;
fd = 2*v*fre_set*1e6/299792458;
err = data.fre_meas-(fre_set*1e6+fd);  %fd = 2*fre_set/299792458;
err_v = (299792458*err)/(2*fre_set);  %v=(299792458*fd)/2;
err_v_1 = err_v/1e6;
plot(v, err_v_1,'.-');  %'LineWidth',1.5,
xlabel('Set speed (m/s)','FontSize',10);
ylabel('Speed Error (m/s)','FontSize',10);
title(sprintf('Speed Error Jitter Range:%3.3f m/s',range(err_v_1)));

minn = min(err_v_1);
maxx = max(err_v_1);
grid on ; hold on;
x1 = yline(maxx);
x1.LineWidth = 1.5;
x1.FontSize = 10;
x1.Color = 'black';
x1.LineStyle = '-.';
x1.Label = sprintf('Max Speed Error %.5f m/s',maxx);
x1.LabelHorizontalAlignment = 'left';
x1.LabelVerticalAlignment = 'top';
x2 = yline(minn);
x2.LineWidth = 1.5;
x2.FontSize = 10;
x2.Color = 'black';
x2.LineStyle = '-.';
x2.Label = sprintf('Min Speed Error %.5f m/s',minn);
x2.LabelHorizontalAlignment = 'left';
x2.LabelVerticalAlignment = 'bottom';