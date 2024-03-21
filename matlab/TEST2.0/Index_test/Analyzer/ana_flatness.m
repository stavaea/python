% 程序用于分析RTS平坦度指标测试数据
clc ; clear ; close all;
%% 文件路径
DataFile_path = '..\Data\RTS7681FS_50\SN_bk24013\20240318_175648_平坦度指标测试';
%% 加载数据
data = load(DataFile_path);
fs_trace = data.trace(1:4:end);
data.trace = data.trace(:,1:10:end);

%% 数据加载及处理
% 模拟器瞬时带宽 单位：MHz
rts_work_band = 5000;
% 模拟器工作带宽 单位：MHz
rts_band      = 5000;
% 模拟器波段
% 0:K 1:E 2:V
rts_mode      = 1;
%% 画图
if rts_band ==  rts_work_band
    switch rts_mode
        case 0
            x = linspace(23000,25000,rts_band+1);
            y = data.trace(1,:);
        case 1
            x = linspace(76000,81000,rts_band+1);
            y = fs_trace(1,:);
    end
elseif rts_band == 5000 && rts_work_band == 2000
    start_freq = 76000;
    stop_freq  = 81000;
    x = linspace(start_freq,stop_freq,rts_band+1);
    y = [data.trace(1,:) data.trace(2,2:end) data.trace(3,1002:end)];
elseif rts_band == 8000 && rts_work_band == 2000
    start_freq = 58000;
    stop_freq  = 66000;
    x = linspace(start_freq,stop_freq,rts_band+1);
    y = [data.trace(1,:) data.trace(2,2:end) data.trace(3,2:end) data.trace(4,2:end)];
elseif rts_band == 8000 && rts_work_band == 5000
    start_freq = 58000;
    stop_freq  = 66000;
    x = linspace(start_freq,stop_freq,rts_band+1);
    y = [data.trace(1,:) data.trace(2,2002:end)];
end
Flatness_plot(x,y,0,1);
%% 画图函数
function Flatness_plot(plot_x,plot_y,flag_xtick,text_x)
fig = figure;
fig.Color = [1 1 1];
fig.Position = [1 1 1920 1002];

minn = min(plot_y);
maxx = max(plot_y);

span_x = range(plot_x)/50;
span_y = range(plot_y)/15;

plot(plot_x,plot_y,'LineWidth',1.5);

axis([min(plot_x)-span_x max(plot_x)+span_x min(plot_y)-span_y max(plot_y)+span_y])
title(sprintf('Flatness : %3.3f dB',range(plot_y)),"FontSize",15);
grid on ; hold on;

xlabel('Freq (MHz)','FontSize',15);ylabel('RCS (dBsm)','FontSize',15);

x1 = yline(maxx);
x1.LineWidth = 1.5;
x1.FontSize = 15;
x1.Color = 'black';
x1.LineStyle = '-.';
x1.Label = sprintf('Max RCS %.3f dBsm',maxx);
x1.LabelHorizontalAlignment = 'left';
x1.LabelVerticalAlignment = 'top';
x2 = yline(minn);
x2.LineWidth = 1.5;
x2.FontSize = 15;
x2.Color = 'black';
x2.LineStyle = '-.';
x2.Label = sprintf('Min RCS %.3f dBsm',minn);
x2.LabelHorizontalAlignment = 'left';
x2.LabelVerticalAlignment = 'bottom';
copygraphics(fig);
end

