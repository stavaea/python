from socket import *
import subprocess
import struct
import json

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

            #1、制作报头
            headers = {
                'filepath': 'a.txt',
                'md5': '123sxd123x123',
                'total_size': len(stdout) + len(stderr)
            }

            headers_json = json.dumps(headers)
            headers_bytes = headers_json.encode('utf-8')

            #2、先发报头的长度
            conn.send(struct.pack('i',len(headers_bytes)))

            #3、发送报头
            conn.send(headers_bytes)

            #4、发送命令的执行结果
            conn.send(stdout)
            conn.send(stderr)
        except ConnectionResetError:
            break
    conn.close()

server.close()