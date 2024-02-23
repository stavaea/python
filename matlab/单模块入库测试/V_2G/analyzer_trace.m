clc ; clear ; close all;

%%
% Path = 'data\trace';
Path = 'data\trace_up';
% Path = 'data\trace_down';
File = dir(fullfile(Path,'*.mat'));
FileNames = {File.name}';
FilePath  = {File.folder}';
temp = 0;
load_File = strcat(cell2mat(FilePath(end-temp,:)),'\',cell2mat(FileNames(end-temp,:)));
load(load_File);
inst = load("data\trace_sig_spec");
amp_inst_sig_spec = inst.trace;
inst = load("data\beipin.mat");
amp_inst_beipin = inst.beipinqi;
inst = load("data\hunpinqi.mat");
amp_inst_hunpin = inst.hunpinqi;
%% Load Data
% load("data\trace\20231020_163055_trace_RS_R_5G_RS230704002.mat"); % Loc = 9.45
% load("data\trace_down\20231020_121253_trace_RS_R_down_5G_RS230704002.mat"); % Loc = 9.45
% load("data\trace_up\20231020_151757_trace_RS_5G_gain_trace_RS230704002.mat"); % Loc = 9.45


%%
trace = amp_meas(1:20:end) - amp_inst_hunpin - amp_inst_sig_spec(1:20:end); % shangbianpin
% trace  = trace(1:20:end) -  amp_inst_sig_spec(1:20:end) - amp_inst_beipin; % xiabinpin
fre_set = fre_set(1:20:end);

% trace = trace - amp_inst_sig_spec;  % 自闭环
% figure('Position',[1 1 1920 1002],Color=[1 1 1]);
figure(Color=[1 1 1]);
plot(fre_set,trace);grid minor;
xlabel('Freq (MHz)',FontSize=15);ylabel('Power (dB)',FontSize=15);
title(sprintf('Flatness : %3.3f dB',range(trace)-3.6),FontSize=15);
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