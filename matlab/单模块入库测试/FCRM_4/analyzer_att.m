clc ; clear ; close all;
warning off

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
% load("data\rf_att\20231016_142045_RF_att_RS_up.mat");
% load(load_File);

%% 下变频衰减
if ~mode
    x = fre_set;
    amp      = amp_meas_down;
    amp_zero = amp_meas_down_zero;
    att      = amp_zero - amp;
    myplot(x,att,1,'Freq (MHz)','Power (dB)');
else
    % 衰减器 3 4 5 画图
    %     x = 4540:50:9450;
    %     amp      = amp_meas_up3;
    %     amp_zero = amp_meas_zero3;
    %     att      = amp_zero - amp;
    %     myplot(x,att,1,'Freq (MHz)','Power (dB)');
    %
    %     x = 4540:50:9450;
    %     amp      = amp_meas_up4;
    %     amp_zero = amp_meas_zero4;
    %     att      = amp_zero - amp;
    %     myplot(x,att,1,'Freq (MHz)','Power (dB)');
    %
    %     x = 4540:50:9450;
    %     amp      = amp_meas_up5;
    %     amp_zero = amp_meas_zero5;
    %     att      = amp_zero - amp;
    %     myplot(x,att,1,'Freq (MHz)','Power (dB)');

    %       for i = 1:length(fre_set)
    %       for i = 1:25
    %           x = att_up1 * 0.5;
    %           amp = amp_meas_up1(i,:);
    %           amp = amp - amp(1);
    %           myplot_att(x,amp,1,'Set Att (dB)','Power (dB)');
    %       end
    for i = 1:25
        x = att_up2 * 0.125;
        amp = amp_meas_up2(i,:);
        amp = amp - amp(1);
        myplot_att(x,amp,1,'Set Att (dB)','Power (dB)');
    end
end
