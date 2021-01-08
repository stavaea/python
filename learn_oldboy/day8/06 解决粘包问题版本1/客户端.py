from socket import *
import struct

client=socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',8093))

while True:
    cmd=input('>>: ').strip()
    if not cmd:continue
    client.send(cmd.encode('utf-8'))

    #1、先接收命令长度
    headers=client.recv(4)
    total_size = struct.unpack('i', headers)[0]

    #2、再收命令的结果
    recv_size=0
    data=b''
    while recv_size < total_size:
        recv_data=client.recv(1024)
        data+=recv_data
        recv_size+=len(recv_data)

    print(data.decode('gbk'))

client.close()