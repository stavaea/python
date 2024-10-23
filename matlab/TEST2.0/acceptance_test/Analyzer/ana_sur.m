clc;close all;clear


Path = '..\Data\RS_E_Rf_202304001\20241010_090706_RCS指标测试_8100';
data = load(Path);
% 波段：E、V、K、X波段
waveband = 'E';
% 模块：Rf(射频模块)、Rm（调理模块）、Fcrm（二次变频与调理模块）
module       = 2;
% 模块类型：Down（下变频模块）、Close（闭环）、Open（开环）、Up(上变频模块)
module_type  = 'Down';


x = data.fre_set;
y = spurious;
plot_sur(x,y)

function plot_sur(x,y)
figure('Position',[1 1 1920 1002],Color=[1 1 1]);
plot(x,y);grid minor;
xlabel('Freq (MHz)',FontSize=15);ylabel('Spurious (dBc)',FontSize=15);
% title(sprintf('Flatness : %3.3f dB',range(gain)));
axis ([min(x)-40 max(x)+60 min(y)-1.4 max(y)+1.4]);
minn = min(y);
maxx = max(y);
x1 = yline(maxx);
x1.LineWidth = 1.5;
x1.FontSize = 15;
x1.Color = 'black';
x1.LineStyle = '-.';
x1.Label = sprintf('Max Spurious %.3f dB',maxx);
x1.LabelHorizontalAlignment = 'left';
x1.LabelVerticalAlignment = 'top';
x2 = yline(minn);
x2.LineWidth = 1.5;
x2.FontSize = 15;
x2.Color = 'black';
x2.LineStyle = '-.';
x2.Label = sprintf('Min Spurious %.3f dB',minn);
x2.LabelHorizontalAlignment = 'left';
x2.LabelVerticalAlignment = 'bottom';
end