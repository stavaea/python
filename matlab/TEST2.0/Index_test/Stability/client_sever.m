function [rts] = client_sever(rts_ip,rts_port)
% Create Tcpclient
    rts = tcpclient(rts_ip,rts_port);
% % Set OutputBufferSize
%     rts.OutputBufferSize = 100000;
% % Set InputBufferSize
%     rts.InputBufferSize = 100000;
% Set ByteOrder
    rts.ByteOrder = 'little-endian';
% Set Timeout
    rts.Timeout = 20;
% Close Rts
    echotcpip("off");
% Open Rts
    echotcpip("on",rts_port);
end