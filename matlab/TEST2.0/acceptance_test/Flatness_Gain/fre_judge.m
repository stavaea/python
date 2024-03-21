function [mult,spec_fre_set] = fre_judge(waveband,module_type,module,fre_set,fre_lo)
% fre_judge 主要判断是否需要进行倍频处理及输出频谱仪的中心频率
% 波段：E、V、K、X波段
% 模块：Rf(射频模块)、Rm（调理模块）、Fcrm（二次变频与调理模块）
% 模块类型：Down（下变频模块）、Close（闭环）、Open（开环）、Up(上变频模块)

switch (waveband)
	case 'E'
		waveband_judge = 1;
	case 'V'
		waveband_judge = 2;
	case 'X'
		waveband_judge = 3;
	case 'K'
		waveband_judge = 4;
end

switch (module)
	case 'Rf'
		module_judge = 1;
	case 'Fcrm'
		module_judge = 2;
	case 'Rm'
		module_judge = 3;
end

switch (module_type)
	case 'Down'
		module_type_judge = 1;
	case 'Up'
		module_type_judge = 2;
	case 'Close'
		module_type_judge = 3;
	case 'Open'
		module_type_judge = 3;
end

if module_judge == 3 || module_type_judge == 3
    spec_fre_set = fre_set;
    mult = 1;
end

if waveband_judge == 1 % RS_E
	if module_judge == 1 % RS_E_Rf
		mult = 6;
		if module_type_judge == 1 % RS_E_Rf_Down
			spec_fre_set = fre_set - 6*fre_lo;
		elseif module_type_judge == 2 % RS_E_Rf_Up
			spec_fre_set = fre_set + 6*fre_lo;
		end
	elseif module_judge == 2% RS_E_Fcrm
		mult = 1;
		if module_type_judge == 1 % RS_E_Fcrm_Dwon
			spec_fre_set = fre_lo - fre_set;
		elseif module_type_judge == 2 % RS_E_Fcrm_Up
			spec_fre_set = fre_lo - fre_set;
		end
	end
elseif waveband_judge == 2 % RS_V
	if module_judge == 1 % RS_V_Rf
		mult = 6;
		if module_type_judge == 1 % RS_V_Rf_Down
			spec_fre_set = fre_set - fre_lo * 4 ;
		elseif module_type_judge == 2 % RS_V_Rf_Up
			spec_fre_set = fre_set + fre_lo * 4 ;
		end
	end
elseif waveband_judge == 3 % RS_X
	mult = 1 ;
	if module_judge == 2 % RS_X_Fcrm
		if module_type_judge == 1 % RS_X_Fcrm_Down
			spec_fre_set = fre_lo - fre_set;
		elseif module_type_judge == 2 % RS_X_Fcrm_Up
			spec_fre_set = fre_lo - fre_set;
		end
	end
elseif waveband_judge == 4 % RS_K
	mult = 1 ;
	if module_judge == 1 % RS_K_Rf
		if module_type_judge == 1 % RS_K_Rf_Down
			spec_fre_set = fre_set - 2*fre_lo ;
		elseif module_type_judge == 2 % RS_K_Rf_Up
			spec_fre_set = fre_set + 2*fre_lo ;
		end
	end
end

