function [fre_meas, amp_meas, amp_meas1, spurious,trace] = spurious_data(keysight83630B,N9020A,fre_set,point)
len = length(fre_set);
amp_meas = zeros(1,len);
fre_meas = zeros(1,len);
amp_meas1 = zeros(1,len);
spurious = zeros(1,len);
bar = waitbar(0,'Please wait ......');
figure('Name','频谱图','NumberTitle','off');
h1 = subplot(121);
h2 = subplot(122);
trace = zeros(len,point);

for i = 1:len
    fprintf(keysight83630B,'FREQuency %f MHz',fre_set(i));
    fprintf(N9020A,'BAND %f KHZ',30);
    pre = i/len;
    waitbar(pre,bar,sprintf('当前频率为：%.3f MHz\n%.2f%%',fre_set(i),pre*100));

    pause(8);
    fprintf(N9020A,':TRAC? TRACE1');
    trace(i,:) = str2num(fscanf(N9020A));
    pause(0.5);
    fprintf(N9020A,'CALC:MARK1:MAX');
    fprintf(N9020A,'CALC:MARK1:X?');fre_meas(1,i)=str2double(fscanf(N9020A));
    fprintf(N9020A,'CALC:MARK1:Y?');amp_meas(1,i)=str2double(fscanf(N9020A));

    temp = trace(i,:);
    [~, col]= max(temp);
    temp(col) = -100;
    amp_meas1(1,i) = max(temp);
    spurious(1,i) = amp_meas1(1,i) - amp_meas(1,i) ;

    x  = linspace(4600,9600,1001);
    plot(h1,x,trace(i,:),'LineWidth',1);
    axis(h1,[min(x) max(x) min(trace(i,:) ) max(trace(i,:) )]);
    xlabel(h1,'频率/MHz');ylabel(h1,'功率/dB');
    title(h1,sprintf('当前杂散为：%.3f dB',spurious(1,i)));

    x = fre_set(1:i);
    y = spurious(1:i);
    plot(h2,x,y,'LineWidth',1);
    xlabel(h2,'频率/MHz');ylabel(h2,'杂散/dB');
    title(h2,sprintf('杂散抖动为：%.3f dB',range(y)));


end
close(bar)