clc;close all,clear all;

f = 10; % 频率
amplitude = 1; % 幅度
fs = 20; % 采样率
duration1 = 1; % 采样时长
duration2 = 2;
% 生成时间向量
t1 = 0:1/fs:duration1;
t2 = 0:1/fs:duration2;
% 生成复信号正弦波
y1=exp(j*2*pi*f*t1);
y2=exp(j*2*pi*f*t2);

N1=1000*length(y1);
fft_s1=abs(fft(y1, N1));
fx1 = linspace(0,fs-fs/N1,N1);
ffs1_dB=20*log10(fft_s1/max(fft_s1));
figure;
plot(fx1,ffs1_dB,'r');
[a,c]=find(ffs1_dB>=-3);
M1 = (max(c)-min(c))*fs/N1;

hold on;

N2=1000*length(y2);
fft_s2=abs(fft(y2, N2));
fx2 = linspace(0,fs-fs/N2,N2);
ffs2_dB=20*log10(fft_s2/max(fft_s2));
plot(fx2,ffs2_dB,'black');

[b,c]=find(ffs2_dB>=-3);
M2 = (max(c)-min(c))*fs/N2;
title(sprintf('2秒时3dB频谱宽度为:%4.3f Hz;1秒时3dB频谱宽度为:%4.3f Hz',M2,M1));

ylim([-70 10]);
xlabel('Hz');
ylabel('幅度');
legend('1','2');
zoom on;grid on;