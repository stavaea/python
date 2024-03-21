function [data_return] = load_am_freq_table(rts,Filename)
% 包头	    Hard	    uint	0xA5A5A5A5
% 数据类型	Type	    uint	OxF00100FF
% 数据大小	DataSize	uint	126*4	       单位字节
% 通道号	ChannelNo	uint 		           1:表示通道 1
%                                              2:表示通道 2
% 文件数据	data	    uint*	0	           1-125 word:
% 包尾	    Tail	    uint	0xB5B5B5B5
% data_return = zeros(8,2);
%% 读取幅频修正表
Filename1 = strcat(Filename,'\AmpFreqTable1.dat');
fp=fopen(Filename1);
data=fread(fp,'uint32');
len1 = length(data);
len = floor(len1/250) - 1;
% temp = zeros(len,250);
for i = 1:len
    syspara = uint32(zeros(1,255));
    syspara(1)= hex2dec('A5A5A5A5');
    syspara(2)= hex2dec('F00100FF');
    syspara(3) = 251*4;%单位字节
    syspara(4) = 1;%通道号
    syspara(1,5:254)=data((i-1)*250+1:i*250);
    syspara(255)=hex2dec('B5B5B5B5');
    rts.write(syspara, 'uint32');
    pause(0.3);
    read_return(rts);
end
%% 组装命令
len2 = len1 - len*250;
syspara = uint32(zeros(1,len2+5));
syspara(1)=hex2dec('A5A5A5A5');
syspara(2)=hex2dec('F00100FF');
syspara(3) = (len2+1)*4;%单位字节
syspara(4) = 1;%通道号
syspara(1,5:len2+4)=data(len*250+1:end);
syspara(len2+5)=hex2dec('B5B5B5B5');
rts.write(syspara, 'uint32');

%% 等待返回数据
read_return(rts);
fclose(fp);
clear syspara;

% %% 发送文件2
% Filename2 = strcat(Filename,'\AmpFreqTable2.dat');
% fp=fopen(Filename2);
% data1=fread(fp,'uint32');
% len12 = length(data1);
% len_2 = floor(len12/250) - 1;
% % temp = zeros(len,250);
% for i = 1:len_2
%     syspara = uint32(zeros(1,255));
%     syspara(1)= hex2dec('A5A5A5A5');
%     syspara(2)= hex2dec('F00100FF');
%     syspara(3) = 250*4;%单位字节
%     syspara(4) = 1;%通道号
%     syspara(1,5:254)=data1((i-1)*250+1:i*250);
%     syspara(255)=hex2dec('B5B5B5B5');
%     fwrite(rts, syspara, 'uint32');
%     pause(0.3);
%     read_return(rts);
% end
% %% 组装命令
% len22 = len12 - len_2*250;
% syspara = uint32(zeros(1,len22+5));
% syspara(1)=hex2dec('A5A5A5A5');
% syspara(2)=hex2dec('F00100FF');
% syspara(3) = (len22)*4;%单位字节
% syspara(4) = 1;%通道号
% syspara(1,5:len22+4)=data1(len_2*250+1:end);
% syspara(len22+5)=hex2dec('B5B5B5B5');
% fwrite(rts, syspara, 'uint32');
%
% %% 等待返回数据
% data_return = read_return(rts);
% fclose(fp);