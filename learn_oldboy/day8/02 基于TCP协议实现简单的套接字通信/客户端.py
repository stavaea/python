import socket

#1、买手机
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #tcp协议

#2、拨电话
phone.connect(('127.0.0.1',8081)) #0-65535

#3、发收消息
phone.send('hello'.encode('utf-8'))

data=phone.recv(1024)
print(data)

#4、挂电话
phone.close()