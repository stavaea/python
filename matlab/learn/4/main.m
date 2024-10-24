clc,clear all,close all;

% 某77GHz雷达发射雷达线性调频信号，中心频率为77.075GHz，带宽150MHz，发射信号时间宽度为100us，光速为 3e8m/s。
% 请产生一个50m静止目标的单个脉冲重复周期时间内的回波，选择合适的采样率fs进行仿真，并给出fs的选择分析依据;
% 1.画出发射信号频率随时间的变化关系，在同一张图上画出回波信号频率随时间的变化关系，给出横纵坐标，曲线标志legend;
% 2.并对回波做去斜处理，再对回波进行 FFT处理，获得一维距离像，画图展示一维距离像，横坐标为距离，
% 纵坐标为归一化幅度/dB，标题为一维距离像
% 提示:发射信号表达式为:y=exp(j*2*pi* ( f0*t + K*t.*t/2))其中f0为起始发射频率，k为调频斜率。
% 回波信号为 y=exp(-j*2*pi* ( f0*t + 0.5*k.* (t-delay).* (t-delay ) ) ) ;

c=3.0e8;
f0=77e9;
T=100e-6;%chirp带宽
B=150e6;
K=B/T;
fs = 1.500e6;
ts=1/fs;
t=0:ts:1*T-ts;
fast_t=mod(t,T);
N=1*length(t);
R=100;
time_delay=2*R/c;
f=f0+K*t;
f_echo=f0+K*(t-time_delay);

send = exp(j*2*pi*(f0*t+K*t.*t/2));
% send = exp(j*2*pi* (f0*t + 0.5*t.*t/2));
echo = exp(j*2*pi*(f0*(t-time_delay)+K*(t-time_delay).*(t-time_delay)/2));
% echo = exp(-j*2*pi*(f0*(t-time_delay)+0.5*(t-time_delay).*(t-time_delay)/2));
% echo = circshift(send,[round(time_delay/ts),1]);
echo_baseband = send.*conj(echo);

fftn = 10*N;
echo_baseband_fft = abs(fft(echo_baseband,fftn));
echo_baseband_fft_db = 20*log10(echo_baseband_fft/max(echo_baseband_fft));
f_x = linspace(0,fs-fs/fftn,fftn);
r_x = f_x/K*c/2;

figure;
plot(t,f,'-',t,f_echo,'ro-');
title('时频图');
xlabel('t/s');
ylabel('Hz');
legend('send','back');

figure;
plot(r_x,echo_baseband_fft_db, '.-');
title('一维距离像');
xlabel('m');
ylabel('dB');
grid on;zoom on;

