close all;clear;clc;
f = 10;
fs=2500;
filename='D:/csv/iladata_corr55.csv';

srow = 1;  %0代表第一行，2代表第三行
scol = 3;  %第4列
data=csvread(filename,srow,scol);

data1_im=data(:,1:8)';
data1_re=data(:,9:16)';

% data1_im = data1_im - mean(data1_re);
% data1_re = data1_re - mean(data1_re);


data2_im=reshape(data1_im,1,[]);
data2_re=reshape(data1_re,1,[]);

data3 = data2_re + 1i * data2_im;

f1=linspace(-fs/2,fs/2,length(data3));
df1=fftshift(fft(data3));
figure(2);plot(data2_re);hold on;plot(data2_im);title('时域图');
figure(3);plot(f1,20*log10(abs(df1)/max(abs(df1))));title('data1频谱图');


%
% f1=linspace(-fs/2,fs/2,length(data1_r));
% df1=fftshift(fft(data1_r));
% [mamp1,index1] = max(abs(df1));
% ph1 = angle(df1(index1));
%
% f2=linspace(-fs/2,fs/2,length(data2_r));
% df2=fftshift(fft(data2_r));
% [mamp2,index2] = max(abs(df2));
% ph2 = angle(df2(index2));
%
% ph = ph1 - ph2 + 2*pi
% t = ph*1000/f/(pi*2)
%
% figure(1);plot(data1_r);hold on;plot(data2_r);title('时域图');
% figure(2);plot(f1,20*log10(abs(df1)/max(abs(df1))));title('data1频谱图');