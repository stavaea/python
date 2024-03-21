function [data] = down_corr_table_corr(rts,freq_center,freq_lo)

    Hard       = 'A5A5A5A5';
    Type       = 'F00200FF';
    Datasize   = 1004;
%     Allsize    = 22528;
    Tail       = 'B5B5B5B5';
    %% 读取数据，截取数据
    data_d     = read_dat('corr_table\dca_err.dat');

    rts_step      = data_d(1);
    rts_band      = data_d(2);
    Allsize       = data_d(3);
    corr_data     = data_d(4:end,1);
    len_tran_data = data_d(3)/4;

    start_freq = freq_lo-(rts_band/2);
    temp       = freq_center - start_freq;
    temp1      = floor(temp/rts_step);
    data_start = temp1*len_tran_data+1;
    data_end   = data_start + len_tran_data-1;

    data_tran  = corr_data(data_start:data_end);
    len_corr   = length(data_tran);
    len_for    = ceil(len_corr/250);

    %%
    para       = zeros(250+5,1);
    para(1)    = hex2dec(Hard);
    para(2)    = hex2dec(Type) ;
    para(3)    = Datasize ;
    para(4)    = Allsize  ;
    para(255)    = hex2dec(Tail);
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
