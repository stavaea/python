clc ; clear ; close all;

Path = 'data\spurious';
File = dir(fullfile(Path,'*.mat'));
FileNames = {File.name}';
FilePath  = {File.folder}';
temp = 0;
load_File = strcat(cell2mat(FilePath(end-temp,:)),'\',cell2mat(FileNames(end-temp,:)));
data = load(load_File);

spec_freq_span = data.spec_freq_span;

start_freq = 7600 - spec_freq_span;
stop_freq  = 9600 + spec_freq_span;
point = stop_freq -  start_freq + 1;
x = linspace(start_freq,stop_freq,point);
y = data.spurious;

figure('Position',[1 1 1920 1002],Color=[1 1 1]);
plot(x,y);grid minor;
xlabel('Freq (MHz)',FontSize=15);ylabel('Power (dB)',FontSize=15);
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