%利用y=exp(j*2*pi*f*t)产生一个频率为10Hz的复信号正弦波，幅度为1采样率为30Hz，采样时长为1s;
% 将频谱图copy到实验报告中，标题显示出信号的频率 (title (sprintf(信号的频率%d Hz，f (i) ) ) )。
%做一个for循环，让信号的频率从OHz变化到50Hz，步进量为1Hz，观察频谱的动态显示结果(不用写入报告):
% 再让信号频率再从OHz变化到-50Hz，步进量为-1Hz，根据结果说明一下DFT的混叠效应。
%注意标题中信号的频率应该动态变化;For循环内可以采用pause停止功能。

f=1:50;

% f=0:-1:-50;
fs=30;
ts=1/fs;
T=1;
t=0:ts:T-ts;

% s=exp(j*2*pi*f*t);
figure;

for i =1:length(f)
    s=exp(j*2*pi*f(i)*t);
    N=length(s);
    fft_s=abs(fft(s));
    f_index=linspace(0,fs-fs/N,N);
    plot(f_index,fft_s,'.-');
    xlabel('频率/Hz');
    ylabel('幅度');
    title(sprintf('信号的频率：%d Hz',f(i)));%3.1f
    ylim([0 30]);
    zoom on;
    grid on;
    pause(0.2);
end