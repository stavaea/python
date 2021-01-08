from socket import *

server=socket(AF_INET,SOCK_DGRAM) #数据报协议
server.bind(('127.0.0.1',8082))


data,client_addr=server.recvfrom(3)
print('第一次：',data)
data,client_addr=server.recvfrom(3)
print('第二次: ',data)