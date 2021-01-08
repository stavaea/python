from socket import *
import subprocess
import struct

server=socket(AF_INET,SOCK_STREAM)
server.bind(('127.0.0.1',8093))
server.listen(5)

while True:
    conn,client_addr=server.accept()
    print(client_addr)

    while True:
        try:
            cmd=conn.recv(8096)
            if not cmd:break

            #ls -l;sadfasdf;pwd;echo 123
            obj=subprocess.Popen(cmd.decode('utf-8'),shell=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE
                             )
            stdout=obj.stdout.read()
            stderr=obj.stderr.read()

            #1、制作固定长度的报头
            total_size = len(stdout) + len(stderr)
            headers=struct.pack('i',total_size)

            #2、先发送命令长度
            conn.send(headers)

            #3、发送命令的执行结果
            conn.send(stdout)
            conn.send(stderr)
        except ConnectionResetError:
            break
    conn.close()

server.close()