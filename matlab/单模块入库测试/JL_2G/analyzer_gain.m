clc ; clear ; close all;

%%
Path = 'data\trace';
File = dir(fullfile(Path,'*.mat'));
FileNames = {File.name}';
FilePath  = {File.folder}';
temp = 0;
load_File = strcat(cell2mat(FilePath(end-temp,:)),'\',cell2mat(FileNames(end-temp,:)));
data =  load(load_File);
%% Load Data
% data = load("data\gain\20230614_002903_gain_2G模块.mat");
% data = load("data\gain\20230703_192122_gain_2G模块_9845.mat");
% data = load("data\gain\20230703_194119_gain_2G模块_9650.mat");
% data = load("data\gain\20230703_195841_gain_2G模块_9470.mat");
% data = load("data\gain\20230614_103414_gain_2G模块.mat");
% data_down = load("data\gain\20230614_095510_gain_down_2G模块.mat");
% data_down = load("data\gain\20230614_101348_gain_down_2G模块.mat");
% data = load("data\gain\20230721_114757_gain_77GHz经济版5G带宽2023004003.mat");
%% 自闭环增益

% figure(Color=[1 1 1]);
% % data.amp_meas(1:6) = data.amp_meas(7:12);
% gain = data.trace - data.amp_set + 30 + 3;
% plot(data.fre_set,gain);grid minor;
% xlabel('Freq (MHz)',FontSize=15);ylabel('Gain (dB)',FontSize=15);
% % title(sprintf('Flatness : %3.3f dB',range(gain)));
% axis ([min(data.fre_set)-40 max(data.fre_set)+60 min(gain)-1 max(gain)+1]);
% minn = min(gain);
% maxx = max(gain);
% x1 = yline(maxx);
% x1.LineWidth = 1.5;
% x1.FontSize = 15;
% x1.Color = 'black';
% x1.LineStyle = '-.';
% x1.Label = sprintf('Max Gain %.3f dB',maxx);
% x1.LabelHorizontalAlignment = 'left';
% x1.LabelVerticalAlignment = 'top';
% x2 = yline(minn);
% x2.LineWidth = 1.5;
% x2.FontSize = 15;
% x2.Color = 'black';
% x2.LineStyle = '-.';
% x2.Label = sprintf('Min Gain %.3f dB',minn);
% x2.LabelHorizontalAlignment = 'left';
% x2.LabelVerticalAlignment = 'bottom';

%% 下变频增益
% figure('Position',[1 1 1920 1002],Color=[1 1 1]);
% gain = data.trace - 15 + 30  + 5 ; % 30dB固衰 5dB线损 下变频
% plot(data.fre_set,gain);grid minor;
% xlabel('Freq (MHz)',FontSize=15);ylabel('Gain (dB)',FontSize=15);
% temp = 0.5;
% axis ([min(data.fre_set)-40 max(data.fre_set)+60 min(gain)-temp max(gain)+temp]);
% minn = min(gain);
% maxx = max(gain);
% x1 = yline(maxx);
% x1.LineWidth = 1.5;
% x1.FontSize = 15;
% x1.Color = 'black';
% x1.LineStyle = '-.';
% x1.Label = sprintf('Max Gain %.3f dB',maxx);
% x1.LabelHorizontalAlignment = 'left';
% x1.LabelVerticalAlignment = 'top';
% x2 = yline(minn);
% x2.LineWidth = 1.5;
% x2.FontSize = 15;
% x2.Color = 'black';
% x2.LineStyle = '-.';
% x2.Label = sprintf('Min Gain %.3f dB',minn);
% x2.LabelHorizontalAlignment = 'left';
% x2.LabelVerticalAlignment = 'bottom';

% % 上变频增益
% figure('Position',[1 1 1920 1002],Color=[1 1 1]);
% % gain = data.amp_meas - data.amp_set + 30  + 5; % 30dB固衰 5dB线损 自闭环
% gain = data.amp_meas - data.amp_set + 30 + 18 + 5 ; % 30dB固衰 5dB线损 上变频
% plot(data.fre_set,gain);grid minor;
% xlabel('Freq (MHz)',FontSize=15);ylabel('Gain (dB)',FontSize=15);
% temp = 0.5;
% axis ([min(data.fre_set)-40 max(data.fre_set)+60 min(gain)-temp max(gain)+temp]);
% minn = min(gain);
% maxx = max(gain);
% x1 = yline(maxx);
% x1.LineWidth = 1.5;
% x1.FontSize = 15;
% x1.Color = 'black';
% x1.LineStyle = '-.';
% x1.Label = sprintf('Max Gain %.3f dB',maxx);
% x1.LabelHorizontalAlignment = 'left';
% x1.LabelVerticalAlignment = 'top';
% x2 = yline(minn);
% x2.LineWidth = 1.5;
% x2.FontSize = 15;
% x2.Color = 'black';
% x2.LineStyle = '-.';
% x2.Label = sprintf('Min Gain %.3f dB',minn);
% x2.LabelHorizontalAlignment = 'left';
% x2.LabelVerticalAlignment = 'bottom';

% 自闭环
%
figure('Position',[1 1 1920 1002],Color=[1 1 1]);
gain = data.trace - data.amp_set + 30  + 5; % 30dB固衰 5dB线损 自闭环
plot(data.fre_set,gain);grid minor;
xlabel('Freq (MHz)',FontSize=15);ylabel('Gain (dB)',FontSize=15);
temp = 0.5;
axis ([min(data.fre_set)-40 max(data.fre_set)+60 min(gain)-temp max(gain)+temp]);
minn = min(gain);
maxx = max(gain);
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

%% 下变频增益
%{
figure(Color=[1 1 1]);
% data_down.amp_meas(1:6) = data_down.amp_meas(7:12);
gain_down = data_down.amp_meas + 45+2;
plot(data.fre_set,gain_down);grid minor;
xlabel('Freq (MHz)',FontSize=15);ylabel('Gain (dB)',FontSize=15);
% title(sprintf('Flatness : %3.3f dB',range(gain)));
axis ([min(data.fre_set)-40 max(data.fre_set)+60 min(gain_down)-1 max(gain_down)+1]);
minn = min(gain_down);
maxx = max(gain_down);
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
%}

%% 上变频增益
%{
gain_up = gain - gain_down;
figure(Color=[1 1 1]);
plot(data.fre_set,gain_up);grid minor;
xlabel('Freq (MHz)',FontSize=15);ylabel('Gain (dB)',FontSize=15);
% title(sprintf('Flatness : %3.3f dB',range(gain)));
axis ([min(data.fre_set)-40 max(data.fre_set)+60 min(gain_up)-1 max(gain_up)+1]);
minn = min(gain_up);
maxx = max(gain_up);
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
%}