function [data] = start_simulation(rts,para)
syspara = zeros(1,7);
syspara(1)	= hex2dec('A5A5A5A5');
syspara(2)	= hex2dec('C30000FF');
syspara(3)	= 12;
% 0：单次模拟 1 ：循环模拟
syspara(4)	= 1;
% 0：简单目标1：自定义目标2：实时目标
syspara(5)	= 0;
% 0：停止模拟 1：启动模拟
syspara(6)	= para;
syspara(7)	= hex2dec('B5B5B5B5');
rts.write(syspara,'uint32');
data = read_return(rts);
end