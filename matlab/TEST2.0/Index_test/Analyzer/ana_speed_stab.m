clc ; clear ; close all;
%% 文件路径
DataFile_path = '..\Data\RTS7681D_50\SN2402006\20240322_160640_速度稳定性指标测试';
% DataFile_path = 'D:\work\bit\20240305_160339_距离指标测试';
%% 加载数据
data = load(DataFile_path);
%% 数据加载及处理
Fc = data.fre_set'*1e6;
% 速度            单位：km/h
speed    = data.speed*3.6;
% 理论计算Doppler 单位：Hz
Doppler  = data.fd * 1e6;
% 采集频率        单位：Hz
coll_fre = data.fre_meas;
% Doppler误差计算 单位：Hz
Doppler_error  = coll_fre - Fc - Doppler;
% 速度误差计算    单位：km/h
% V_error = (C*fd)/(2*fc) * 3.6
V_error  = (299792458.*Doppler_error) ./ (2.*77e9) .* 3.6;

time = data.time / 3600;
x =time;
y = V_error;
plot(x,y)

xlabel('time (hour)','FontSize',15);ylabel('Speed (km/h)','FontSize',15);
title(sprintf('Speed Jitter Range :%.3f km/h',range(y)),'FontSize',15);
minn = min(y);maxx=max(y);
x1 = yline(maxx);
x1.LineWidth = 1.5;
x1.FontSize = 15;
x1.Color = 'black';
x1.LineStyle = '-.';
x1.Label = sprintf('Max Speed Error %.5f km/h',maxx);
x1.LabelHorizontalAlignment = 'left';
x1.LabelVerticalAlignment = 'top';
x2 = yline(minn);
x2.LineWidth = 1.5;
x2.FontSize = 15;
x2.Color = 'black';
x2.LineStyle = '-.';
x2.Label = sprintf('Min Speed Error %.5f km/h',minn);
x2.LabelHorizontalAlignment = 'left';
x2.LabelVerticalAlignment = 'bottom';