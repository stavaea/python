
test_point =11;

waveband     = 'E';
% 模块：Rf(射频模块)、Rm（调理模块）、Fcrm（二次变频与调理模块）
module       = 'Rf';
% 模块类型：Down（下变频模块）、Close（闭环）、Open（开环）
module_type  = 'Down';
% 本振频率
fre_lo               = 11910;
fre_set              = linspace(76000,81000,test_point) ; % 生成测试频率点
[mult,spec_fre_set]  = fre_judge(waveband,module_type,module,fre_set,fre_lo);

waveband     = 'E';
% 模块：Rf(射频模块)、Rm（调理模块）、Fcrm（二次变频与调理模块）
module       = 'Fcrm';
% 模块类型：Down（下变频模块）、Close（闭环）、Open（开环）
module_type  = 'Down';
% 本振频率
fre_lo               = 9840;
fre_set              = linspace(7600,9600,test_point) ; % 生成测试频率点
[mult,spec_fre_set]  = fre_judge(waveband,module_type,module,fre_set,fre_lo);

waveband     = 'E';
% 模块：Rf(射频模块)、Rm（调理模块）、Fcrm（二次变频与调理模块）
module       = 'Rm';
% 模块类型：Down（下变频模块）、Close（闭环）、Open（开环）
module_type  = 'Down';
% 本振频率
fre_lo               = 11910;
fre_set              = linspace(4540,9540,test_point) ; % 生成测试频率点
[mult,spec_fre_set]  = fre_judge(waveband,module_type,module,fre_set,fre_lo);

waveband     = 'V';
% 模块：Rf(射频模块)、Rm（调理模块）、Fcrm（二次变频与调理模块）
module       = 'Rf';
% 模块类型：Down（下变频模块）、Close（闭环）、Open（开环）
module_type  = 'Down';
% 本振频率
fre_lo               = 12783;
fre_set              = linspace(58000,62000,test_point) ; % 生成测试频率点
[mult,spec_fre_set]  = fre_judge(waveband,module_type,module,fre_set,fre_lo);

waveband     = 'K';
% 模块：Rf(射频模块)、Rm（调理模块）、Fcrm（二次变频与调理模块）
module       = 'Rf';
% 模块类型：Down（下变频模块）、Close（闭环）、Open（开环）
module_type  = 'Down';
% 本振频率
fre_lo               = 9200;
fre_set              = linspace(23000,25000,test_point) ; % 生成测试频率点
[mult,spec_fre_set]  = fre_judge(waveband,module_type,module,fre_set,fre_lo);

waveband     = 'X';
% 模块：Rf(射频模块)、Rm（调理模块）、Fcrm（二次变频与调理模块）
module       = 'Fcrm';
% 模块类型：Down（下变频模块）、Close（闭环）、Open（开环）
module_type  = 'Down';
% 本振频率
fre_lo               = 12040;
fre_set              = linspace(9800,11800,test_point) ; % 生成测试频率点
[mult,spec_fre_set]  = fre_judge(waveband,module_type,module,fre_set,fre_lo);

waveband     = 'X';
% 模块：Rf(射频模块)、Rm（调理模块）、Fcrm（二次变频与调理模块）
module       = 'Rf';
% 模块类型：Down（下变频模块）、Close（闭环）、Open（开环）
module_type  = 'Down';
% 本振频率
fre_lo               = 11910;
fre_set              = linspace(6868,11868,test_point) ; % 生成测试频率点
[mult,spec_fre_set]  = fre_judge(waveband,module_type,module,fre_set,fre_lo);
