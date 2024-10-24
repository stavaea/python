clc; clear; close all;

% t = 0:0.01:1;
% figure;
% plot(t,sin(2*pi*2*t),'b.-');
% hold on;
% plot(t,sin(2*pi*4*t),'ro-');
% xlabel('时间/s');
% ylabel('幅度');
% title('信号时域图')
% legend('f=2Hz', 'f=4Hz');
% grid on;
% zoom on;




%单图--循环
% fs=1000;
% ts=1/fs;
% t=0.1:ts:1;
% figure;
% f=1:50;
% for i = length(f)
%     y=exp(j*2*pi*f(i)*t);
%     plot(t,real(y),'b.-',t,imag(y),'r.-');
%     xlabel('时间/s');ylabel('幅度');
%     title(sprintf('复正弦信号波,频率为: %d Hz',f(i)));
%     legend('real','imag');
%     text(0.5,0.5,'hi');
%     hold on;
%     pause(0.1);
% end
% grid on;
% zoom on;

%多图
% fs=1000;
% ts=1/fs;
% t=0.1:ts:1;
% figure;
% f=1:50;
% for i = length(f)
%     y=exp(j*2*pi*f(i)*t);
%     subplot(2,1,1);plot(t,real(y),'b.-');
%     subplot(2,1,2);plot(t,imag(y),'r.-');
%     xlabel('时间/s');ylabel('幅度');
%     title(sprintf('复正弦信号波,频率为: %d Hz',f(i)));
% end

%三维
% t=0:pi/50:10*pi;
% plot3(sin(t), cos(t), t);
% [x,y]=meshgrid(1:5);
% z=x+y;
% plot3(x,y,z);
% [x,y]=meshgrid(-2:0.1:2);
% z=x*exp(-x.^4-y.^4);
% plot3(x,y,z);
%
%
% [x,y]=meshgrid(-8:0.5:8);
% z=sqrt(x.^2+y.^2);
% z1=sin(z)./z;
% mesh(x,y,z)
% mesh(x,y,z1)



%布朗运动
% n=20;s=0.02;
% x=rand(n,1)-0.5;y=rand(n,1)-0.5;
% h=plot(x,y,'.');
% axis([-1 1 -1 1]);
% axis square;
% grid off;
% set(h,'erasemode','xor','markersize',18);
% while 1
%     x=x+s*randn(n,1);
%     y=y+s*randn(n,1);
%     set(h,'xdata','ydata',y);
%     drawnow;
% end





% f=10;
% fs=100;
% ts=1/fs;
% T=1;
% t=0:ts:T-ts;

% s=exp(j*2*pi*f*t);
% figure;
% N=10*length(s);
% fft_s = fft(s, N);
% fft_s_db=20*log10(fft_s/max(fft_s));
% f_index=linspace(0,fs-fs/N,N);
% % plot(f_index,abs(fft_s),'.-');
% plot(f_index,real(fft_s),'.-');
% hold on;
% plot(f_index,imag(fft_s),'r.-');
% legend('1','2');
% xlabel('频率/Hz');
% ylabel('幅度');
% grid on;
% zoom on;

% f=40;fs=100;ts=1/fs;T=1;t=0:ts:T-ts;
% s=exp(j*2*pi*f*t);
% N=fs*T;
% figure;
% plot(t,s,'.-');
% fx=linspace(0,fs-fs/N,N);
%
% fft_s=abs(fft(s));
% figure;
% plot(fx,fft_s,'.-');
%
% beishu=10;
% N1=beishu*N;
% fft_s1=abs(fft(s,N1));
% fx1=linspace(0,fs-fs/N1,N1);
% figure;
% plot(fx1,fft_s1,'.-');
% grid on;
% zoom on;
% % fft(a,10*length(a))=fft([a zeros(1,9*length(a))]);
%
% fft_s2=abs(fft([s zeros(1,9*length(s))]));
% figure;
% plot(fx1,fft_s2,'.-');
% %以dB的方式
% fft_s2_dB=20*log10(fft_s2/max(fft_s2));%功率，幅度用10*log10
% figure;
% plot(fx1,fft_s2_dB,'.-');
% ylim([-60 10]);


% 1.利用y=exp(j*2*pi*f*t)产生一个频率为10Hz的复信号正弦波，幅度为1,采样率为20Hz，采样时长为1s。
% a) 做200点DFT，并画出该信号的归一化频谱图，自动测量出3dB频谱宽度，显示在标题中。
% b) 做20000点DFT，并画出该信号的归一化频谱图，与200点DFT画在一起，用legend标识，观察是否提高频率分辨力。
% c) 在b)基础上，将采样率提高到40Hz，画出归一化频谱图，对比采样率在20Hz和40Hz下两条曲线的区别。
% d)在b)基础上，将采样时长设为2s，画出不同采样时间长度下两个归一化频谱图曲线的区别。
% 2.在题目1b)的基础上，增加一个信号频率为10.5Hz的复信号正弦波，还有一个信号频率为15Hz的复信号正弦波，
% 幅度均为1，其余条件不变，观察频谱是否可以看到3个信号峰值。
% 如不能，请解释什么原因?怎样做信号处理才能看到3个信号峰值。
% 给出措施和实验结果，以及实验结论。
% f1=10;f2=10.5;f3=15;fs=40;T=2;f_span3dB_theory=1/T*0.886;t=0:1/fs:T-1/fs;







% f=1:50;
%
% % f=0:-1:-50;
% fs=30;
% ts=1/fs;
% T=1;
% t=0:ts:T-ts;
%
% % s=exp(j*2*pi*f*t);
% figure;
%
% for i =1:length(f)
%     s=exp(j*2*pi*f(i)*t);
%     N=length(s);
%     fft_s=abs(fft(s));
%     f_index=linspace(0,fs-fs/N,N);
%     plot(f_index,fft_s,'.-');
%     xlabel('频率/Hz');
%     ylabel('幅度');
%     title(sprintf('信号的频率：%d Hz',f(i)));%3.1f
%     ylim([0 30]);
% %     zoom on;
%     grid on;
%     pause(0.2);
% end



f=10;
% f=0:-1:-50;
fs=100;
ts=1/fs;
T=1;
t=0:ts:T-ts;

y=exp(j*2*pi*f*t);
s=cos(2*pi*f*t);

N = 10;

N1=N*length(y);
fft_s1=abs(fft(y, N1));
fx1 = linspace(0,fs-fs/N1,N1);
ffs1_dB=20*log10(fft_s1/max(fft_s1));

N2=N*length(s);
fft_s2=abs(fft(s, N2));
fx2 = linspace(0,fs-fs/N2,N2);
ffs2_dB=20*log10(fft_s2/max(fft_s1));

figure;
plot(fx1,ffs1_dB,'g.-');
hold on;
plot(fx2,ffs2_dB,'r.-');

title('频谱图')
xlabel('Hz');
ylabel('dB');
legend('y','s');
zoom on;grid on;
