clc; clear all; close all;

data = load('20231216_173022_ubw速度指标测试.mat');
v = data.speed;
temp_speed1 = v(1:10:1001);
temp_speed2 = v(1801:10:2801);
speed_range = [temp_speed1 v(1002:1800) temp_speed2 v(2802:end)];
x11=speed_range;
jd_speed1 = v(1:1001);
jd_speed2 = v(1801:2801);
% x2=[jd_speed1 jd_speed2];

fre=data.fre_meas;
temp_freq1 = fre(1:10:1001);
temp_freq2 = fre(1801:10:2801);
speed_range_freq = [temp_freq1 fre(1002:1800) temp_freq2 fre(2802:end)];
y1=speed_range_freq;
jd_freq1 = fre(1:1001);
jd_freq2 = fre(1801:2801);
% y2=[jd_freq1 jd_freq2] ;

fre_set = 2900;
fd = 2*x11*fre_set*1e6/299792458;
fd1 = y1-fre_set;
err = y1-(fre_set*1e6+fd);  %fd = 2*fre_set/299792458;
% f_err = fd1-fd;
err_v=(err*299792458)/(2*fre_set);
% err_v = (299792458*err)/(2*fre_set);  %v=(299792458*fd)/2;
err_v_1 = err_v/1e6;
plot(x11,err_v_1)

% figure;
% fd1 = 2*jd_speed1*fre_set*1e6/299792458;
% % fd1 = y1-fre_set;
% err1 = jd_freq1-(fre_set*1e6+fd1);  %fd = 2*fre_set/299792458;
% % f_err = fd1-fd;
% err_v1=(err1*299792458)/(2*fre_set);
% % err_v = (299792458*err)/(2*fre_set);  %v=(299792458*fd)/2;
% err_v_2 = err_v1/1e6;
% plot(jd_speed1,err_v_2)
%
%
% figure;
% fd2 = 2*jd_speed2*fre_set*1e6/299792458;
% % fd1 = y1-fre_set;
% err2 = jd_freq2-(fre_set*1e6+fd2);  %fd = 2*fre_set/299792458;
% % f_err = fd1-fd;
% err_v2=(err2*299792458)/(2*fre_set);
% % err_v = (299792458*err)/(2*fre_set);  %v=(299792458*fd)/2;
% err_v_3 = err_v2/1e6;
% plot(jd_speed2,err_v_3)
xlabel('Set Range (m/s)','FontSize',20);
ylabel('Speed Error (m/s)','FontSize',20);
title(sprintf('Speed Error Jitter Range:%3.3f m/s',range(err_v_1)),'FontSize',20);
xlim([99 1501])
xticks([100 200 300 400 500 600 700 800 900 1000 1100 1200 1300 1400 1500])
% axis tight;
% ylim([-5 7])
% xticks('auto')
minn = min(err_v_1);
maxx = max(err_v_1);
grid on ; hold on;
x1 = yline(maxx);
x1.LineWidth = 1.5;
x1.FontSize = 10;
x1.Color = 'black';
x1.LineStyle = '-.';
x1.Label = sprintf('Max Speed Error %.5f m/s',maxx);
x1.LabelHorizontalAlignment = 'left';
x1.LabelVerticalAlignment = 'top';
x2 = yline(minn);
x2.LineWidth = 1.5;
x2.FontSize = 10;
x2.Color = 'black';
x2.LineStyle = '-.';
x2.Label = sprintf('Min Speed Error %.5f m/s',minn);
x2.LabelHorizontalAlignment = 'left';
x2.LabelVerticalAlignment = 'bottom';

% subplot(1,2,1);plot(x1,err_v_1)
% subplot(1,2,2);plot(x2,err_v_2)
