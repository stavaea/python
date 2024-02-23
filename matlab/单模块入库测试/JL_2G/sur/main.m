clc ;clear ; close all;

%%
% type = 'syn2';
ip_spec = ['TCPIP0::','192.168.1.6','::INSTR'];
point = 10001;
y_ref   = 10;
y_div   = 10;
%%
% mult                 = 6;
% GPIB_83630B          = 'GPIB0::24::INSTR';
GPIB_83630B          = 'GPIB3::10::INSTR';
fre_set              = 400:100:5400   ;
amp_set              = -25              ;

center_freq_standard = fre_set(1)        ;
%%
keysight83630B = visa('agilent', GPIB_83630B);
fopen(keysight83630B);fprintf(keysight83630B,'*IDN?');fscanf(keysight83630B);
%%
N9020A       = visa('agilent',ip_spec); %设置频谱仪ip
set(N9020A,'InputBufferSize',60e4);%尽可能大一点 便于点数录入
fopen(N9020A);fprintf(N9020A,'*IDN?');fscanf(N9020A) %设置频谱仪

%%
fprintf(keysight83630B,'FREQuency %f MHz',fre_set(1));
fprintf(keysight83630B,'POWer %f dbm',amp_set);
fprintf(keysight83630B,'POWer:STATe ON');

%%
fprintf(N9020A,'FREQ:CENT %f MHz',fre_set(1)); % 设置中心频率
fprintf(N9020A,'BAND Auto ON');% RBW
fprintf(N9020A,'SWE:POIN %d',point);
fprintf(N9020A,'DISP:WIND:TRAC:Y:PDIV %f DB',y_div);        % 设置频谱仪y轴一格代表表示多少dB。
fprintf(N9020A,'DISP:WIND1:TRAC:Y:RLEV %f dBm',y_ref);
%% Doppler
% span    = [1 1 1 1 1 1 1 1 1];
span = [0.001 0.01 0.1 1 10 100 1000 4000 5000];
len = length(fre_set);
% len = length(span);

% trace = zeros(length(span),point);

% Doppler = [0 10 -10 20 -20 50 -50 100 -100];
trace = zeros(len,point,length(span));
% diff_freq = zeros(len,1);
% fprintf(N9020A,'FREQ:SPAN %f Hz',200);% X轴范围
for j = 1:length(span)
% for j = 5:5
fig = figure();
fig.Position = [-1919 1 1920 1002];
fig.Name = sprintf('Span is %3.3f MHz',span(j));
    for i = 1:len
        fprintf(keysight83630B,'FREQuency %f MHz',fre_set(i));
        fprintf(N9020A,'FREQ:CENT %f MHz',fre_set(i));
        fprintf(N9020A,'FREQ:SPAN %f MHz',span(j));% X轴范围
    %     fprintf(N9020A,'FREQ:SPAN %f KHz',span(i));% X轴范围
        pause(3)
        fprintf(N9020A,':TRAC? TRACE1');
        trace(i,:,j) = str2num(fscanf(N9020A));
    %     figure
    %     x = linspace((fre_set*1e6-span(i)/2*1e3),(fre_set*1e6+span(i)/2*1e3),10001);
    %     x = linspace((fre_set(i)*1e6-span/2*1e3),(fre_set(i)*1e6+span/2*1e3),10001);
        x = linspace((fre_set(i)*1e6-span(j)/2*1e6),(fre_set(i)*1e6+span(j)/2*1e6),10001);
    %     plot(x,trace(i,:),'r',x,trace(1,:),'b');
%         subplot(5,11,i);
        plot(x,trace(i,:,j),'r');
        axis 'auto xy'
        xlabel('Frequency / HZ');
        ylabel('Power / dB');

        [max1,point1] = max(trace(i,:));
        [max2,point2] = max(trace(1,:));
        diff_freq = (point1 - point2) * (1e3/10001);
    %     title(sprintf('Doppler is %3.1f Hz',diff_freq));
    %     leg= ['Now Doppler';
    %           '0   Doppler'];
    %     legend(gca,leg);
    %     title(sprintf('Span is %3.0f KHz Trace',Doppler(i)));
        title(sprintf('Freq is %3.0f MHz Trace',fre_set(i)));
        grid minor;

    end
end
fprintf(keysight83630B,'POWer:STATe OFF');

%% Save
type = '板卡供电频综提供本振本振射频中频自闭环杂散测试多span' ;
clock1 = clock;
savefile = strcat(sprintf('data\\%04d%02d%02d_%02d%02d%02.0f_Trace_%s.mat',clock1(1),clock1(2),clock1(3),clock1(4),clock1(5),clock1(6),type))
% save(savefile,'span',"Doppler","trace");
save(savefile,"span",'diff_freq',"fre_set","trace","amp_set");
%%
instrreset





