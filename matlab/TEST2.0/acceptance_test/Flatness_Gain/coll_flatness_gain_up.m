function [trace] = coll_flatness_gain_up(keysight83630B,hp83712B,N9020A,fre_set_lo,fre_set)
    len      = length(fre_set);
    trace    = zeros(1,len);
    fre_meas = zeros(1,len);
    fprintf(N9020A,'SWE:POIN %d',1001);
    fprintf(N9020A,'FREQ:CENT %f MHz',300);
    fprintf(N9020A,'FREQ:SPAN %f Hz',2000);
    pause(0.5)
    fprintf(N9020A,'CALC:MARK1:MAX');
    fprintf(N9020A,'CALC:MARK1:Y?');
    y_ref_temp=str2double(fscanf(N9020A));

    fprintf(N9020A,'DISP:WIND1:TRAC:Y:RLEV %f dBm',y_ref_temp+10);

    for i = 1:len
        fprintf(keysight83630B,'FREQuency %f MHz',fre_set(i));
        fprintf(hp83712B,'FREQuency %f MHz',fre_set_lo(i));
        pause(0.5)
        fprintf(N9020A,'CALC:MARK1:MAX');         %将mark1设置为最大值
        fprintf(N9020A,'CALC:MARK1:X?');fre_meas(i)=str2double(fscanf(N9020A));
        fprintf(N9020A,'CALC:MARK1:Y?');trace(i)   =str2double(fscanf(N9020A));
    end
end