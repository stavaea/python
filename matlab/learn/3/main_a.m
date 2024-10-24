clc;close all,clear all;

f = 10; % 频率
amplitude = 1; % 幅度
fs = 20; % 采样率
duration = 1; % 采样时长
% 生成时间向量
t = 0:1/fs:duration;
% 生成复信号正弦波
y=exp(j*2*pi*f*t);

N=10*length(y);
fft_s=abs(fft(y, N));
fx = linspace(0,fs-fs/N,N);
ffs_dB=20*log10(fft_s/max(fft_s));
figure;
plot(fx,ffs_dB,'r.-');
xlabel('Hz');
ylabel('幅度');
ylim([-70 10]);
[b,c]=find(ffs_dB>=-3);
M = (max(c)-min(c))*fs/N;
% A = fs/N
title(sprintf('3dB频谱宽度为:%4.3f Hz',M));
zoom on;
grid on;


