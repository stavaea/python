from socket import *
import struct
import json

client=socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',8093))

while True:
    cmd=input('>>: ').strip()
    if not cmd:continue
    client.send(cmd.encode('utf-8'))

    #1、先接收报头的长度
    headers_size=struct.unpack('i',client.recv(4))[0]

    #2、再收报头
    headers_bytes=client.recv(headers_size)
    headers_json=headers_bytes.decode('utf-8')
    headers_dic=json.loads(headers_json)
    print('========>',headers_dic)
    total_size=headers_dic['total_size']

    #3、再收命令的结果
    recv_size=0
    data=b''
    while recv_size < total_size:
        recv_data=client.recv(1024)
        data+=recv_data
        recv_size+=len(recv_data)

    print(data.decode('gbk'))

client.close()