clc ; clear ; close all;

%%
Path = 'data\trace';
File = dir(fullfile(Path,'*.mat'));
FileNames = {File.name}';
FilePath  = {File.folder}';
temp = 0;
load_File = strcat(cell2mat(FilePath(end-temp,:)),'\',cell2mat(FileNames(end-temp,:)));
load(load_File);
inst = load("data\trace_sig.mat");
amp_inst_sig_spec = inst.trace;
inst = load("data\beipin.mat");
amp_inst_beipin = inst.beipinqi;
inst = load("data\hunpinqi.mat");
amp_inst_hunpin = inst.hunpinqi;
%% Load Data
% load("data\trace\20230613_234353_trace_2G模块.mat"); % Loc = 9.45
% load("data\trace\20230614_000044_trace_2G模块.mat"); % Loc = 9.65
% load("data\trace\20230614_001012_trace_2G模块.mat"); % Loc = 9.85
% load("data\trace\20230614_110909_trace_2G模块.mat"); % Loc = 9.47
% load("data\trace\20230614_112034_trace_2G模块.mat"); % Loc = 9.67
% load("data\trace\20230614_113915_trace_2G模块.mat"); % Loc = 9.87
% load("data\trace\20230704_092150_trace_2G模块_9845.mat"); % Loc = 9.87
% load("data\trace\20230704_093940_trace_2G模块_9650.mat"); % Loc = 9.87
% load("data\trace\20230704_102805_trace_2G模块_9470.mat"); % Loc = 9.87
% load("data\trace\20230721_155910_trace_77GHz经济版5G带宽2023004003.mat"); % Loc = 9.87

% trace = amp_meas(1:2:end)- amp_inst_hunpin(1:2:end) - amp_inst_sig_spec(1:2:end); % shangbianpin
trace  = trace(1:2:end) -  amp_inst_sig_spec(1:2:end) - amp_inst_beipin(1:2:end); % xiabinpin
fre_set = fre_set(1:2:end);
% trace = trace - amp_inst_sig_spec;  % 自闭环
%%
figure(Color=[1 1 1]);
plot(fre_set,trace);
xlabel('Freq (MHz)',FontSize=15);ylabel('Power (dB)',FontSize=15);
title(sprintf('Flatness : %3.3f dB',range(trace)),FontSize=15);
axis ([min(fre_set)-1 max(fre_set)+1 min(trace)-0.3 max(trace)+0.3]);
minn = min(trace);
maxx = max(trace);
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