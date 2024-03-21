% 该程序用于生成初始化的衰减对照表、误差表
clc ; clear ; close all ; warning off
%% 参数配置
% 信号起始频率
start_freq      = 7600;
% 信号结束频率
stop_freq       = 9600;
% 频率步进
step_freq       = 50  ;
% RTS 瞬时带宽
rts_band        = 2000;
% RTS 信号起始频率(射频)
start_freq_rf   = 76000;
% 下载数据大小
size_data       = 256*22*4 ;
% 温度步进
temperature     = -10:4:74 ;
%% 生成误差表数据
file_dca_err    = 'Initial_table\dca_err.dat' ;
freq            = start_freq:step_freq:stop_freq ;
att             = (0:0.5:127.5)'             ;

len_freq        = length(freq)             ;
len_temperature = length(temperature)      ;
len             = length(att)              ;

data_out_d      = zeros(len_temperature*len_freq*len,1);
data_out        = [step_freq ; rts_band ; size_data ; data_out_d];
delete(file_dca_err);
fid = fopen(file_dca_err,'w');
fwrite(fid,data_out(1:end),'uint32');
fclose(fid);

%% 生成对照表数据
file_dca_cont   = 'Initial_table\dca_cont.dat';

dca_cont             = (0:0.5:127.5)/0.125     ;
dca_contrast         = repmat(dca_cont,1,len_freq);
dca_contrast_reshape = reshape(dca_contrast,len_freq*len,1);
dca_contrast_temp    = repmat(dca_contrast_reshape,1,len_temperature);
dca_contrast_temp_reshape = reshape(dca_contrast_temp,len_freq* len * len_temperature,1);

data_out             = [step_freq ; rts_band ; size_data ; dca_contrast_temp_reshape];

delete(file_dca_cont);
fid = fopen(file_dca_cont,'w');
fwrite(fid,data_out(1:end),'uint32');
fclose(fid);

% t1 = zeros(22*256,1);
% for i = 1:length(t1)
%     t1(i) = i;
% end
% for i = 1:41
%     t(:,i) = t1 + i;
% end
% dca_contrast_temp_reshape = reshape(t,22*256*41,1);