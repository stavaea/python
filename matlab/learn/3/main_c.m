clc;close all,clear all;

f = 10; % 频率
amplitude = 1; % 幅度
fs1 = 20; % 采样率
fs2=40;
duration = 1; % 采样时长
% 生成时间向量
t1 = 0:1/fs1:duration;
t2 = 0:1/fs2:duration;
% 生成复信号正弦波
y1=exp(j*2*pi*f*t1);
y2=exp(j*2*pi*f*t2);

N1=1000*length(y1);
fft_s1=abs(fft(y1, N1));
fx1 = linspace(0,fs1-fs1/N1,N1);
ffs1_dB=20*log10(fft_s1/max(fft_s1));
figure;
plot(fx1,ffs1_dB,'r');
[a,c]=find(ffs1_dB>=-3);
M1 = (max(c)-min(c))*fs1/N1;

hold on;

N2=1000*length(y2);
fft_s2=abs(fft(y2, N2));
fx2 = linspace(0,fs2-fs2/N2,N2);
ffs2_dB=20*log10(fft_s2/max(fft_s2));
plot(fx2,ffs2_dB,'black');
[b,c]=find(ffs2_dB>=-3);
M2 = (max(c)-min(c))*fs2/N2;
title(sprintf('40Hz时3dB频谱宽度为:%4.3f Hz；20Hz时3dB频谱宽度为:%4.3f Hz',M2,M1));
xlabel('Hz');
ylabel('幅度');
ylim([-70 10]);
legend('20','40');
zoom on;
grid on;