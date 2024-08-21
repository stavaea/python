  
% % 调用函数并获取结果  
[dRMin] = targetRCS(10); % 示例dRMin值  
% result = getTargetRCS(dRMin);  
disp(['The calculated dRCS is: ' num2str(dRMin)]);


function dRCS = targetRCS(dRMin)  
    % 天线增益 
    Grts_r = 10;    %E 10, K 7.5
    % 用于存储最终计算的RCS值的变量  
    dRCS = 0;      
    kfpga = 0;
    RCS = 15;   
    LIGHTSPEED = 299792458; % 光速，单位：米/秒  
    CenterFrequency = 77; % 中心频率
    RadarRTSDistance = 1;  % 雷达与RTS距离
    DisCorrection  = 0; % 距离校正值
    EIRPCorrection = 0;  % EIRP校正值
    RCSCorrection = 0;  % RCS校正值
    AcceptanceGainAttenuation = 24;  % 接收衰减量 47dr
%     AcceptanceGainAttenuation = 26;  % 接收衰减量 ku
    MaximumReceiveGain = 35; % 最大接收增益  47dr
%     MaximumReceiveGain = 36; % 最大接收增益  ku
%     MaximumSendGain = -2;  % 最大发射增益  47dr不加放大器
    MaximumSendGain = 20;  % 最大发射增益  47dr加放大器
%     MaximumSendGain = 1;  % 最大发射增益   ku115
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
%     dRCS = dRCS + 10 * log10((dRMin + DisCorrection)^4) - 10 * log10((4 * fPI * RadarRTSDistance^4) / (lamuda^2 * (Grts_r * 2)^2));  
    dRCS = dRCS + 10 * log10((dRMin + DisCorrection)^4) - 10 * log10((4 * fPI * RadarRTSDistance^4) / (lamuda^2 )) + (Grts_r * 2);  
%     dRCS = dRCS - 10*log10(RCS) %RCS即设置的地面反射系数实际值

    % 使用disp函数打印调试信息（如果需要）  
%     disp(['Rmin ' num2str(dRMin) ' centerfrequency ' num2str(CenterFrequency) ' RTSDistance ' num2str(RadarRTSDistance) ...  
%          ' Grts_r ' num2str(Grts_r) ' EIRPCorrection ' num2str(EIRPCorrection) ...  
%          ' AcceptanceGainAttenuation ' num2str(AcceptanceGainAttenuation) ...  
%          ' RCSCorrection ' num2str(RCSCorrection) ...  
%          ' MaximumReceiveGain ' num2str(MaximumReceiveGain) ...  
%          ' MaximumSendGain ' num2str(MaximumSendGain) ...  
%          ' dRCS ' num2str(dRCS)]);  
end  
  

