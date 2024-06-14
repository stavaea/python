function [rts] = client_sever(ip,port)
rts = tcpip(ip,port,'NetworkRole','client');
rts.OutputBufferSize = 100000;
rts.InputBufferSize = 100000;
rts.ByteOrder='littleEndian';
fclose(rts);
%The network client sets up a connection with a server and returns an error
%until the connection is complete
fopen(rts);