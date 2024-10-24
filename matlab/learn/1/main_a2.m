% 信号参数
% f = 10; % 频率为 10Hz
% amplitude = 1; % 幅度为 1
% fs = 100; % 采样率为 100Hz
% duration = 1; % 采样时长为 1s
% % 生成时间向量
% t = 0:1/fs:duration;
%
% % 生成复信号正弦波
% y = cos(2*pi*f*t)+j*sin(2*pi*f*t);
% % 绘制实部和虚部
% figure;
% plot(t, real(y), 'g.-');
% hold on;
% plot(t,imag(y),'ro-');
% xlabel('时间 (秒)');
% ylabel('幅度');
% title('10Hz 信号时域图');
% legend(['实部';'虚部']);
% grid on ;
% zoom on;

%信号参数
f = 10; % 频率为 10Hz
amplitude = 1; % 幅度为 1
fs = 100; % 采样率为 100Hz
duration = 1; % 采样时长为 1s
% 生成时间向量
t = 0:1/fs:duration;
% 生成复信号正弦波
y = cos(2*pi*f*t)+1i*sin(2*pi*f*t);
%产生高斯噪声
c = sqrt(0.1);
% noise = randn(size(t)) * c;
noise = randn(1,10000)*c;
hist(noise,100);    %生成直方图
% yn = y+noise;
yn = y + (noise(1:101))+j*noise(102:202);
% 绘制实部和虚部
figure;
plot(t, real(yn), 'black.-');
hold on;
plot(t,imag(yn),'ro-');
xlabel('时间 (秒)');
ylabel('幅度');
title('10Hz 信号时域图');
legend(['实部';'虚部']);
grid on;
zoom on;