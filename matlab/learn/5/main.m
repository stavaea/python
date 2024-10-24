% 某77GHz雷达发射雷达线性调频信号，中心频率为77.075GHz，带宽150MHz，
% 发射信号时间宽度为100us，采样率fs=2MHz，光速为3e8m/s。
% 天线配置为1发2收，采用相位干涉仪的测角体制，两个接收天线之间的间距d为波长的一半，
% 发射天线的坐标就是原点，也就是两个接收天线的中心。目标位置在法线方向30度，距离为100m处。
% 目标速度为15m/s，方向为沿着y轴负方向（注意并不是径向速度），目标几何场景设置如下：
%
% 请仿真该场景下，目标运动3秒钟的过程。每个周期100us，每帧积累100个脉冲（FFT点数设计为256），
% 则每帧时间为10ms，3秒内有300帧回波数据，在每帧数据的回波上叠加一个功率为1的复高斯白噪声，
% 目标回波的信噪比为0dB（通过回波幅度来设置），对回波进行处理，并绘制出二维路面的运行轨迹结果。
% 提示：
% 本次作业相当于在作业8的基础上，动态运行起来，可以对作业8进行修改，
% 变成一个可以调用的函数，输入为目标的距离、速度、角度，输出为目标的距离、速度和角度，
% 然后在主函数随着仿真进程，目标参数不断更新，调用这个雷达函数就可以获得雷达的测量结果。


clc; clear all; close all;

N=300;
n=0:1:N-1;
R0=100;
Azimuth=30;
Rx=R0*sind(Azimuth);
Ry=R0*cosd(Azimuth);
T1=100e-6;

rx1(i+1)=Rx;
Ry=ry-v*i*Tnn;
ry1(i+1)=Ry;
Azimuth=90-atan(Ry/Rx)*180/pi;
R0=sqrt(Ry^2+Rx^2);
rxx(i+1)=target_range*sind(angle_measure);
ryy(i+1)=target_range*cosd(angle_measure);
plot(rxx,ryy,'.')
title('叠加噪声探测目标运行轨迹');
xlim([0 60]);
ylim([0 60]);
grid on;zoom on;
hold on;
plot(rx1,ry1,'r.-');
title('理论目标运行轨迹');
xlabel('Rx/m');ylabel('Ry/m');
xlim([0 60]);ylim([0 90]);
grid on;zoom on;