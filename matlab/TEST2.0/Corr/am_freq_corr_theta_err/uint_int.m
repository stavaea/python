function [data] = uint_int(data_int)
if data_int < 0
    t = hex2dec('FFFFFFFF');
    data = t + data_int + 1;
else
    data = data_int;
end