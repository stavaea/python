clc;close all;clear


Path = '..\Data\RS_E_Rf_202304001\20241010_090706_RCS指标测试_8100';
data = load(Path);
% 波段：E、V、K、X波段
waveband = 'E';
% 模块：Rf(射频模块)、Rm（调理模块）、Fcrm（二次变频与调理模块）
module       = 2;
% 模块类型：Down（下变频模块）、Close（闭环）、Open（开环）、Up(上变频模块)
module_type  = 'Down';


switch (waveband)
	case 'E'
		waveband_judge = 1;
	case 'V'
		waveband_judge = 2;
	case 'X'
		waveband_judge = 3;
	case 'K'
		waveband_judge = 4;
end

switch (module)
	case 'Rf'
		module_judge = 1;
	case 'Fcrm'
		module_judge = 2;
	case 'Rm'
		module_judge = 3;
end

switch (module_type)
	case 'Down'
		module_type_judge = 1;
	case 'Up'
		module_type_judge = 2;
	case 'Close'
		module_type_judge = 3;
	case 'Open'
		module_type_judge = 3;
end



if module_judge == 2 || module_judge == 3
    x = data.fre_set;
    y = data.trace - data.amp_set + 5;
    plot_fcrm(x,y)

elseif module_judge == 1
    if module_type_judge == 2
        x = data.fre_set;
        y = data.amp_meas - data.amp_set + 30 + 18 + 5;
        plot_up(x,y)

    elseif module_type_judge == 1
        x = data.fre_set;
        y = data.trace - 15 + 30  + 5;
        plot_down(x,y)
    end
end



function plot_fcrm(x,y)
figure(Color=[1 1 1]);
plot(x,y);grid minor;
xlabel('Freq (MHz)',FontSize=15);ylabel('Gain (dB)',FontSize=15);
% title(sprintf('Flatness : %3.3f dB',range(gain)));
axis ([min(x)-40 max(x)+60 min(y)-1 max(y)+1]);
minn = min(y);
maxx = max(y);
x1 = yline(maxx);
x1.LineWidth = 1.5;
x1.FontSize = 15;
x1.Color = 'black';
x1.LineStyle = '-.';
x1.Label = sprintf('Max Gain %.3f dB',maxx);
x1.LabelHorizontalAlignment = 'left';
x1.LabelVerticalAlignment = 'top';
x2 = yline(minn);
x2.LineWidth = 1.5;
x2.FontSize = 15;
x2.Color = 'black';
x2.LineStyle = '-.';
x2.Label = sprintf('Min Gain %.3f dB',minn);
x2.LabelHorizontalAlignment = 'left';
x2.LabelVerticalAlignment = 'bottom';
end

function plot_up(x,y)
figure('Position',[1 1 1920 1002],Color=[1 1 1]);
plot(x,y);grid minor;
xlabel('Freq (MHz)',FontSize=15);ylabel('Gain (dB)',FontSize=15);
temp = 0.5;
axis ([min(x)-40 max(x)+60 min(y)-temp max(y)+temp]);
minn = min(y);
maxx = max(y);
x1 = yline(maxx);
x1.LineWidth = 1.5;
x1.FontSize = 15;
x1.Color = 'black';
x1.LineStyle = '-.';
x1.Label = sprintf('Max Gain %.3f dB',maxx);
x1.LabelHorizontalAlignment = 'left';
x1.LabelVerticalAlignment = 'top';
x2 = yline(minn);
x2.LineWidth = 1.5;
x2.FontSize = 15;
x2.Color = 'black';
x2.LineStyle = '-.';
x2.Label = sprintf('Min Gain %.3f dB',minn);
x2.LabelHorizontalAlignment = 'left';
x2.LabelVerticalAlignment = 'bottom';
end


function plot_down(x,y)
figure('Position',[1 1 1920 1002],Color=[1 1 1]);
plot(x,y);grid minor;
xlabel('Freq (MHz)',FontSize=15);ylabel('Gain (dB)',FontSize=15);
temp = 0.5;
axis ([min(x)-40 max(x)+60 min(y)-temp max(y)+temp]);
minn = min(y);
maxx = max(y);
x1 = yline(maxx);
x1.LineWidth = 1.5;
x1.FontSize = 15;
x1.Color = 'black';
x1.LineStyle = '-.';
x1.Label = sprintf('Max Gain %.3f dB',maxx);
x1.LabelHorizontalAlignment = 'left';
x1.LabelVerticalAlignment = 'top';
x2 = yline(minn);
x2.LineWidth = 1.5;
x2.FontSize = 15;
x2.Color = 'black';
x2.LineStyle = '-.';
x2.Label = sprintf('Min Gain %.3f dB',minn);
x2.LabelHorizontalAlignment = 'left';
x2.LabelVerticalAlignment = 'bottom';
end

