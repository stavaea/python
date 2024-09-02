%% Disconnect and delete all instrument objects
clc ; clear ; close all ; warning off
%% 参数配置
% start_freq      = 7600;
start_freq      = 4540;
% 信号结束频率
% stop_freq       = 9600;
stop_freq       = 9540;
% 频率步进
step_freq       = 50;
% RTS 瞬时带宽
rts_band        = 5000;
% RTS 信号起始频率(射频)
% start_freq_rf   = 76000;
start_freq_rf   = 76000;
% 下载数据大小
size_data       = 256*22*4 ;
% 温度步进
temperature     = -10:4:74 ;
%% 基础参数生成
freq            = start_freq:step_freq:stop_freq ;
att             = (0:0.5:127.5)'           ;%0:0.5:100
file_dca_err    = 'corr_table\dca_err.dat' ;
file_dca_cont   = 'corr_table\dca_cont.dat';

len_freq        = length(freq)             ;
len_temperature = length(temperature)      ;
len             = length(att)              ;

per             = 0.5                      ;
counter         = len_freq  ;
len_interp1     = 0:0.5:127.5;
%% 数据处理
for m = 1:len_temperature
    Filename = strcat('data\corr_data\dca_coll_',sprintf('%d.mat',temperature(m)));
    load(Filename);
    x1 = Att;
    interp_len = length(fre_set);
    % 数据归一化
    amp_meas_gyh = amp_meas - amp_meas(:,1);
    % 精度计算 向下取整
    interp_data= amp_meas_gyh;
    for interp_i = 1:interp_len
        interpdata(interp_i,:)= interp1(x1,interp_data(interp_i,:),att,'linear','extrap');
    end

    amp_meas_ceil =floor(interpdata / per );
%     amp_meas_ceil =floor(amp_meas_gyh / per );
    % 精度恢复
    amp_meas_ceil = amp_meas_ceil * per;
    amp_meas_ceil_ne = -1*amp_meas_ceil;
    % 误差计算 误差为负代表多衰减，误差为正代表少衰减
%     amp_error    = amp_meas_gyh - amp_meas_ceil;
    amp_error    = interpdata - amp_meas_ceil;
    % 查表
    att_code = 0:0.5:100;

    len_x  = length(att_code);

    [len_row,len_col] = size(amp_meas);

    amp_meas_contrast = zeros(counter,256);

    code_contrast     = zeros(counter,256);
    error_out         = zeros(counter,256);

%     error_out_new = zeros(counter,256);
%     code_contrast_new = zeros(counter,256);
%     for k = 1:1:counter
%         error_out_new(k,:) = interp1(amp_meas(k,:),error_out(k,:),len_interp1,'linear','extrap');
%         code_contrast_new(k,:) = interp1(amp_meas(k,:),code_contrast(k,:),len_interp1,'linear','extrap');
%     end

    for i = 1:len_row
        t = 0;
        for j = 1:len_x
            temp_code = find(amp_meas_ceil_ne(i,:) == t);
            if (isempty(temp_code))
                amp_meas_contrast(i,j) = amp_meas_contrast(i,j-1) +0.5 ;
                code_contrast(i,j)     = code_contrast    (i,j-1)      ;
                error_out(i,j)         = error_out        (i,j-1) +0.5 ;
            else
                len = length(temp_code);

                if (len == 1)
                    amp_meas_contrast(i,j) = amp_meas_ceil_ne(i,temp_code);
                    code_contrast(i,j)     = att(temp_code);
                    error_out(i,j)         = amp_error(i,temp_code);
                else
                    min_error = 999;
                    row = 0;
                    for s = 1:len
                        now_error = amp_error(i,temp_code(s)) + (t - amp_meas_ceil_ne(i,temp_code(s)));

                        if (min_error > now_error)
                            min_error = now_error;
                            row       = temp_code(s);
                        end
                    end
                    error_out(i,j) = amp_error(i,row) + (t - amp_meas_ceil_ne(i,row));
                    amp_meas_contrast(i,j) = amp_meas_ceil_ne(i,row);
                    code_contrast(i,j)     = att(row);
                end
            end
            t = t + 0.5;
        end
    end
%     code_contrast(:,65:67) = code_contrast(:,65:67)-1;
    mmmm = 1;
    for r = len_x+1:1:256
        error_out(:,r) = error_out(:,len_x) + mmmm*0.5;
        code_contrast(:,r)  = code_contrast(:,len_x) ;
        mmmm = mmmm + 1;
    end

%     error_out_new = zeros(counter,256);
%     code_contrast_new = zeros(counter,256);
%     for k = 1:1:counter
%         error_out_new(k,:) = interp1(amp_meas_contrast(k,:),error_out(k,:),len_interp1,'linear','extrap');
%         code_contrast_new(k,:) = interp1(amp_meas_contrast(k,:),code_contrast(k,:),len_interp1,'linear','extrap');
%     end
%     error(:,:,m) = error_out_new;
%     code (:,:,m)  = code_contrast_new;
    error(:,:,m) = error_out;
    code (:,:,m)  = code_contrast;
end

%% Dat
error = error / 0.125;
error = round(error);
code  = code  / 0.125;
len_freq_loc = 1;
len_att        = 256;
cnt1 = len_temperature*len_att;

for i = 1:len_freq_loc
    for j = 1:len_freq
        col = (i-1)*len_freq + j;
        for k = 1:len_temperature
            point_start = ((i-1)*len_freq*len_temperature*len_att) + ...
            ((j-1)*len_temperature*len_att) + ((k-1)*len_att) + 1;
            point_end   = ((i-1)*len_freq*len_temperature*len_att) + ...
            ((j-1)*len_temperature*len_att) + (k*len_att);
            code_dat(point_start:point_end) = code (col,:,k);
            erro_dat(point_start:point_end) = error(col,:,k);
        end
    end
end
%% dat Out
erro_dat             = [ step_freq , rts_band , size_data , erro_dat];
code_dat             = [ step_freq , rts_band , size_data , code_dat];
delete(file_dca_err);
fid = fopen(file_dca_err,'w');
fwrite(fid,erro_dat(1:end),'uint32');
fclose(fid);

delete(file_dca_cont);
fid = fopen(file_dca_cont,'w');
fwrite(fid,code_dat(1:end),'uint32');
fclose(fid);