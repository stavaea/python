% 程序用于分析RTS RCS指标测试数据
clc ; clear ; close all;
%% 文件路径
DataFile_path1 = '..\Data\RTS7681D_20\SN2402003\20240306_091626_RCS指标测试_8100'; % 频率1数据
DataFile_path2 = '..\Data\RTS7681D_20\SN2402003\20240306_092107_RCS指标测试_8600'; % 频率2数据
%% 加载数据
data1 = load(DataFile_path1);
data2 = load(DataFile_path2);
%% 数据加载及处理
% 设置衰减 单位：dB
set_att1 = data1.Att;
set_att2 = data2.Att;
% 采集功率 单位：dBm
coll_pwoer1 = data1.amp_meas;
coll_pwoer1 = coll_pwoer1 - coll_pwoer1(1);
coll_pwoer2 = data2.amp_meas;
coll_pwoer2 = coll_pwoer2 - coll_pwoer2(1);
% 衰减误差 单位：dB
error_att1 = coll_pwoer1 + set_att1;
error_att2 = coll_pwoer2 + set_att2;
%% 数据拆分
% 频率1
% RCS范围数据
att_range1        = [set_att1(1) set_att1(10:19) set_att1(28:end)  ];
att_range_error1  = [error_att1(1) error_att1(10:19)  error_att1(28:end)];
% RCS精度数据
att_setp1_1         = set_att1(1:9);
att_setp_error1_1   = error_att1(1:9);
att_setp1_2         = set_att1(19:27);
att_setp_error1_2   = error_att1(19:27);
% 频率2
% RCS范围数据
att_range2        = [set_att2(1) set_att2(10:19) set_att2(28:end)  ];
att_range_error2  = [error_att2(1) error_att2(10:19)  error_att2(28:end)];
% RCS精度数据
att_setp2_1         = set_att2(1:9);
att_setp_error2_1   = error_att2(1:9);
att_setp2_2         = set_att2(19:27);
att_setp_error2_2   = error_att2(19:27);
%% 画图
distance_plot(att_range1,att_range_error1,1,0.75);% 后续需要更改
pause_win('频率1 0~90 RCS范围');
distance_plot(att_range2,att_range_error2,1,0.75);% 后续需要更改
pause_win('频率2 0~90 RCS范围');
distance_plot(att_setp1_1,att_setp_error1_1,0,0.7);% 后续需要更改
pause_win('频率1 0~1dB RCS精度');
distance_plot(att_setp2_1,att_setp_error2_1,0,0.7);% 后续需要更改
pause_win('频率2 0~1dB RCS精度');
distance_plot(att_setp1_2,att_setp_error1_2,0,0.994);% 后续需要更改
pause_win('频率1 50~51dB RCS精度');
distance_plot(att_setp2_2,att_setp_error2_2,0,0.994);% 后续需要更改

%% 画图函数
function distance_plot(plot_x,plot_y,flag_xtick,text_x)
fig = figure;
fig.Color = [1 1 1];
fig.Position = [1 1 1920 1002];

minn = min(plot_y);
maxx = max(plot_y);

span_x = range(plot_x)/50;
span_y = range(plot_y)/15;

plot(plot_x,plot_y,'LineWidth',1.5);
% if flag_xtick
%     set(gca,'XTick',[-720:36:720]);
% end
axis([min(plot_x)-span_x max(plot_x)+span_x min(plot_y)-span_y max(plot_y)+span_y])
text(max(plot_x)*text_x,maxx,sprintf(['RCS Jitter Range ：%.3f dBsm\n' ...
    'Standard Deviation ：%.3f dBsm'], ...
    range(plot_y),std(plot_y)),'FontSize',15);% 后续需要更改
grid on ; hold on;

xlabel('Target RCS (dBsm)','FontSize',15);ylabel('RCS Error (dBsm)','FontSize',15);

x1 = yline(maxx);
x1.LineWidth = 1.5;
x1.FontSize = 15;
x1.Color = 'black';
x1.LineStyle = '-.';
x1.Label = sprintf('Max RCS Error %.3f dBsm',maxx);
x1.LabelHorizontalAlignment = 'left';
x1.LabelVerticalAlignment = 'top';
x2 = yline(minn);
x2.LineWidth = 1.5;
x2.FontSize = 15;
x2.Color = 'black';
x2.LineStyle = '-.';
x2.Label = sprintf('Min RCS Error %.3f dBsm',minn);
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
