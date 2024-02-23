clc ; clear ; close all;

%% Load Data
data = load("20230516_190911_Trace_Doppler_测试.mat");

%% Plot Set
len = length(data.Doppler);
point = length(data.trace);

for i = 1:len
    figure(Color=[1 1 1]);
    x = linspace(data.fre_set-data.span(i)/2,data.fre_set+data.span(i)/2,point);
    plot(x,data.trace(i,:));
    axis 'auto xy'
    xlabel('Frequency / KHZ');
    ylabel('Power / dB');
%     title(sprintf('Doppler is %3.0f Hz Trace',data.Doppler(i)/10));
    grid minor;
end
