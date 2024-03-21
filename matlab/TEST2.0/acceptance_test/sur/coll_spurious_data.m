function [fre_meas, amp_meas, amp_meas1, spurious,trace] = coll_spurious_data(keysight83630B,N9020A,fre_set,spec_fre_set,point,connect_att,cable_att,y_ref,spec_span)

len = length(fre_set);
amp_meas = zeros(1,len);
fre_meas = zeros(1,len);
amp_meas1 = zeros(1,len);
spurious = zeros(1,len);

figure('Name','频谱图','NumberTitle','off');
h1 = subplot(121);
h2 = subplot(122);
trace = zeros(len,point);

for i = 1:len
    fprintf(N9020A,'DISP:WIND1:TRAC:Y:RLEV %f dBm',y_ref);
    fprintf(N9020A,'BWID:AUTO ON');
    fprintf(keysight83630B,'FREQuency %f MHz',fre_set(i));
    fprintf(N9020A,'CALC:MARK1:MAX');
    fprintf(N9020A,'CALC:MARK1:Y?');y_ref_temp=str2double(fscanf(N9020A));
    fprintf(N9020A,'DISP:WIND1:TRAC:Y:RLEV %f dBm',y_ref_temp+5);

    fprintf(N9020A,'BAND %f KHZ',30);
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
    coll_out = 50;
    temp = [temp(1:col-coll_out) temp(col+coll_out:end)];
    amp_meas1(1,i) = max(temp);
    spurious(1,i) = amp_meas1(1,i) - amp_meas(1,i) - connect_att - cable_att;

    x  = linspace(min(spec_fre_set(1),spec_fre_set(end))-spec_span,max(spec_fre_set(1),spec_fre_set(end))+spec_span,point);
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