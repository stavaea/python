clc ; clear ; close all;

cont_file  = 'corr_table\dataK_0206\dca_cont.dat';
error_file = 'corr_table\dataK_0206\dca_err.dat';

cont_file  = 'corr_table\dataE\dca_cont.dat';
error_file = 'corr_table\dataE\dca_err.dat';

cont_file  = 'corr_table\dataE_0101\dca_cont.dat';
error_file = 'corr_table\dataE_0101\dca_err.dat';

cont_file  = 'corr_table\datak_0101\dca_cont.dat';
error_file = 'corr_table\datak_0101\dca_err.dat';

rts_ip     = '192.168.1.11';
rts_ip     = '192.168.1.10';
rts_port   = 7;
rts        = client_sever(rts_ip,rts_port);
rts_reset(rts);

down_sys_para(rts,0,0,78.5,76,1);

down_sys_para(rts,0,0,24,24,0);
down_sim_para(rts,10,0);


down_cont_table_corr (rts,cont_file ,7040,7040);
down_error_table_corr(rts,error_file,7040,7040);

down_cont_table_corr (rts,cont_file ,24000,24000);
down_error_table_corr(rts,error_file,24000,24000);
att_control(rts,0);


start_simulation(rts);