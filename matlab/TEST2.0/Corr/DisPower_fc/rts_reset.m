function [data] = rts_reset(rts)
    Hard     = 'A5A5A5A5';
    Type     = 'C00000FF';
    Datasize = '00000000';
    Tail     = 'B5B5B5B5';

    % Group Packet
    para = [hex2dec(Hard);hex2dec(Type);hex2dec(Datasize);hex2dec(Tail)];
    rts.write(para,"uint32");
    data = read_return(rts);
end