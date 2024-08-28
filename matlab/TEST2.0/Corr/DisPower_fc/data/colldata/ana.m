clc ; clear ; close all;

file1  = '20240725_201204_Dis_Power_Corr.mat';
file2  = '20240725_214105_Dis_Power_Corr.mat';
file3  = '20240725_231013_Dis_Power_Corr.mat';
file4  = '20240726_003925_Dis_Power_Corr.mat';

data1  = load(file1);
data2  = load(file2);
data3  = load(file3);
data4  = load(file4);

error1 = data1.power - data2.power;
error2 = data2.power - data3.power;
error3 = data3.power - data4.power;
error4 = data4.power - data1.power;
