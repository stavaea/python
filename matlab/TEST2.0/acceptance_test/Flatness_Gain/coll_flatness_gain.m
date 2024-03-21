function [trace] = coll_flatness_gain(keysight83630B,N9020A,fre_set)

    len = length(fre_set);
    fprintf(N9020A,'SWE:POIN %d',len);
    for i = 1:len
        pause(0.5)
        fprintf(keysight83630B,'FREQuency %f MHz',fre_set(i));
    end
    fprintf(N9020A,':TRAC? TRACE1');
    trace = str2num(fscanf(N9020A));
end