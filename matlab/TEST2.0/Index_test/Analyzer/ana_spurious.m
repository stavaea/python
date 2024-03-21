% 程序用于分析RTS杂散指标测试数据
clc ; clear ; close all;
%% 文件路径
DataFile_path = '..\Data\RTS7681D_50\SN_wz\20240319_170027_杂散指标测试';
%% 加载数据
data = load(DataFile_path);
%% 数据加载及处理
% 模拟器瞬时带宽 单位：MHz
rts_work_band = 2000;
% 模拟器工作带宽 单位：MHz
rts_band      = 5000;
% 模拟器波段
% 0:K 1:E 2:V
rts_mode      = 1;
% 多余点数处理
% data.spec_freq_span = 5;
spec_freq_span  = data.spec_freq_span;
%% 画图
if rts_band ==  rts_work_band
    switch rts_mode
        case 0
            start_freq = data.fre_set(1)-spec_freq_span;
            stop_freq  = data.fre_set(end)+spec_freq_span;
            point = stop_freq -  start_freq + 1;
            x = linspace(start_freq,stop_freq,point);
            y = data.spurious(1,:);
        case 1
            start_freq = data.fre_set(1)-spec_freq_span;
            stop_freq  = data.fre_set(end)+spec_freq_span;
            point = stop_freq -  start_freq + 1;
            x = linspace(start_freq,stop_freq,point);
            y = data.spurious(1,:);
    end
elseif rts_band == 5000 && rts_work_band == 2000
    start_freq = 76000 - spec_freq_span;
    stop_freq  = 81000 + spec_freq_span;
    point = stop_freq -  start_freq + 1;
    x = linspace(start_freq,stop_freq,point);
    y = [data.spurious(1,1:end-spec_freq_span) data.spurious(2,2+spec_freq_span:end-spec_freq_span) data.spurious(3,1002+spec_freq_span:end)];
elseif rts_band == 8000 && rts_work_band == 2000
    start_freq = 58000 - spec_freq_span;
    stop_freq  = 66000 + spec_freq_span;
    point = stop_freq -  start_freq + 1;
    x = linspace(start_freq,stop_freq,point);
    y = [data.spurious(1,1:end-spec_freq_span) data.spurious(2,2+spec_freq_span:end-spec_freq_span) data.spurious(3,2+spec_freq_span:end-spec_freq_span) data.spurious(4,2+spec_freq_span:end)];
elseif rts_band == 8000 && rts_work_band == 5000
    start_freq = 58000 - spec_freq_span;
    stop_freq  = 66000 + spec_freq_span;
    point = stop_freq -  start_freq + 1;
    x = linspace(start_freq,stop_freq,point);
    y = [data.spurious(1,1:end-spec_freq_span) data.spurious(2,2002+spec_freq_span:end)];
end
sup_plot(x,y);
%% 画图函数
function sup_plot(plot_x,plot_y)
fig = figure;
fig.Color = [1 1 1];
fig.Position = [1 1 1920 1002];

minn = min(plot_y);
maxx = max(plot_y);

span_x = range(plot_x)/50;
span_y = range(plot_y)/15;

plot(plot_x,plot_y,'LineWidth',1.5);

axis([min(plot_x)-span_x max(plot_x)+span_x min(plot_y)-span_y max(plot_y)+span_y])
grid on ; hold on;

xlabel('Freq (MHz)','FontSize',15);ylabel('Power (dB)','FontSize',15);

end
