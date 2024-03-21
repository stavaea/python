function [data] = down_sys_para(rts,freq_lo,freq_center,rece,waveband,varargin)
%%%%%%%%%%%%%%%%%%%%%%%%默认参数配置%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    default_parameter = inputParser;
    addParameter(default_parameter,'para_updata',50);
    addParameter(default_parameter,'astrict',40);
    addParameter(default_parameter,'rcs_corr',0);
    addParameter(default_parameter,'rece_gain',55);
    addParameter(default_parameter,'tran_gain',25);
    default_parameter.parse(varargin{:});
%%%%%%%%%%%%%%%%%%%%%%%%%%%END%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    syspara     = zeros(1,16);
    syspara(1)  = hex2dec('A5A5A5A5');
    syspara(2)  = hex2dec('C00200FF');
    % 数据大小 uint
    syspara(3)  = 48;
    % 参数更新时间间隔，精度0.1ms,范围0~1000,单位ms
    syspara(4)  = default_parameter.Results.para_updata*10;
    % RTS延时，精度0.001m，范围0~500，单位m
    syspara(5)  = 0;
    % 幅度检测门限，精度1，量化值，范围0~65536
    syspara(6)  = default_parameter.Results.astrict;
    % 雷达与RTS距离，精度0.001，范围0~10，单位m
    syspara(7)  = 0;
    % 接收增益衰减,精度0.0625,单位dB,范围0~63
    syspara(8)  = rece/0.0625;
    % 系统本振，精度1MHz
    syspara(9)  = freq_lo;
    % 中心频率
    syspara(10) = freq_center;
    % RCS校正值，精度0.0625dB，范围-100~100，单位dB
    syspara(11) = uint_int(default_parameter.Results.rcs_corr)*16;
    % K_down_max,精度0.5，默认55,范围-100~100
    syspara(12) = uint_int(default_parameter.Results.rece_gain)*2;
    % k_up_max,精度1dB,范围-100~100
    syspara(13) = uint_int(default_parameter.Results.tran_gain);
    % 工作模式选择，0：正常工作；1：W校正；2：X校正
    syspara(14) = 0;
    % 工作频段选择
    % 0：24G
    % 1：77G
    % 2：60G
    syspara(15) = waveband;

    syspara(16) = 0;
    syspara(17) = 5000;
    % 包尾
    syspara(18) = hex2dec('B5B5B5B5');
    rts.write(syspara,'uint32');

    data = read_return(rts);
end
