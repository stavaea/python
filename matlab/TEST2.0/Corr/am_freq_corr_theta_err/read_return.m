function [data] = read_return(rts)
    while 1
        pause(0.15);
        if rts.BytesAvailable > 0
            break;
        end
        disp('Data Return Error Please Stop program !!!!');

    end
    data = fread(rts, rts.bytesAvailable/4,'uint32');

end