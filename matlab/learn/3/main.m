clc;close all,clear all;

f1 = 10; % 频率
f2=10.5;
f3=15;
amplitude = 1; % 幅度
fs = 20; % 采样率
duration = 2; % 采样时长
% 生成时间向量
t = 0:1/fs:duration;
% 生成复信号正弦波
y1=exp(j*2*pi*f1*t);
y2=exp(j*2*pi*f2*t);
y3=exp(j*2*pi*f3*t);

N = 20;
N1=N*length(y1);
fft_s1=abs(fft(y1, N1));
fx1 = linspace(0,fs-fs/N1,N1);
ffs1_dB=20*log10(fft_s1/max(fft_s1));
figure;
plot(fx1,ffs1_dB,'g.-');
hold on;

N2=N*length(y2);
fft_s2=abs(fft(y2, N2));
fx2 = linspace(0,fs-fs/N2,N2);
ffs2_dB=20*log10(fft_s2/max(fft_s2));
plot(fx2,ffs2_dB,'r.-');
hold on;

N3=N*length(y3);
fft_s3=abs(fft(y3, N3));
fx3 = linspace(0,fs-fs/N3,N3);
ffs3_dB=20*log10(fft_s3/max(fft_s3));
plot(fx3,ffs3_dB,'black.-');

ylim([-70 10]);
xlabel('Hz');
ylabel('dB');
legend('10','10.5','15');
zoom on;grid on;