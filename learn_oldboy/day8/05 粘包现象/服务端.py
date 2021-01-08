from socket import *
import time

server=socket(AF_INET,SOCK_STREAM)
server.bind(('127.0.0.1',8091))
server.listen(5)

conn,addr=server.accept()

#b'hello'
res1=conn.recv(5) #b'h'
print('res1: ',res1)

# b'elloworld'
time.sleep(6)
res2=conn.recv(5)
print('res2: ',res2)

conn.close()
server.close()