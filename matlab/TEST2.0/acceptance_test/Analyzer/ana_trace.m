clc;close all;clear


Path = '..\Data\RS_E_Rf_202304001\20241010_090706_RCS指标测试_8100';
data = load(Path);
% 波段：E、V、K、X波段
waveband = 'E';
% 模块：Rf(射频模块)、Rm（调理模块）、Fcrm（二次变频与调理模块）
module       = 2;
% 模块类型：Down（下变频模块）、Close（闭环）、Open（开环）、Up(上变频模块)
module_type  = 'Down';

inst = load("data\trace_hui.mat");
amp_inst_sig_spec = inst.trace;
inst = load("data\beipin.mat");
amp_inst_beipin = inst.beipinqi;
inst = load("data\hunpinqi.mat");
amp_inst_hunpin = inst.hunpinqi;

% 波段：E、V、K、X波段
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

% 模块：Rf(射频模块)、Rm（调理模块）、Fcrm（二次变频与调理模块）
switch (module)
	case 'Rf'
		module_judge = 1;
	case 'Fcrm'
		module_judge = 2;
	case 'Rm'
		module_judge = 3;
end

% 模块类型：Down（下变频模块）、Close（闭环）、Open（开环）、Up(上变频模块)
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
    y = data.trace - amp_inst_sig_spec;
    plot_fcrm(x,y)
elseif module_judge == 1
    if module_type_judge == 1
        x = data.fre_set;
        y = data.trace - amp_inst_sig_spec - amp_inst_beipin;
    elseif module_type_judge == 2
        x = data.fre_set(1:2:end);
        y = data.amp_meas - amp_inst_hunpin - amp_inst_sig_spec;
    end
end
plot_rf(x,y)



function plot_rf(x,y)
figure(Color=[1 1 1]);
plot(x,y);grid minor;
xlabel('Freq (MHz)',FontSize=15);ylabel('Power (dB)',FontSize=15);
title(sprintf('Flatness : %3.3f dB',range(trace)),FontSize=15);
axis ([min(x)-1 max(x)+1 min(y)-0.3 max(y)+0.3]);
minn = min(y);
maxx = max(y);
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
end


function plot_fcrm(x,y)
figure(Color=[1 1 1]);
plot(x,y);grid minor;
xlabel('Freq (MHz)',FontSize=15);ylabel('Power (dB)',FontSize=15);
title(sprintf('Flatness : %3.3f dB',range(trace)),FontSize=15);
axis ([min(x)-1 max(x)+1 min(y)-0.3 max(y)+0.3]);
minn = min(y);
maxx = max(y);
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
end