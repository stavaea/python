clc ; clear ; close all;

%% Load Data
data  = load("data\20230528_121624_Trace_板卡供电频综提供本振本振射频中频自闭环杂散测试多span.mat");
% data  = load("data\20230523_185743_Trace_板卡供电信号源提供本振射频中频自闭环杂散测试多span.mat");
data1 = load("data\20230523_164733_Trace_直流稳压源供电射频头中频自闭环杂散测试多span.mat");
%% Program
span    = data.span;
fre_set = data.fre_set;
trace1  = data.trace;
trace2  = data1.trace;
len1    = length(span);
len2    = length(fre_set);

%% Plot
% for i = 5:5
for i = 1:length(span)
    fig             = figure;
    fig.NumberTitle = 'off';
    fig.Name        = sprintf('Span is %3.3f MHz',span(i));
    fig.Color       = [1 1 1];
%     fig.Position    = [-1919 1 1920 1002];
    for j = 1:len2
        x = linspace((fre_set(j)*1e6-span(i)/2*1e6),(fre_set(j)*1e6+span(i)/2*1e6),10001);
        x = x./1e6;
        if (x(1) < 0)
            x = linspace(-80,-80+span(i),10001);
        end
        y1 = trace1(j,:,i);
        y2 = trace2(j,:,i);
%         subplot(6,9,j);
        plot(x,y1,'r',x,y2,'b');
%         plot(x,y2,'b');
        axis([min(x) max(x) min([y1,y2])-1 max([y1,y2])+1]);
        xlabel('Frequency / MHZ',FontSize=20);
        ylabel('Power / dB',FontSize=20);
        title(sprintf('Freq is %3.0f MHz',fre_set(j)),FontSize=20);
        leg = ['板卡供电   '; ...
               '直流稳压源供电'];
        grid minor;
%         legend(gca,leg,FontSize=20);
    end
end


%%
copygraphics(gcf)