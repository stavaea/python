% 产生一个频率为10Hz的复信号，幅度为1，采样率为100Hz，采样时长为1s，利用matlab进行频谱分析。
% 画图1，横坐标名称:时间，单位秒，纵坐标名称:幅度，题目:10Hz信号时域图
% 画图2，横坐标名称:频率，单位Hz，纵坐标名称:幅度，题目:10Hz信号频谱图，需要确保频率所在的位置正确。
% 画图3，横坐标名称:频率，单位Hz，纵坐标名称，归一化幅度，单位dB;题目:10Hz信号频谱图，利用公式20*log10(x/max(x)),其中，x为频谱幅度
% 画图4
% 将10Hz信号改成10.5Hz，观察发生的频谱栅栏效应:如何解决?(补一倍的零)。
% 为什么信号的频谱看不到sinc函数形状?如何解决?
% 将解决前后的频谱图画在一张图上，用不同的颜色表示
f=10;fs=100;T=1;ts=1/fs;
t=0:ts:T-ts;
s=exp(j*2*pi*f*t);
N=10*length(s);
fx=linspace(0,fs-fs/N,N);
ffs=abs(fft(s,N));

figure; %图1
plot(t,s,'.-');
xlabel('时间/s');ylabel('幅度');title('10Hz信号时域图');
grid on;
zoom on;

figure;%图2
bs=10;
N1=bs*N;
fft_s1 = abs(fft(s,N1));
fx1 = linspace(0,fs-fs/N1,N1);
plot(fx1,fft_s1,'.-');
xlabel('频率/Hz');ylabel('幅度');title('10Hz信号频谱图');
grid on;
zoom on;

figure;%图3
ffs=abs(fft(s,N));
ffs_dB=20*log10(ffs/max(ffs));
plot(fx,ffs_dB,'.-');
xlabel('频率/Hz');ylabel('归一化幅度/dB');title('10Hz信号频谱图');
grid on;
zoom on;