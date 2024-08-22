function [data] = adc_dac_p(rts,adc_p,dac_p)
%%%%%%%%%%%%%%%%%%%%%%%%%%%END%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    syspara     = zeros(1,6);
    syspara(1)  = hex2dec('A5A5A5A5');
    syspara(2)  = hex2dec('C00700FF');
    % 数据大小 uint
    syspara(3)  = 8;
    % 参数更新时间间隔，精度0.1ms,范围0~1000,单位ms
    syspara(4)  = adc_p;
    % RTS延时，精度0.001m，范围0~500，单位m
    syspara(5)  = dac_p;
    % 包尾
    syspara(6) = hex2dec('B5B5B5B5');
    rts.write(syspara,'uint32');

    data = read_return(rts);
end
