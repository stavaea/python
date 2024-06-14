function[return_data] = sim_para(rts)
    syspara     = zeros(1,4);
    syspara(1)	= hex2dec('A5A5A5A5');
    syspara(2)	= hex2dec('C00100FF');
    syspara(3)	= 0;
    syspara(4)  = hex2dec('B5B5B5B5');
    rts.write(syspara,'uint32');
    data = read_return(rts);

    return_data(1) = hex2dec(data(5,:)) - 100;
    return_data(2) = hex2dec(data(6,:)) - 100;
    return_data(3) = hex2dec(data(7,:)) - 100;

end