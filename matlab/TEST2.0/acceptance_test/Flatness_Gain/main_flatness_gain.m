% 该程序主要应用于模块的平坦度及增益测试
% 程序使用信号源83630B、频谱仪N9020A。
instrreset;
clc ; clear ; close all;
%% 参数配置
% 生产厂家：RS(冉思科技)、JL(杰联科技)等
manufacturer = 'RS';
% 波段：E、V、K、X波段
waveband     = 'E';
% 模块：Rf(射频模块)、Rm（调理模块）、Fcrm（二次变频与调理模块）
module       = 'Rf';
% 模块类型：Down（下变频模块）、Close（闭环）、Open（开环）、Up(上变频模块)
module_type  = 'Down';
% 编号：模块标注编号
module_numbeer = '202304001';
% 起始频率
fre_start            = 76000 ;
% 结束频率
fre_end              = 81000 ;
% 本振频率
fre_lo               = 11910;
% 测试点数
test_point           = 51   ;
% 连接使用衰减
connect_att          = 0    ;
% 线损
cable_att            = 2    ;
% 信号源输出功率
amp_set              = -5   ;
% 信号源GPIB(信号)
GPIB_83630B          = 'GPIB4::20::INSTR'                  ;
% 信号源GPIB(混频器本振)
GPIB_hp83712B        = 'GPIB4::20::INSTR'                  ;
% 频谱仪IP
ip_spec              = ['TCPIP0::','192.168.1.6','::INSTR'];
% 频谱仪点数
point                = 1001;
% 频谱仪功率参考
y_ref                = 20;
%% 保存文件名称
File_path            = '..\Data\';
File                 = strcat(File_path,manufacturer,'_',waveband,'_',module,'_',module_numbeer);
File_data            = strcat(File,'\',manufacturer,'_',waveband,'_',module,'_',module_type);
Creat_File(File); % 创建保存数据的文件夹
%% 信号源、频谱仪参数
mode_flag = strcmp(module_type,'Up');
fre_set              = linspace(fre_start,fre_end,test_point) ; % 生成测试频率点
[mult,spec_fre_set]  = fre_judge(waveband,module_type,module,fre_set,fre_lo);
y_ref     = 20;
point     = test_point;
spec_span = 0;
%% 连接信号源、频谱仪
keysight83630B = visa('agilent', GPIB_83630B);
fopen(keysight83630B);
N9020A       = visa('agilent',ip_spec);
set(N9020A,'InputBufferSize',60e4);
fopen(N9020A);
%% 信号源(信号)配置
fprintf(keysight83630B,'FREQuency:MULTiplier  %d',mult);
fprintf(keysight83630B,'FREQuency:MULTiplier:STATE ON');
fprintf(keysight83630B,'FREQuency %f MHz',fre_set(1));
fprintf(keysight83630B,'POWer %f dbm',amp_set);
fprintf(keysight83630B,'POWer:STATe ON');
%% 信号源(混频器本振)配置
if (mode_flag)
	fre_set_lo     = fre_set - 300;
	amp_set_lo = 10;
	hp83712B   = visa('agilent', GPIB_hp83712B);
	fopen(hp83712B);
	fprintf(hp83712B,'FREQuency:MULTiplier %d',mult);
	fprintf(hp83712B,'FREQuency %f MHz',fre_set_lo(1));
	fprintf(hp83712B,'POWer %f dbm',amp_set_lo);
	fprintf(hp83712B,':OUTPut ON');
end
%% 频谱仪配置
fprintf(N9020A,'SYST:PRES');
pause(1)
fprintf(N9020A,'FREQ:STAR %f MHz',min(spec_fre_set(1),spec_fre_set(end))-spec_span);pause(0.5)
fprintf(N9020A,'FREQ:STOP %f MHz',max(spec_fre_set(1),spec_fre_set(end))+spec_span);pause(0.5)
fprintf(N9020A,'SWE:POIN %d',point);
fprintf(N9020A,'DISP:WIND1:TRAC:Y:RLEV %f dBm',y_ref);
%% 采集数据
if (mode_flag)
    [trace] = coll_flatness_gain_up(keysight83630B,hp83712B,N9020A,fre_set_lo,fre_set);
    fprintf(hp83712B,':OUTPut OFF');
else
    [trace] = coll_flatness_gain(keysight83630B,N9020A,fre_set);
end
fprintf(keysight83630B,'POWer:STATe OFF');

%% 数据保存
clock1 = clock;
savefile = sprintf('%s_Flatness_Gain_%04d%02d%02d_%02d%02d%02.0f',File_data,clock1(1),clock1(2), ...
    clock1(3),clock1(4),clock1(5),clock1(6))
save(savefile,"trace","connect_att","cable_att","fre_set","spec_fre_set","mult","fre_lo",'File','File_data',"module_type","module","waveband","manufacturer");

instrreset
