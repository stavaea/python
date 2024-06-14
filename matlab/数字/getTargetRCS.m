function dRCS = getTargetRCS(dRMin)
    % 天线增益
    Grts_r = 13;

    % 用于存储最终计算的RCS值的变量
    dRCS = 0;

    kfpga = 0;
    % 光速
    LIGHTSPEED = 3e8; % 光速，单位：米/秒

    CenterFrequency = 24; % 中心频率
    RadarRTSDistance = 1;  % 雷达与RTS距离
    EIRPCorrection = 0;  % EIRP校正值
    RCSCorrection = 0;  % RCS校正值
    AcceptanceGainAttenuation = 30;  % 接收衰减量
    MaximumReceiveGain = 35; % 最大接收增益
    MaximumSendGain = 2;  % 最大发射增益

    % 计算波长
    lamuda = LIGHTSPEED / (CenterFrequency * 1e9);

    % π
    fPI = pi;

    % 计算k_down_max和kdown
    k_down_max = MaximumReceiveGain - EIRPCorrection;
    kdown = k_down_max - AcceptanceGainAttenuation;

    % 计算k_up_max
    k_up_max = MaximumSendGain - RCSCorrection;

    % 计算最终的dRCS值
    dRCS = k_up_max + kdown + kfpga; % kfpga在这里是0
    dRCS = dRCS + 10 * log10(dRMin^4) - 10 * log10((4 * fPI * RadarRTSDistance^4) / (lamuda^2 * (Grts_r * 2)^2));

    % 使用disp函数打印调试信息（如果需要）
%     disp(['Rmin ' num2str(dRMin) ' centerfrequency ' num2str(CenterFrequency) ' RTSDistance ' num2str(RadarRTSDistance) ...
%          ' Grts_r ' num2str(Grts_r) ' EIRPCorrection ' num2str(EIRPCorrection) ...
%          ' AcceptanceGainAttenuation ' num2str(AcceptanceGainAttenuation) ...
%          ' RCSCorrection ' num2str(RCSCorrection) ...
%          ' MaximumReceiveGain ' num2str(MaximumReceiveGain) ...
%          ' MaximumSendGain ' num2str(MaximumSendGain) ...
%          ' dRCS ' num2str(dRCS)]);
end



% 调用函数并获取结果
% dRMin = 100; % 示例dRMin值
% result = getTargetRCS(dRMin);
% disp(['The calculated dRCS is: ' num2str(result)]);