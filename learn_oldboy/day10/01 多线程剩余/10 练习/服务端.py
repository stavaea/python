from gevent import monkey,spawn;monkey.patch_all()
from threading import current_thread
from socket import *

def comunicate(conn):
    print('子线程：%s' %current_thread().getName())
    while True:
        try:
            data=conn.recv(1024)
            if not data:break
            conn.send(data.upper())
        except ConnectionResetError:
            break
    conn.close()

def server(ip,port):
    print('主线程：%s' %current_thread().getName())
    server = socket(AF_INET, SOCK_STREAM)
    server.bind((ip,port))
    server.listen(5)

    while True:
        conn, addr = server.accept()
        print(addr)
        # comunicate(conn)
        # t=Thread(target=comunicate,args=(conn,))
        # t.start()
        spawn(comunicate,conn)

    server.close()

if __name__ == '__main__':
    g=spawn(server,'127.0.0.1', 8081)
    g.join()