from socket import *
import subprocess

server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.0.1', 8090))
server.listen(5)

while True:
    conn, client_addr = server.accept()
    print(client_addr)

    while True:
        try:
            cmd = conn.recv(1024)
            if not cmd:
                break

            #ls -l;sadfasdf;pwd;echo 123
            obj = subprocess.Popen(cmd.decode('utf-8'), shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            stdout = obj.stdout.read()
            stderr = obj.stderr.read()

            cmd_res = stdout+stderr
            print(len(cmd_res))
            conn.send(cmd_res)
        except ConnectionResetError:
            break
    conn.close()

server.close()