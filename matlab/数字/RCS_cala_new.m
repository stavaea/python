close all
clc
clear
c = 3e8;
f=76.8e9;
rcs_dbsm = 10;%dbm与1w的转换
lamda = c/f;
R_RTS = [0.5 1.5 2 3.5 8 10];
R = 0:0.1:70;
GRTS = 10;
Kd  = 34;
Ku = -9;
K = Kd + Ku;
R_IF_P_1O = -17;%接收射频头中频输出P-1功率点
R_RF_P_1I = R_IF_P_1O - Kd;%接收射频头射频输入P-1功率点

%理论上可模拟的最大RCS
for i=1:length(R_RTS)
    RCS(:,i) = 10*log10( lamda*lamda/4/pi)+40*log10(R/R_RTS(i))+K+2*GRTS;
end
figure('color', [1 1 1]);%%%去除画图的灰色背景
plot(R,RCS);
set(gca,'LineWidth',1);
grid on;
% ylim([-60 40])
xlabel('Target Distance (m)','FontSize',10);ylabel('Maximum RCS (dBsm)','FontSize',10)
legend('Air Gap=0.5m','Air Gap=1m','Air Gap=2m','Air Gap=3.5m','Air Gap=8m','Air Gap=10m')
set(gcf,'position',[360 291 471 327]);
% copygraphics(gcf);%%%拷贝matlab画图的原图，2021版可用

%雷达EIRP约束条件
for i=1:length(R_RTS)
    RadarEIRP(:,i) = R_RF_P_1I - GRTS - 10*log10( lamda*lamda/(4*pi*R_RTS(i)).^2);
end
figure('color', [1 1 1]);%%%去除画图的灰色背景
plot(R_RTS,RadarEIRP);
set(gca,'LineWidth',1);
grid on;
% ylim([-60 40])
xlabel('Air Gap (m)','FontSize',10);ylabel('Maximum radar EIRP (dBm)','FontSize',10)
set(gcf,'position',[360 291 471 327]);




