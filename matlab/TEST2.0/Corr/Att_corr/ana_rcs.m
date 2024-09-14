clc ; clear ; close all ; warning off

DataFile_path = '..\Data\RTS7681FS_50\SN_243302\20240914_111245_距离RCS稳定性测试';
data = load(DataFile_path);

power = data.power(1:1461);
len_power = length(power);
down_temp = data.down_temp;
len_temp = length(down_temp);

temp = zeros(1,len_temp);
rcs_35 = zeros(1,len_temp);
rcs_36 = zeros(1,len_temp);
rcs_37 = zeros(1,len_temp);
rcs_38 = zeros(1,len_temp);
rcs_39 = zeros(1,len_temp);
rcs_40 = zeros(1,len_temp);
rcs_41 = zeros(1,len_temp);
rcs_42 = zeros(1,len_temp);
rcs_43 = zeros(1,len_temp);
rcs_44 = zeros(1,len_temp);
rcs_45 = zeros(1,len_temp);

for i = 1:len_temp
    if down_temp(i) == 35
        rcs_35(i) = power(i);
    end
    if down_temp(i) == 36
        rcs_36(i) = power(i);
%         rcs_36{down_temp(i)}{end+1} = power(i);
    end
    if down_temp(i) == 37
        rcs_37(i) = power(i);
    end
    if down_temp(i) == 38
        rcs_38(i) = power(i);
    end
    if down_temp(i) == 39
        rcs_39(i) = power(i);
    end
    if down_temp(i) == 40
        rcs_40(i) = power(i);
    end
    if down_temp(i) == 41
        rcs_41(i) = power(i);
    end
    if down_temp(i) == 42
        rcs_42(i) = power(i);
    end
    if down_temp(i) == 43
        rcs_43(i) = power(i);
    end
    if down_temp(i) == 44
        rcs_44(i) = power(i);
    end
    if down_temp(i) == 45
        rcs_45(i) = power(i);
    end
end

avg_34 = mean(rcs_34)
avg_35 = mean(rcs_35)
avg_36 = mean(rcs_36)