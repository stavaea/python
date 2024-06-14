clc; close all; clear;

dRMin = 100;


Grts_r = 10;
LIGHTSPEED = 3e8;
fPI = pi;
d_RCS = 0;
kfpga = 0;

CenterFrequency = 76; % 中心频率
RadarRTSDistance = 1;  % 雷达与RTS距离
EIRPCorrection = 0;  % EIRP校正值
RCSCorrection = 0;  % RCS校正值
AcceptanceGainAttenuation = 25;  % 接收衰减量
MaximumReceiveGain = 35; % 最大接收增益
MaximumSendGain = 4;  % 最大发射增益

lamuda = LIGHTSPEED / (CenterFrequency * 1e9);

k_up_max = MaximumSendGain - RCSCorrection;
k_down_max = MaximumReceiveGain - EIRPCorrection;
kdown = k_down_max - AcceptanceGainAttenuation;

d_RCS = k_up_max + kdown + kfpga ;
d_RCS = d_RCS + (10*log10((dRMin^4))-10*log10((4*fPI*(RadarRTSDistance^4))/(lamuda^2)*(Grts_r*2^2)));