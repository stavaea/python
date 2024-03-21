% 该程序主要应用于自闭环杂散测试、接收射频模块的杂散测试
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
% 模块类型：Down（下变频模块）、Close（闭环）、Open（开环）
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
test_point           = 11   ;
% 连接使用衰减
connect_att          = 30   ;
% 线损
cable_att            = 2    ;
% 信号源输出功率
amp_set              = -5   ;
% 信号源GPIB
GPIB_83630B          = 'GPIB4::20::INSTR'                  ;
% 频谱仪IP
ip_spec              = ['TCPIP0::','192.168.1.6','::INSTR'];

%% 保存文件名称
File_path            = '..\Data\';
File                 = strcat(File_path,manufacturer,'_',waveband,'_',module,'_',module_numbeer);
File_data            = strcat(File,'\',manufacturer,'_',waveband,'_',module,'_',module_type);
Creat_File(File); % 创建保存数据的文件夹
%% 信号源、频谱仪参数
fre_set              = linspace(fre_start,fre_end,test_point) ; % 生成测试频率点
[mult,spec_fre_set]  = fre_judge(waveband,module_type,module,fre_set,fre_lo);
y_ref   = 20;
point   = 1001;
spec_span = 0;
%% 连接信号源、频谱仪
keysight83630B = visa('agilent', GPIB_83630B);
fopen(keysight83630B);
N9020A       = visa('agilent',ip_spec);
set(N9020A,'InputBufferSize',60e4);
fopen(N9020A);
%% 信号源配置
fprintf(keysight83630B,'FREQuency %f MHz',fre_set(1));
fprintf(keysight83630B,'POWer %f dbm',amp_set);
fprintf(keysight83630B,'POWer:STATe ON');
%% 频谱仪配置
fprintf(N9020A,'SYST:PRES');
pause(1)
fprintf(N9020A,'FREQ:STAR %f MHz',min(spec_fre_set(1),spec_fre_set(end))-spec_span);pause(1)
fprintf(N9020A,'FREQ:STOP %f MHz',max(spec_fre_set(1),spec_fre_set(end))+spec_span);pause(1)
fprintf(N9020A,'SWE:POIN %d',point);
fprintf(N9020A,'DISP:WIND1:TRAC:Y:RLEV %f dBm',y_ref);
%% 采集数据
[fre_meas, amp_meas, amp_meas1, spurious,trace] = ...
coll_spurious_data(keysight83630B,N9020A,fre_set,spec_fre_set,point,connect_att,cable_att,y_ref,spec_span);
fprintf(keysight83630B,'POWer:STATe OFF');
%% 数据保存
clock1 = clock;
savefile = sprintf('%s_Spurious_%04d%02d%02d_%02d%02d%02.0f',File_data,clock1(1),clock1(2), ...
    clock1(3),clock1(4),clock1(5),clock1(6))
save(savefile,'fre_meas','amp_meas',"amp_meas1","spurious","trace","connect_att","cable_att","fre_set","spec_fre_set","mult","fre_lo",'File','File_data',"module_type","module","waveband","manufacturer");

instrreset
