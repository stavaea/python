clc;clear all;close all;

c=3.0e8;
f0=77e9;
lamda=c/f0;
d=lamda/2;
T=100e-6;%chirp带宽
B=150e6;
K=B/T;
fs = 2e6;
ts=1/fs;
T_n=64;
prf=1/T;
t=0:ts:T_n*T-ts;
fast_t=mod(t,T);
slow_t = t-fast_t;
N=1*length(t);
R0=100;
% time_delay=2*R/c;
% f=f0+K*t;
% f_echo=f0+K*(t-time_delay);
Azimuth=30;

range_N=2*fs*T;
fd_N=2*T_n; %1/T
reslution_v=prf/fd_N*lamda/2;
reslution_R=fs/range_N/K*c/2; %fd_N
V=15;

send = exp(j*2*pi*(f0*t+K*fast_t.*fast_t/2));

tar_x =R0*sind(Azimuth)*ones(size(t));
tar_y =R0*cosd(Azimuth)*ones(size(t))-V*t;

recieve1_x=-d/2;recieve1_y=0;
recieve2_x=d/2;recieve2_y=0;
RT=sqrt((tar_x).^2+(tar_y).^2);
R1=sqrt((tar_x-recieve1_x).^2+(tar_y-recieve1_y).^2);
R2=sqrt((tar_x-recieve2_x).^2+(tar_y-recieve2_y).^2);
time_delay1=(RT+R1)/c;
time_delay2=(RT+R2)/c;

echo_1=exp(-j*2*pi*(f0*(t-time_delay1)-K*(fast_t-time_delay1).*(fast_t-time_delay1)/2));
echo_baseband1=send.*conj(echo_1);
echo_2=exp(-j*2*pi*(f0*(t-time_delay2)-K*(fast_t-time_delay2).*(fast_t-time_delay2)/2));
echo_baseband2=send.*conj(echo_2);

echo_2d1=reshape(echo_baseband1,length(echo_baseband1)/T_n,T_n);
echo_2d2=reshape(echo_baseband2,length(echo_baseband2)/T_n,T_n);

echo_2d_fft1=(fft2(echo_2d1,range_N,fd_N));
echo_2d_fft2=(fft2(echo_2d2,range_N,fd_N));
echo_2d_fft1_db1=20*log10(abs(echo_2d_fft1));
echo_2d_fft2_db2=20*log10(abs(echo_2d_fft2));

[max_value1,target_index1]=max_metrix(abs(echo_2d_fft1));
[max_value2,target_index2]=max_metrix(abs(echo_2d_fft2));

angle_meas=asind(angle(echo_2d_fft2(target_index2(1),target_index2(2)) ...
    ./echo_2d_fft1(target_index1(1),target_index1(2)))*lamda/2/pi/d);
angle_error=angle_meas-Azimuth;
sprintf('角度测量误差为%3.2f°',angle_error);

[max_value, target_index]=max_metrix(echo_2d_fft1);
target_fb=target_index(1)*fs/range_N;
target_fd=target_index(2)*prf/fd_N;
target_v=target_fd*lamda/2;
target_fr=target_fb-target_fd;
target_range=target_fr/K*c/2;

rx=linspace(0,fs-fs/range_N,range_N)/K*c/2;
figure;
plot(rx,echo_2d_fft2_db2,'.-');
xlabel('距离/m');
ylabel('幅度/dB');
grid on;zoom on;
title(sprintf('距离测量误差为%3.2f m，距离分辨率为%3.2f m',target_range-R0,reslution_R))

vx=linspace(0,prf-prf/fd_N,fd_N)*lamda/2;
figure;
plot(vx,echo_2d_fft2_db2,'.-');
xlabel('速度/m/s');
ylabel('幅度/dB');
grid on;zoom on;
title(sprintf('速度测量误差为%3.2f m/s，速度分辨率为%3.2f m/s',target_v,reslution_v))

loss_db=20*log10(max(max(abs(echo_2d_fft1)))/N);
sprintf('积累损失为%3.2f dB',loss_db)