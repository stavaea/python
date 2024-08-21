function [data] = read_return(rts)
    while 1
        pause(0.15);
        if rts.BytesAvailable > 0
            break;
        end
        disp("Data Return Error Please Stop program !!!!");

    end
    data = dec2hex(rts.read(rts.NumBytesAvailable/4,'uint32'));

end