clear, close all;
RCS = 39.4825;%dBsm，设置的目标RCS值，也即RCS真值
R = 10;%m目标距离
Rrts = 1;%m DUT

c = 299792458;%m/s
f = 24e9;%Hz，工作频率
lamna = c/f;%m

Gr_ant = 15;%dB，RTS接收天线增益
Gt_ant = 15;%dB，RTS发射天线增益
% Gt_ant=15;%dB，RTS发射天线增益

Kdx_max = 51;%dB，RTS X频段接收通道最大增益
% Kdw_max=20-5;%dB，RTS W频段接收通道最大增益，5dB为端接衰减器
Kdw_max = -12;%dB，RTS W频段接收通道最大增益，5dB为端接衰减器
Att_d = 20;%dB，RTS接收衰减
% Ld=8;%dB，RTS接收线损
Ld = 0;%dB，RTS接收线损
Yita_EIRP = 0;%dB，EIRP校正值，系统参数设置界面设置参数，Yita_EIRP=雷达EIRP基准值- EIRP初始测量值（即：Yita_EIRP=0时的EIRP测量值）
%EIRP校正后的显示值= EIRP初始测量值+Yita_EIRP

Kd_max = Kdx_max+Kdw_max-Ld%dB，RTS接收通道最大增益，系统参数设置界面设置参数

Kd_max_adjust = Kd_max-Yita_EIRP;%dB，显控软件修正后的RTS接收通道最大增益
Kd = Kd_max_adjust-Att_d;%dB，RTS接收通道增益

Kfpga = 0;%dB

% Kux_max=0 ;%dB，RTS X频段发射通道最大增益
Kux_max = 0 ;%dB，RTS X频段发射通道最大增益
Kuw_max = 0;%dB，RTS 频段发射通道最大增益
% Kuw_max=20;%dB，RTS 频段发射通道最大增益
% Lu=8;%dB，RTS发射线损
Lu = 0;%dB，RTS发射线损
Yita_RCS = 0;%dB，RCS校正值，系统参数设置界面设置参数，Yita_RCS=RCS界面设置值（即RCS真值）-校正前雷达RCS测量值

Ku_max = Kux_max+Kuw_max-Lu%dB，RTS 发射通道最大增益，系统参数设置界面设置参数
% % % Yita=Yita_RCS+Yita_EIRP;%dB，RTS收发失配系数
% % % Ku_max_adjust=Kux_max+Kuw_max-Lu-Yita%dB，修正后的RTS 发射通道最大增益
Ku_max_adjust = Ku_max-Yita_RCS;%dB，修正后的RTS 发射通道最大增益

K = RCS-40*log10(R)+10*log10(4*pi*(Rrts.^4)/(lamna.^2))-Gr_ant-Gt_ant;

Ku = K-Kd-Kfpga;
% Att_u=Ku_max-Ku%RTS 发射衰减量，FPGA计算生成的发射衰减控制参数
Att_u = Ku_max_adjust-Ku%RTS 发射衰减量，FPGA计算生成的发 射衰减控制参数

% figure
% plot(R, Att_u);

pause;
