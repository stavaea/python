clc ; clear ; close all;
test_point =11;
%% RS_E_Rf_Down_5G
waveband     = 'E';
module       = 'Rf';
module_type  = 'Down';
fre_start    = 76000;
fre_stop     = 81000;
fre_lo       = 11910;
fre_set      = linspace(fre_start,fre_stop,test_point) ;
[mult,spec_fre_set] = fre_judge(waveband,module_type,module,fre_set,fre_lo);
%% RS_E_Rf_Up_5G
waveband     = 'E';
module       = 'Rf';
module_type  = 'Up';
fre_start    = 4540;
fre_stop     = 9540;
fre_lo       = 11910;
fre_set      = linspace(fre_start,fre_stop,test_point) ;
[mult,spec_fre_set] = fre_judge(waveband,module_type,module,fre_set,fre_lo);
%% RS_E_Rf_Down_2G
waveband     = 'E';
module       = 'Rf';
module_type  = 'Down';
fre_start    = 76000;
fre_stop     = 78000;
fre_lo       = 11400;
fre_set      = linspace(fre_start,fre_stop,test_point) ;
[mult,spec_fre_set] = fre_judge(waveband,module_type,module,fre_set,fre_lo);
%% RS_E_Rf_Up_2G
waveband     = 'E';
module       = 'Rf';
module_type  = 'Up';
fre_start    = 7600;
fre_stop     = 9600;
fre_lo       = 11400;
fre_set      = linspace(fre_start,fre_stop,test_point) ;
[mult,spec_fre_set] = fre_judge(waveband,module_type,module,fre_set,fre_lo);
%% RS_E_Fcrm_Down
waveband     = 'E';
module       = 'Fcrm';
module_type  = 'Down';
fre_start    = 7600;
fre_stop     = 9600;
fre_lo       = 9840;
fre_set      = linspace(fre_start,fre_stop,test_point) ;
[mult,spec_fre_set] = fre_judge(waveband,module_type,module,fre_set,fre_lo);
%% RS_E_Fcrm_Up
waveband     = 'E';
module       = 'Fcrm';
module_type  = 'Up';
fre_start    = 240;
fre_stop     = 2240;
fre_lo       = 9840;
fre_set      = linspace(fre_start,fre_stop,test_point) ;
[mult,spec_fre_set] = fre_judge(waveband,module_type,module,fre_set,fre_lo);

