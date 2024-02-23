clc ; clear ; close all;


%% Get File_name
Path = 'data\rf_att';
File = dir(fullfile(Path,'*.mat'));
FileNames = {File.name}';
FilePath  = {File.folder}';
temp = 0;
load_File = strcat(cell2mat(FilePath(end-temp,:)),'\',cell2mat(FileNames(end-temp,:)));
% load_File = 'data\rf_att\20230703_185601_RF_att_2G模块_9845.mat';
% load_File = 'data\rf_att\20230703_175351_RF_att_2G模块_9650.mat';
% load_File = 'data\rf_att\20230703_172957_RF_att_2G模块_9475.mat';
%% Load Data
% load("data\rf_att\20230613_205635_RF_att_2G模块.mat");
load(load_File);

%% 下变频衰减
figure('Name','下变频衰减',Color=[1 1 1]);
freq     = 400:50:5400;
att_down = amp_meas_zero - amp_meas_down;
plot(freq,att_down);grid minor;
xlabel('Freq (MHz)',FontSize=15);ylabel('Att (dB)',FontSize=15);
axis ([min(freq)-1 max(freq)+1 min(att_down)-0.1 max(att_down)+0.1]);
minn = min(att_down);
maxx = max(att_down);
x1 = yline(maxx);
x1.LineWidth = 1.5;
x1.FontSize = 15;
x1.Color = 'black';
x1.LineStyle = '-.';
x1.Label = sprintf('Max Att %.3f dB',maxx);
x1.LabelHorizontalAlignment = 'left';
x1.LabelVerticalAlignment = 'top';
x2 = yline(minn);
x2.LineWidth = 1.5;
x2.FontSize = 15;
x2.Color = 'black';
x2.LineStyle = '-.';
x2.Label = sprintf('Min Att %.3f dB',minn);
x2.LabelHorizontalAlignment = 'left';
x2.LabelVerticalAlignment = 'bottom';
%% 上变频衰减 固定
figure('Name','上变频衰减 固定',Color=[1 1 1]);
freq     = 400:50:5400;
att_up3 = amp_meas_zero - amp_meas_up3;
plot(freq,att_up3);grid minor;
xlabel('Freq (MHz)',FontSize=15);ylabel('Att (dB)',FontSize=15);
axis ([min(freq)-1 max(freq)+1 min(att_up3)-0.1 max(att_up3)+0.1]);
minn = min(att_up3);
maxx = max(att_up3);
x1 = yline(maxx);
x1.LineWidth = 1.5;
x1.FontSize = 15;
x1.Color = 'black';
x1.LineStyle = '-.';
x1.Label = sprintf('Max Att %.3f dB',maxx);
x1.LabelHorizontalAlignment = 'left';
x1.LabelVerticalAlignment = 'top';
x2 = yline(minn);
x2.LineWidth = 1.5;
x2.FontSize = 15;
x2.Color = 'black';
x2.LineStyle = '-.';
x2.Label = sprintf('Min Att %.3f dB',minn);
x2.LabelHorizontalAlignment = 'left';
x2.LabelVerticalAlignment = 'bottom';


%% 上变频衰减 压控
len = length(fre_set);
for i = 1:len
    figure('Name','上变频衰减 压控','Position',[-1919 1 1920 1002],Color=[1 1 1]);
    plot(att_up1,amp_meas_up1(i,:));
    grid minor;
    xlabel('Code',FontSize=15);ylabel('Att (dB)',FontSize=15);
    title(sprintf('Power Jitter Range : %3.3f dB',range(amp_meas_up1(i,:))),FontSize=15);
    axis ([min(att_up1)-1 max(att_up1)+1 min(amp_meas_up1(i,:))-1.5 max(amp_meas_up1(i,:))+1.5]);
    minn = min(amp_meas_up1(i,:));
    maxx = max(amp_meas_up1(i,:));
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
%% 上变频 数控
len = length(fre_set);
for i = 1:len
%    'Position', [-1919 1 1920 1002],
%     figure(Color=[1 1 1]);
    figure('Name','上变频衰减 数控','Position', [-1919 1 1920 1002],Color=[1 1 1]);
    plot(att_up2,amp_meas_up2(i,:));
    grid minor;
    xlabel('Set Att (dB)',FontSize=15);ylabel('Att (dB)',FontSize=15);
    title(sprintf('Power Jitter Range : %3.3f dB',range(amp_meas_up2(i,:))))
    axis ([min(att_up2)-1 max(att_up2)+1 min(amp_meas_up2(i,:))-3 max(amp_meas_up2(i,:))+3]);
    minn = min(amp_meas_up2(i,:));
    maxx = max(amp_meas_up2(i,:));
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