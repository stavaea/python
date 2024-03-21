% 程序用于分析RTS速度指标测试数据
clc ; clear ; close all;
%% 文件路径
DataFile_path = '..\Data\RTS7681D_50\SN_wz\20240319_170707_速度指标测试';
%% 加载数据
data = load(DataFile_path);
%% 数据加载及处理
% 采集Doppler频率
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
V_error  = (299792458.*Doppler_error) ./ (2.*Fc) .* 3.6;
%% 数据拆分
% 速度范围数据
speed_range        = [speed(1:20)   speed(71)   speed(122:end)  ];
speed_range_error  = [V_error(:,1:20) V_error(:,71) V_error(:,122:end)];
% 速度精度数据
speed_setp         = speed(21:121);
speed_setp_error   = V_error(:,21:121);
%% 画图
for i = 1:length(Fc)
    speed_plot(speed_range,speed_range_error(i,:),1,0.45);
    pause_win(Fc(i),'速度范围');
    speed_plot(speed_setp,speed_setp_error(i,:),1,0.45);
    pause_win(Fc(i),'速度精度');
end
%% 画图函数
function speed_plot(plot_x,plot_y,flag_xtick,text_x)
fig = figure;
fig.Color = [1 1 1];
fig.Position = [1 1 1920 1002];

minn = min(plot_y);
maxx = max(plot_y);

span_x = range(plot_x)/50;
span_y = range(plot_y)/15;

plot(plot_x,plot_y,'LineWidth',1.5);
if flag_xtick
    set(gca,'XTick',[-720:36:720]);
end
axis([min(plot_x)-span_x max(plot_x)+span_x min(plot_y)-span_y max(plot_y)+span_y])
text(max(plot_x)*text_x,maxx,sprintf(['Speed Jitter Range ：%.5f km/h\n' ...
    'Standard Deviation ：%.5f km/h'], ...
    range(plot_y),std(plot_y)),'FontSize',15);
grid on ; hold on;

xlabel('Target Speed (km/h)','FontSize',15);ylabel('Speed Error (km/h)','FontSize',15);

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
copygraphics(fig);
end
%% 窗口函数
function pause_win(freq,msg)
    msg = strcat(sprintf('%3.3fGHz',freq/1e9),msg,'绘图完成，点击确定继续');
    wait = msgbox(msg,'提示');
    uiwait(wait);
end
