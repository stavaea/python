function [data] = down_sim_para(rts,start_dis,start_speed)
%    if(start_dis > 2.4)
%         start_dis = start_dis*1.0001 - (0.0258)/2;
%         start_dis = (start_dis  - 0.02);
%         start_dis = (start_dis  - 0.02)*1.004-0.0035;
%    end

    syspara     = zeros(1,120);
    syspara(1)	= hex2dec('A5A5A5A5');
    syspara(2)	= hex2dec('C30200FF');
    syspara(3)	= 464;
    % 目标有效 b0：表示目标1 0：无效 1：有效
    syspara(4)	= uint32(1);
    % EIRP最大值 0
    syspara(5)	= uint32(20);
    % 幅度距离 0 :恒定幅度 1:距离衰变
    syspara(6)	= uint32(0);
    % 角度模拟 0: 角度不模拟 1: 角度模拟
    syspara(7)	= uint32(0);
    %最长周期数低位
    syspara(8)	= int32(0);
    %最长周期数高位
    syspara(9)  = uint32(bitshift(syspara(8),-32));
    % 目标1运动类型 0：标较 1：运动
    syspara(10) = uint32(0);
    %目标1循环模式 0：单次 1：循环
    syspara(11)  = int32(1);
    %目标1周期数低位
    syspara(12)  = int32(0);
    %目标1周期数高位
    syspara(13)  = int32(bitshift(0,-32));
    %目标1加速度低位
    syspara(14)  = int32(0);
    %目标1加速度高位
    syspara(15)  = int32(bitshift(0,-32));
    %目标1 K1低位
    syspara(16)  = int32(0);
    %目标1 K1高位
    syspara(17)	= uint32(bitshift(0,-32));
    %目标1 K2低位
    syspara(18)	= uint32(0);
    %目标1 K2高位
    syspara(19)	= uint32(bitshift(0,-32));
    %目标1 K3低位
    syspara(20)	= uint32(0);
    %目标1 K3高位
    syspara(21)	= uint32(bitshift(0,-32));
    %目标1 H
    syspara(22)	= int32(0);
    %目标1起始距离低位
    syspara(23)	= uint32(round(start_dis * 1e3));
    %目标1起始距离高位
    syspara(24) = uint32(bitshift(round(start_dis * 1e3),-32));
    %目标1结束距离低位 单位：m 精度0.001m 范围 ：0~500
    syspara(25) = uint32(round(start_dis * 1e3));
    %目标1结束距离高位 单位：m 精度0.001m 范围 ：0~500
    syspara(26) = uint32(bitshift(round(start_dis * 1e3),-32));
    % 目标1起始速度 单位：m/s 精度0.001m/s
    syspara(27) = uint_int(round(start_speed * 1e3));
    % 目标1结束速度 单位：m/s 精度0.001m/s
    syspara(28)	= uint_int(round(start_speed * 1e3));
    % 目标1RCS 单位：dBsm 精度0.001
    syspara(29)	= uint_int(1000);
    % 目标1起始角度 单位：° 精度0.001m 范围：-90~90
    syspara(30)	= uint_int(0);
    % 目标1结束角度 单位：° 精度0.001m 范围：-90~90
    syspara(31)	= uint_int(0);

    syspara(120)	= hex2dec('B5B5B5B5');
    rts.write(syspara,'uint32');
    data = read_return(rts);
end