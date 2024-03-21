% 程序用于分析RTS距离指标测试数据
clc ; clear ; close all;
%% 文件路径
DataFile_path = '..\Data\RTS7681D_50\SN_wz\20240319_164058_距离指标测试';
% DataFile_path = 'D:\work\bit\20240305_160339_距离指标测试';
%% 加载数据
data = load(DataFile_path);
%% 数据加载及处理
% 设置距离 单位：m
set_distance = data.tar_dis;
% 采集距离 单位：m
coll_distance = data.distance;
% 距离误差 单位：mm
error_distance = coll_distance - set_distance;
error_distance = error_distance * 1e3;
%% 数据拆分
% 距离范围数据
distance_range        = [set_distance(1) set_distance(502:601) set_distance(1102:end)  ]; % 后续需要调整
distance_range_error  = [error_distance(1) error_distance(502:601) error_distance(1102:end)]; % 后续需要调整
% 距离精度数据
distance_setp1         = set_distance(1:501); % 后续需要调整
distance_setp_error1   = error_distance(1:501); % 后续需要调整
distance_setp2         = set_distance(601:1101); % 后续需要调整
distance_setp_error2   = error_distance(601:1101); % 后续需要调整
%% 画图
distance_plot(distance_range,distance_range_error,1,0.75);% 后续需要更改
pause_win('0m~500m 距离范围'); % 后续需要更改
distance_plot(distance_setp1,distance_setp_error1,0,0.75);% 后续需要更改
pause_win('0~0.5m 距离精度'); % 后续需要更改
distance_plot(distance_setp2,distance_setp_error2,0,0.998);% 后续需要更改
% pause_win('30~30.5m 距离精度'); % 后续需要更改
%% 画图函数
function distance_plot(plot_x,plot_y,flag_xtick,text_x)
fig = figure;
fig.Color = [1 1 1];
% fig.Position = [-1919 1 1920 1002];

minn = min(plot_y);
maxx = max(plot_y);

span_x = range(plot_x)/50;
span_y = range(plot_y)/15;

plot(plot_x,plot_y,'LineWidth',1.5);
% if flag_xtick
%     set(gca,'XTick',[-720:36:720]);
% end
axis([min(plot_x)-span_x max(plot_x)+span_x min(plot_y)-span_y max(plot_y)+span_y])
text(max(plot_x)*text_x,maxx,sprintf(['Distance Jitter Range ：%.3f mm\n' ...
    'Standard Deviation ：%.3f mm'], ...
    range(plot_y),std(plot_y)),'FontSize',15);% 后续需要更改
grid on ; hold on;

xlabel('Target Distance (mm)','FontSize',15);ylabel('Distance Error (mm)','FontSize',15);

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
end
%% 窗口函数
function pause_win(msg)
msg = strcat(msg,'绘图完成，点击确定继续');
wait = msgbox(msg,'提示');
uiwait(wait);
end
