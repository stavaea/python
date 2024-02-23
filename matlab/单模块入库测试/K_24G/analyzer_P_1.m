clc ; clear ; close all;

%%
% Path = 'data\P_1_down';
Path = 'data\P_1_up';
File = dir(fullfile(Path,'*.mat'));
FileNames = {File.name}';
FilePath  = {File.folder}';
temp = 0;
load_File = strcat(cell2mat(FilePath(end-temp,:)),'\',cell2mat(FileNames(end-temp,:)));
data =  load(load_File);
%% Load Data
% data = load("data\rf_p_1\20230704_111532_rf_p_1_2G模块_9470.mat");
% data = load("data\rf_p_1\20230703_162254_rf_p_1_2G模块_9650.mat");
% data = load("data\rf_p_1\20230703_170314_rf_p_1_2G模块_9845.mat");
% data = load("data\rf_p_1\20230721_104501_rf_p_1_77GHz经济版5G带宽2023004003.mat");


%% Data processing
len  = length(data.fre_set);
len1 = length(data.amp_set);
% len2 = length(data.amp_set2);
% len3 = length(data.amp_set3);


x1 = data.amp_set;
% x2 = data.amp_set2;
% x3 = data.amp_set3;

str = ['采集曲线' ;...
       '理论曲线'];
for i = 1:len
    fig = figure;
    fig.Color = [1 1 1];
%     fig.Position = [-1919 1 1920 1002];
    y1 = data.amp_meas(i,1:len1);
%     y2 = data.amp_meas(i,len1+1:len1+len2);
%     y3 = data.amp_meas(i,len1+len2+1:end);

    y12 = x1+(y1(1) - x1(1));
%     y22 = x2+(y2(1) - x2(1));
%     y32 = x3+(y3(1) - x3(1));
    ereor1 = y1 - y12;
%     ereor2 = y2 - y22;
%     ereor3 = y3 - y32;
    h1 = subplot(121);
%     h2 = subplot(232);
%     h3 = subplot(233);
    h4 = subplot(122);
%     h5 = subplot(235);
%     h6 = subplot(236);
    plot(h1,x1,y1,'r',x1,y12,'b');legend(h1,str,'Box','OFF','Location','north',FontSize=15);
%     plot(h2,x2,y2,'r',x2,y22,'b');legend(h2,str,'Box','OFF','Location','north',FontSize=15);
%     plot(h3,x3,y3,'r',x3,y32,'b');legend(h3,str,'Box','OFF','Location','north',FontSize=15);
    xlabel(h1,'Set Power / dB',FontSize=15);ylabel(h1,'Spec Power / dB',FontSize=15);
%     xlabel(h2,'Set Power / dB',FontSize=15);ylabel(h2,'Spec Power / dB',FontSize=15);
%     xlabel(h3,'Set Power / dB',FontSize=15);ylabel(h3,'Spec Power / dB',FontSize=15);
    plot  (h4,x1,ereor1);
%     plot  (h5,x2,ereor2);
%     plot  (h6,x3,ereor3);
    xlabel(h4,'Set Power / dB',FontSize=15);ylabel(h4,'Error',FontSize=15);
%     xlabel(h5,'Set Power / dB',FontSize=15);ylabel(h5,'Error',FontSize=15);
%     xlabel(h6,'Set Power / dB',FontSize=15);ylabel(h6,'Error',FontSize=15);
    grid(h1,'minor');
%     grid(h2,'minor');
%     grid(h3,'minor');
    grid(h4,'minor');
%     grid(h5,'minor');
%     grid(h6,'minor');
end



