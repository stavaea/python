function [data] = att_control(rts,tran)

syspara = zeros(1,5);
syspara(1)	= hex2dec('A5A5A5A5');
syspara(2)	= hex2dec('C00300FF');
syspara(3)	= 4;
syspara(4)	= tran/0.0625;
syspara(5)	= hex2dec('B5B5B5B5');
rts.write(syspara,'uint32');
data = read_return(rts);
end