clc;close all,clear all;

f = 10; % 频率
amplitude = 1; % 幅度
fs = 20; % 采样率
duration = 1; % 采样时长
% 生成时间向量
t = 0:1/fs:duration;
% 生成复信号正弦波
y=exp(j*2*pi*f*t);

N1=10*length(y);
fft_s1=abs(fft(y, N1));
fx1 = linspace(0,fs-fs/N1,N1);
ffs1_dB=20*log10(fft_s1/max(fft_s1));
figure;
plot(fx1,ffs1_dB);
[a,c]=find(ffs1_dB>=-3);
M1 = (max(c)-min(c))*fs/N1;

hold on;

N2=1000*length(y);
fft_s2=abs(fft(y, N2));
fx2 = linspace(0,fs-fs/N2,N2);
ffs2_dB=20*log10(fft_s2/max(fft_s2));
plot(fx2,ffs2_dB,'r');
ylim([-70 10]);
[b,c]=find(ffs2_dB>=-3);
M2 = (max(c)-min(c))*fs/N2;
title(sprintf('20000点DFT时3dB频谱宽度为:%4.3f Hz；200点DFT时3dB频谱宽度为:%4.3f Hz',M2,M1));
xlabel('Hz');
ylabel('幅度');
legend('200','20000');
zoom on;grid on;