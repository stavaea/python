clc ; clear ; close all;


%% Load Data& Program
temp = 1; %%绘制 10K 100K 1M 相噪
% temp = 3; %%绘制 100Hz 1KHz 相噪
File = "data\Phasenoise\Phasenoise.mat";
% File = "data\Phasenoise\20240219_111625_006_Fix_out1.mat";
% File = "data\Phasenoise\20231030_142712_PZ2G2309002_NoFix_out1.mat";
% File = "data\Phasenoise\20231030_143034_PZ2G2309002_Fix_out1.mat";
% File = "data\Phasenoise\20231030_143316_PZ2G2309002_Fix_out2.mat";

%% Program
load(File);
x = phasenoise_trace_x;
y = phasenoise_trace  ;

%% 寻找100Hz 、 1KHz 、 10KHz 、 100KHz 、 1MHz的相噪
phase_data(1) = phasenoise_trace(11 );
phase_data(2) = phasenoise_trace(201);
phase_data(3) = phasenoise_trace(191);
phase_data(4) = phasenoise_trace(371);
phase_data(5) = phasenoise_trace(281);
fprintf('%3.3fdBc/Hz@100Hz\n%3.3fdBc/Hz@1KHz\n%3.3fdBc/Hz@100KHz\n%3.3fdBc/Hz@1MHz\n', ...
    phase_data(1),phase_data(2),phase_data(3),phase_data(4));
fprintf(['可变频综Lo_Out1相噪为 %3.3fdBc/Hz@100Hz ' ...
    ',%3.3fdBc/Hz@1KHz,%3.3fdBc/Hz@10KHz,%3.3fdBc' ...
    '/Hz@100KHz,%3.3fdBc/Hz@1MHz。\n'],phase_data(1), ...
    phase_data(2),phase_data(3),phase_data(5),phase_data(4));
fprintf(['固定频综Lo_Out1相噪为 %3.3fdBc/Hz@100Hz ' ...
    ',%3.3fdBc/Hz@1KHz,%3.3fdBc/Hz@10KHz,%3.3fdBc' ...
    '/Hz@100KHz,%3.3fdBc/Hz@1MHz。\n'],phase_data(1), ...
    phase_data(2),phase_data(3),phase_data(5),phase_data(4));
fprintf(['可变频综Lo_Out2相噪为 %3.3fdBc/Hz@100Hz ' ...
    ',%3.3fdBc/Hz@1KHz,%3.3fdBc/Hz@10KHz,%3.3fdBc' ...
    '/Hz@100KHz,%3.3fdBc/Hz@1MHz。\n'],phase_data(1), ...
    phase_data(2),phase_data(3),phase_data(5),phase_data(4));
fprintf(['固定频综Lo_Out2相噪为 %3.3fdBc/Hz@100Hz ' ...
    ',%3.3fdBc/Hz@1KHz,%3.3fdBc/Hz@10KHz,%3.3fdBc' ...
    '/Hz@100KHz,%3.3fdBc/Hz@1MHz。\n'],phase_data(1), ...
    phase_data(2),phase_data(3),phase_data(5),phase_data(4));
% disp(t)
% 数据删减，删除0~90Hz的相噪

x = x (11:end-90*temp)/1000;
y = y (11:end-90*temp);


% leg    =  '100Hz~10MHz Phase Noise';

%% Plot
fig          = figure;
% fig.Position = [-1919 1 1920 1002];
fig.Color    = [1 1 1];

p            = plot(x,y);
p.Color      = 'b';
p.LineWidth  = 1;
p.LineStyle  = '-';
if (temp == 1)
    datatip(p,x(181),y(181));
    datatip(p,x(271),y(271));
    datatip(p,x(361),y(361));
else
    datatip(p,x(1  ),y(1  ));
    datatip(p,x(91 ),y(91 ));
    datatip(p,x(181),y(181));
end
grid 'minor';
xlabel('Frequency (KHz)',FontSize=20);
ylabel('Phase Noise (dBc/Hz)',FontSize=20);
title('Phase Noise',FontSize=20);
% l            = legend(p,leg);
% l.Box        = 'off';
%%
copygraphics(gcf);