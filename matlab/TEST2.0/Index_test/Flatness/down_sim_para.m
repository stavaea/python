function [data] = down_sim_para(rts,start_dis,start_speed)
   if(start_dis > 2.4)
%         start_dis = start_dis*1.0001 - (0.0258)/2;
        start_dis = (start_dis  - 0.02);
%         start_dis = (start_dis  - 0.02)*1.004-0.0035;
   end

    syspara     = zeros(1,44);
    syspara(1)	= hex2dec('A5A5A5A5');
    syspara(2)	= hex2dec('C30200FF');
    syspara(3)	= 160;
    % 运动类型 0 : 标校目标 1 ：运动目标
    syspara(4)	= 0;
    % 目标有效 b0：表示目标1 0：无效 1：无效
    syspara(5)	= 1;
    % EIRP最大值 0
    syspara(6)	= 20;
    % 幅度距离 0 :恒定幅度 1:距离衰变
    syspara(7)	= 0;
    % 角度模拟 0: 角度不模拟 1: 角度模拟
    syspara(8)	= 0;
    % 目标1起始距离 单位：m 精度0.001m 范围 ：0~500
    syspara(9)	= round(start_dis * 1e3);
    % 目标1起始角度 单位：° 精度0.001m 范围：-90~90
    syspara(10)	= uint_int(0);
    % 目标1结束距离 单位：m 精度0.001m 范围 ：0~500
    syspara(11)	= round(start_dis * 1e3);
    % 目标1结束角度 单位：° 精度0.001m 范围：-90~90
    syspara(12)	= uint_int(0);
    % 目标1起始速度 单位：m/s 精度0.001m/s
    syspara(13)	= uint_int(round(start_speed * 1e3));
    % 目标1结束速度 单位：m/s 精度0.001m/s
    syspara(14)	= uint_int(round(start_speed * 1e3));
    % 目标1RCS 单位：dBsm 精度0.001
    syspara(15)	= uint_int(1000);
    syspara(44)	= hex2dec('B5B5B5B5');
    rts.write(syspara,'uint32');
    data = read_return(rts);
end