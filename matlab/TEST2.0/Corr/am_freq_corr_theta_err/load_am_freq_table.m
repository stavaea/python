function [data_return] = load_am_freq_table(rts,amp_freq_data)
% 包头	    Hard	    uint	0xA5A5A5A5
% 数据类型	Type	    uint	OxF00100FF
% 数据大小	DataSize	uint	126*4	       单位字节
% 通道号	ChannelNo	uint 		           1:表示通道 1
%                                              2:表示通道 2
% 文件数据	data	    uint*	0	           1-125 word:
% 包尾	    Tail	    uint	0xB5B5B5B5
% data_return = zeros(8,2);
%% 下载修正表
for j=1:ceil(length(amp_freq_data)/250)
    if j>length(amp_freq_data)/250
        len_amp_freq_data=length(amp_freq_data)-250*(j-1);
    else
        len_amp_freq_data=250;
    end
    syspara     = zeros(1,len_amp_freq_data+5);
    syspara(1)	= hex2dec('A5A5A5A5');
    syspara(2)	= hex2dec('F00100FF');
    syspara(3)	= 4*len_amp_freq_data+4;      %数据大小
    syspara(4)	= 1;        %通道号
    for i=1:len_amp_freq_data
        syspara(i+4)=amp_freq_data(i+250*(j-1));
    end
    syspara(i+5) = hex2dec('B5B5B5B5');

    fwrite(rts,syspara,'uint32');
    data_return = read_return(rts);
end