clc ; clear ; close all;
%%
% Path = 'data\spurious';
Path = 'data\spurious_down';
File = dir(fullfile(Path,'*.mat'));
FileNames = {File.name}';
FilePath  = {File.folder}';
temp = 0;
load_File = strcat(cell2mat(FilePath(end-temp,:)),'\',cell2mat(FileNames(end-temp,:)));
load(load_File);
%% Load Data
% load("data\spurious\20231020_170125_spurious_5G__RS230704002.mat"); % Loc = 9.45
% load("data\spurious_down\20231020_122418_spurious_RS_R_down_5G__RS230704002.mat"); % Loc = 9.45
% load("data\spurious\20231022_183642_spurious_RS_5G__RS230704003.mat"); % Loc = 9.65
% load("data\spurious\20230703_202230_spurious_2G模块_9845.mat"); % Loc = 9.85

%%
% spurious = spurious - 5;
% spurious(1) = -87.8628 + 27.5713 - 5;
% spurious(2) = -86.8605 + 27.8032 - 5;

% fre_meas = linspace(240,2240,11);
% spurious = [-1 -8 -6 2 -3 -2 -7 -1 -1 -4 -1];

figure('Position',[1 1 1920 1002],Color=[1 1 1]);
plot(fre_meas/1e6,spurious);grid minor;
xlabel('Freq (MHz)',FontSize=15);ylabel('Spurious (dBc)',FontSize=15);
axis ([min(fre_meas/1e6)-40 max(fre_meas/1e6)+60 min(spurious)-1.4 max(spurious)+1.4]);
minn = min(spurious);
maxx = max(spurious);
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
%%
% fre_set = linspace(76000,81000,1001);
% plot(fre_set,trace(1,:));
% plot(fre_set,trace(2,:));
% plot(fre_set,trace(3,:));
% plot(fre_set,trace(4,:));