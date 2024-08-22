instrreset;
clc ; clear ; close all;


% RTS IP 地址
RTS_ip   = '192.168.1.10';
% RTS IP 端口号
RTS_port = 7;

%% 连接信号源、频谱仪、RTS
rts            = client_sever(RTS_ip,RTS_port);


adc_p = 40; %0~120
dac_p = 2; %0~3
ADC_DAC_phase(rts,adc_p,dac_p)

instrreset;