clc ; clear ; close all;
%% 参数
tar_num = 8;
freq_step = 8000;
rts_band  = 8000;
temperature_band = 1;
% temperature_band = -10:1:70;
temperature_len  = length(temperature_band);
down_size = 4 * temperature_len * tar_num;

%% 修正
power = zeros(1,tar_num);
% power(1) = 16.5  ;
% power(2) = 16  ;
% power(3) = 12  ;
% power(4) = 16.5 ;
% power(1) = -28.4  ;
% power(2) = -31.2  ;
% power(3) = -27.4  ;
% power(4) = -28.7 ;

%% corr
corr_power = power - min(power);

% code = corr_power / 0.125;
code = corr_power / 0.0625;
code = round(code);
code_copy = repmat(code,1,temperature_len);

code_out = [freq_step,rts_band,down_size,code_copy]';
%% Out File
file = 'table\rcs_cor.dat';
delete(file);
fid = fopen(file,'W');
fwrite(fid,code_out,"uint32");
fclose(fid);