%% RS_E_Rm_Down
waveband     = 'E';
module       = 'Rm';
module_type  = 'Down';
fre_start    = 4540;
fre_stop     = 9540;
fre_lo       = 9800;
fre_set      = linspace(fre_start,fre_stop,test_point) ;
[mult,spec_fre_set] = fre_judge(waveband,module_type,module,fre_set,fre_lo);
%% RS_E_Rm_Up
waveband     = 'E';
module       = 'Rm';
module_type  = 'Up';
fre_start    = 4540;
fre_stop     = 9540;
fre_lo       = 9840;
fre_set      = linspace(fre_start,fre_stop,test_point) ;
[mult,spec_fre_set] = fre_judge(waveband,module_type,module,fre_set,fre_lo);
%% RS_V_Rf_Down_5G_12783
waveband     = 'V';
module       = 'Rf';
module_type  = 'Down';
fre_start    = 58000;
fre_stop     = 63000;
fre_lo       = 12783;
fre_set      = linspace(fre_start,fre_stop,test_point) ;
[mult,spec_fre_set] = fre_judge(waveband,module_type,module,fre_set,fre_lo);
%% RS_V_Rf_Up_5G_12783
waveband     = 'V'  ;
module       = 'Rf' ;
module_type  = 'Up' ;
fre_start    = 6868 ;
fre_stop     = 11868;
fre_lo       = 12783;
fre_set      = linspace(fre_start,fre_stop,test_point) ;
[mult,spec_fre_set] = fre_judge(waveband,module_type,module,fre_set,fre_lo);
%% RS_V_Rf_Down_5G_13283
waveband     = 'V';
module       = 'Rf';
module_type  = 'Down';
fre_start    = 60000;
fre_stop     = 65000;
fre_lo       = 13283;
fre_set      = linspace(fre_start,fre_stop,test_point) ;
[mult,spec_fre_set] = fre_judge(waveband,module_type,module,fre_set,fre_lo);
%% RS_V_Rf_Up_5G_13283
waveband     = 'V'  ;
module       = 'Rf' ;
module_type  = 'Up' ;
fre_start    = 6868 ;
fre_stop     = 11868;
fre_lo       = 13283;
fre_set      = linspace(fre_start,fre_stop,test_point) ;
[mult,spec_fre_set] = fre_judge(waveband,module_type,module,fre_set,fre_lo);
%% RS_V_Rf_Down_2G
waveband     = 'V';
module       = 'Rf';
module_type  = 'Down';
fre_start    = 58000;
fre_stop     = 60000;
fre_lo       = 12050;
fre_set      = linspace(fre_start,fre_stop,test_point) ;
[mult,spec_fre_set] = fre_judge(waveband,module_type,module,fre_set,fre_lo);
%% RS_V_Rf_Up_2G
waveband     = 'V'  ;
module       = 'Rf' ;
module_type  = 'Up' ;
fre_start    = 9800 ;
fre_stop     = 11800;
fre_lo       = 12050;
fre_set      = linspace(fre_start,fre_stop,test_point) ;
[mult,spec_fre_set] = fre_judge(waveband,module_type,module,fre_set,fre_lo);
%% RS_X_Fcrm_Down
waveband     = 'X';
module       = 'Fcrm';
module_type  = 'Down';
fre_start    = 9800;
fre_stop     = 11800;
fre_lo       = 12040;
fre_set      = linspace(fre_start,fre_stop,test_point) ;
[mult,spec_fre_set] = fre_judge(waveband,module_type,module,fre_set,fre_lo);
%% RS_X_Fcrm_Up
waveband     = 'X'  ;
module       = 'Fcrm' ;
module_type  = 'Up' ;
fre_start    = 240 ;
fre_stop     = 2240;
fre_lo       = 12040;
fre_set      = linspace(fre_start,fre_stop,test_point) ;
[mult,spec_fre_set] = fre_judge(waveband,module_type,module,fre_set,fre_lo);
%% RS_X_Rm_Down
waveband     = 'X';
module       = 'Rm';
module_type  = 'Down';
fre_start    = 6868;
fre_stop     = 11868;
fre_lo       = 12040;
fre_set      = linspace(fre_start,fre_stop,test_point) ;
[mult,spec_fre_set] = fre_judge(waveband,module_type,module,fre_set,fre_lo);
%% RS_X_Rm_Up
waveband     = 'X'  ;
module       = 'Rm' ;
module_type  = 'Up' ;
fre_start    = 6868;
fre_stop     = 11868;
fre_lo       = 12050;
fre_set      = linspace(fre_start,fre_stop,test_point) ;
[mult,spec_fre_set] = fre_judge(waveband,module_type,module,fre_set,fre_lo);
%% RS_K_Rf_Down
waveband     = 'K';
module       = 'Rf';
module_type  = 'Down';
fre_start    = 23000;
fre_stop     = 25000;
fre_lo       = 9200;
fre_set      = linspace(fre_start,fre_stop,test_point) ;
[mult,spec_fre_set] = fre_judge(waveband,module_type,module,fre_set,fre_lo);
%% RS_K_Rf_Up
waveband     = 'K'  ;
module       = 'Rf' ;
module_type  = 'Up' ;
fre_start    = 4600;
fre_stop     = 6600;
fre_lo       = 9200;
fre_set      = linspace(fre_start,fre_stop,test_point) ;
[mult,spec_fre_set] = fre_judge(waveband,module_type,module,fre_set,fre_lo);
