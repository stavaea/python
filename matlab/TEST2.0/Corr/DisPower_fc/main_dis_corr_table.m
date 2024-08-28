% clc ; clear ; close all;
%% parameter
freq            = 9100                     ;
temperature     = 1                        ;
freq_loc        = 1                        ;
% dis             = 0:0.2:61.6250          ;
dis             =  0:0.128:500             ;

len_freq        = length(freq)             ;
len_temperature = length(temperature)      ;
len_freq_loc    = length(freq_loc)         ;
len_dis         = length(dis)              ;

%% Load Data
filepath = "data\";
corr = zeros(len_dis,len_freq*len_freq_loc,len_temperature);
for i = 1:len_temperature
    data = load(strcat(filepath,sprintf('Dis_Power_Corr_%d',temperature(i))));
    corr_data  = data.power          ;
    corr_data  = corr_data - 100        ;
    corr_stand = min(corr_data)         ;
    corr_power = corr_data - corr_stand ;
%     for j = 1:length(dis)
%         if(corr_power(i) > 30)
%             corr_power(i) = 30;
%     	end
%     end
    corr_power = corr_power * 16        ;
    corr_power = round(corr_power)      ;
% 	corr_power(1:10) = 0                ;
    corr(:,:,i) = corr_power        ;
end
%% 整合数据
data_out = zeros(1,len_dis*len_freq*len_freq_loc*len_temperature)';
file_dis_power_table = 'DisPow_cor.dat';
% file_dis_power_table = 'DisPow_cor_init.dat';
% file_dis_power_table = 'DisPow_cor_test.dat';
%% 整合数据
% data_out_d = zeros(1,len_dis*len_freq*len_freq_loc*len_temperature)';
data_out_d = corr;
% freq_loc_step   = 5000  ;
% freq_loc_min    = 76000 ;
% freq_step       = 5000  ;
% size_data       = len_dis*4;

freq_loc_step   = 2000  ;
freq_loc_min    = 23000 ;
freq_step       = 2000  ;
size_data       = 3938*4;

data_out_d = [freq_loc_step ; freq_loc_min ; freq_step ; size_data ; data_out_d];
fid = fopen(file_dis_power_table,'W');
fwrite(fid,data_out_d(1:length(data_out_d)),"uint32");
fclose(fid);

%% remind
disp(file_dis_power_table);
disp ('文件生成成功');
% run main_dis_ver.m
