% DataFile_path = 'D:\work\脚本\Test2.0\Corr\am_freq_corr\data\back_up\20240304_183818_RTS7681D_20_SN2402004_平坦度指标测试';
% DataFile_path = 'D:\work\脚本\Test2.0\Corr\am_freq_corr\data\back_up\20240304_184106_RTS7681D_20_SN2402004_平坦度指标测试';
DataFile_path = 'D:\work\脚本\Test2.0\Corr\am_freq_corr\data\back_up\20240304_184325_RTS7681D_20_SN2402004_平坦度指标测试';


%% 加载数据
data = load(DataFile_path);
% x=linspace(7600,9600,20001);
x=linspace(7.6e9/1e6,9.6e9/1e6,20001);
y=data.trace;
y1=data.trace_corr;


subplot(121)
plot(x,y);
title(sprintf('修正前平坦度为：%3.3fdB',range(y)),FontSize=15);
xlabel('Freq (MHZ)',FontSize=15);
ylabel('Power (dB)',FontSize=15);
grid minor

subplot(122)
plot(x,y1);
title(sprintf('修正后平坦度为：%3.3fdB',range(y1)),FontSize=15);
xlabel('Freq (MHZ)',FontSize=15);
ylabel('Power (dB)',FontSize=15);
grid minor