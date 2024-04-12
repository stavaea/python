% data = load('D:\work\脚本\Test2.0\Corr\Att_corr\data\ver_data\20240410_091423_Ver_coll.mat');
data1 = load('D:\work\脚本\Test2.0\Corr\Att_corr\data\ver_data\20240410_183413_Ver_coll_nc.mat');
data2 = load('D:\work\脚本\Test2.0\Corr\Att_corr\data\ver_data\20240411_102630_Ver_coll.mat');

x = data1.Att;
% y = amp_meas;
y = data1.amp_meas - data1.amp_meas(1) + x;
subplot(121);
plot(x,y,'LineWidth',1.5);
xlabel('Set Att (dB)','FontSize',15);ylabel('Att Error (dB)','FontSize',15);
grid minor;

x1 = data2.Att;
% y = amp_meas;
y1 = data2.amp_meas - data2.amp_meas(1) + x1;
subplot(122);
plot(x1,y1,'LineWidth',1.5);
xlabel('Set Att (dB)','FontSize',15);ylabel('Att Error (dB)','FontSize',15);
grid minor;