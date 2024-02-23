% 自动测试相噪程函数
% Name：频谱仪name
% spec_fre_set：测试相噪频率点
% spec_fre_set_diff：测试多少相噪

function [y1,y2,phasenoise,phasenoise_trace,phasenoise_trace_x]=get_phasenoise(N9020A,fre_set,spec_fre_set_diff,point)

%% 调整频谱仪坐标系
fprintf(N9020A,'FREQ:STAR %f MHz',fre_set);  % 将marker1设置为中心频率
pause(0.3);
fprintf(N9020A,'CALC:MARK1:MAX');%
pause(0.3);
fprintf(N9020A,'CALC:MARK1:Y?');
ref_y = str2double(fscanf(N9020A));
pause(0.3);
fprintf(N9020A,'DISP:WIND1:TRAC:Y:RLEV %f dBm',ref_y+5);   % 设置Y_cale
pause(0.3)

%% 测试相噪
phasenoise = zeros(1,length(spec_fre_set_diff));
y2 = zeros(1,length(spec_fre_set_diff));
y1 = zeros(1,length(spec_fre_set_diff));
phasenoise_trace_x = zeros(1,length(spec_fre_set_diff)*90+11);
phasenoise_trace   = zeros(1,length(spec_fre_set_diff)*90+11);
stop_freq = fre_set;
cnt_trace = 1;
for i = 1 : length(spec_fre_set_diff)
    % 频谱仪参数设置
    fprintf(N9020A,'FREQ:STOP %f MHz',fre_set+(spec_fre_set_diff(i)*10)/1e3);% X轴范围
    fprintf(N9020A,'BAND %d KHZ',spec_fre_set_diff(i)/500);% RBW
    fprintf(N9020A,'BAND:VID %d KHZ',spec_fre_set_diff(i)/1000);% RBW

    % 获取最高点坐标
    pause(0.5);
    fprintf(N9020A,'CALC:MARK1:MAX');
    pause(0.3);
    fprintf(N9020A,'CALC:MARK1:Y?');
    y1(i) = str2double(fscanf(N9020A));

    % 开启Marker noise
    fprintf(N9020A,'CALC:MARK1:FUNC NOIS');
    pause(6);
    fprintf(N9020A,'CALC:MARK1:FUNC:BAND:SPAN:AUTO ON');

    % 下发相噪点
    pause(0.5);
    phasenoise_x = fre_set+spec_fre_set_diff(i)/1000;
    fprintf(N9020A,'CALC:MARK1:X %f MHz',phasenoise_x);
    pause(1)

    % 获取marker 坐标
    fprintf(N9020A,'CALC:MARK1:Y?');
    y2(i) = str2double(fscanf(N9020A));
    pause(0.3);

    % 获取多点相噪
    pause(1)
    while 1
        phasenoise_trace_x(1,cnt_trace) = (stop_freq - fre_set)*1e6;
        fprintf(N9020A,'CALC:MARK1:X %f MHz',stop_freq);
%         pause(0.3)
        fprintf(N9020A,'CALC:MARK1:Y?');
        phasenoise_trace(1,cnt_trace) = str2double(fscanf(N9020A))-y1(i);

        stop_freq = stop_freq + (spec_fre_set_diff(i)*10)/1e3/100;


        if stop_freq >= fre_set+(spec_fre_set_diff(i)*10)/1e3
            stop_freq = stop_freq - (spec_fre_set_diff(i)*10)/1e3/100;
            break;
        end
        cnt_trace = cnt_trace + 1;
    end
    % 关闭marker noise
    fprintf(N9020A,'CALC:MARK:FUNC OFF');
    % 获取相噪
    phasenoise(i) = y2(i) - y1(i);
end