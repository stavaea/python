clc ; clear ; close all;
%%
Path = 'data\spurious';
File = dir(fullfile(Path,'*.mat'));
FileNames = {File.name}';
FilePath  = {File.folder}';
temp = 0;
load_File = strcat(cell2mat(FilePath(end-temp,:)),'\',cell2mat(FileNames(end-temp,:)));
load(load_File);
%% Load Data
% load("data\spurious\20230703_200760_spurious_2G模块_9470.mat"); % Loc = 9.45
% load("data\spurious\20230703_201326_spurious_2G模块_9650.mat"); % Loc = 9.65
% load("data\spurious\20230703_202230_spurious_2G模块_9845.mat"); % Loc = 9.85

%%
figure('Position',[-1919 1 1920 1002],Color=[1 1 1]);
plot(fre_meas/1e6,spurious);grid minor;
xlabel('Freq (MHz)',FontSize=15);ylabel('Spurious (dBc)',FontSize=15);
% title(sprintf('Flatness : %3.3f dB',range(gain)));
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