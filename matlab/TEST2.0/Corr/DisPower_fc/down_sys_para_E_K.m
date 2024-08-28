function [data] = down_sys_para_E_K(rts,delay,wave_band_sel,rece,varargin)
%%%%%%%%%%%%%%%%%%%%%%%%默认参数配置%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    default_parameter = inputParser;
    addParameter(default_parameter,'para_updata',50);
    addParameter(default_parameter,'astrict',40);
    addParameter(default_parameter,'rcs_corr',0);
    addParameter(default_parameter,'rece_gain',0);
    addParameter(default_parameter,'tran_gain',3);
    default_parameter.parse(varargin{:});
%%%%%%%%%%%%%%%%%%%%%%%%%%%END%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    syspara     = zeros(1,16);
    syspara(1)  = hex2dec('A5A5A5A5');
    syspara(2)  = hex2dec('C00200FF');
    % 数据大小 uint
    syspara(3)  = 52;
    % 参数更新时间间隔，精度0.1ms,范围0~1000,单位ms
    syspara(4)  = default_parameter.Results.para_updata*10;
    % RTS延时，精度0.001m，范围0~500，单位m
    syspara(5)  = delay * 1000;
    % 幅度检测门限，精度1，量化值，范围0~65536
    syspara(6)  = default_parameter.Results.astrict;
    % 雷达与RTS距离，精度0.001，范围0~10，单位m
    syspara(7)  = 0.6*1e3;
    % 接收增益衰减,精度0.25,单位dB,范围0~63
    syspara(8)  = rece*16;
    % 系统本振，精度1MHz，单位GHz,范围76~81GHz
    syspara(9)  = 78500;
    % 中心频率
    syspara(10) = 76500;
    % RCS校正值，精度0.1dB，范围-100~100，单位dB
    syspara(11) = uint_int(default_parameter.Results.rcs_corr*16);
    % K_down_max,精度0.5，默认55,范围-100~100
    syspara(12) = uint_int(default_parameter.Results.rece_gain)*2;
    % k_up_max,精度1dB,范围-100~100
    syspara(13) = uint_int(default_parameter.Results.tran_gain);
    % 工作模式选择，0：正常工作；1：W校正；2：X校正
    syspara(14) = 0;
    % 工作频段选择
    syspara(15) = wave_band_sel;
    % 包尾
    syspara(16) = 0;
    syspara(17) = hex2dec('B5B5B5B5');
    rts.write(syspara,'uint32');

    data = read_return(rts);
end
