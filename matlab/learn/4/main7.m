close all;clear all;clc;tic


c = 3.0e8;
f0 = 77e9;
T = 100e-6; %chirp时宽
B = 150e6; %chirp带宽
K = B/T;
fs = 1.500e6;
ts = 1/fs;
t = 0:ts:1*T-ts;
fast_t = mod(t,T);

N = 1*length(t);
R = 100;
time_delay = 2*R/c;
f = f0 + K*t;
f_echo = f0 + K*(t-time_delay);

send_sigal = exp(j*2*pi*(f0*t+K*t.*t/2));
% echo = circshift(send_sigal,[round(time_delay/ts),1]);
echo = exp(j*2*pi*(f0*(t-time_delay)+K*(t-time_delay).*(t-time_delay)/2));
echo_baseband = send_sigal.*conj(echo);

fftn = 10*N;
% echo_baseband = echo_baseband.*hamming(length(echo_baseband))';
echo_baseband_fft = abs(fft(echo_baseband,fftn));
echo_baseband_fft_dB = 20*log10(echo_baseband_fft/max(echo_baseband_fft));
f_x = linspace(0,fs-fs/fftn,fftn);
r_x = f_x/K*c/2;
% figure;plot(real(echo_baseband))
figure;plot(t,f,'.-',t,f_echo,'ro-');title('时频图');legend('发射信号','回波信号')
figure;plot(r_x,echo_baseband_fft_dB,'.-');grid on;zoom on;
% ylim([-80 0]);
% figure;mesh(echo_baseband_fft);grid on;zoom on;


