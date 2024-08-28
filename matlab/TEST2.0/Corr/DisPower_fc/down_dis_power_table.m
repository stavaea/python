function [data] = down_dis_power_table(rts,file_dis)
    Hard       = 'A5A5A5A5';
    Type       = 'F00800FF';
    Datasize   = 1004;
    Tail       = 'B5B5B5B5';

    data_h              = read_dat(file_dis);

    Allsize             = data_h(4);
    data_tran           = data_h(5:end);
    len_corr            = length(data_tran);
    len_for             = ceil(len_corr/250);
    para                = zeros(250+5,1);
    para(1)             = hex2dec(Hard);
    para(2)             = hex2dec(Type) ;
    para(3)             = Datasize ;
    para(4)             = Allsize  ;
    para(255)           = hex2dec(Tail);

    for i = 1:(len_for-1)
        start  = (i-1) * 250;
        para(5:254) = data_tran(start+1 : start + 250);
        rts.write(para,'uint32');
        data = read_return(rts);
    end
    %%
    len           = len_corr - (len_for-1) * 250;
    start         = ((len_for-1)) * 250;
    para          = zeros(len+5,1);
    para(1)       = hex2dec(Hard);
    para(2)       = hex2dec(Type) ;
    Datasize = len*4+4;
    para(3)       = Datasize ;
    para(4)       = Allsize  ;
    para(5:4+len) = data_tran(start+1:end);
    para(len+5)     = hex2dec(Tail);
    rts.write(para,'uint32');
    data = read_return(rts);
end
