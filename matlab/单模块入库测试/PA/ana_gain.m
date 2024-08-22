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
% data = load("data\gain_down\20231020_115203_gain_RS_R_down_5G_202309002.mat");

% % 增益
figure('Position',[1 1 1920 1002],Color=[1 1 1]);
gain = data.trace - data.amp_set + 4  ; % 2.5dB线损
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

