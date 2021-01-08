import socket

phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #tcp协议
phone.connect(('127.0.0.1',8083)) #0-65535

while True:
    msg=input('>>: ').strip()
    if not msg:continue

    phone.send(msg.encode('utf-8'))
    # print('has send===>')
    data=phone.recv(1024)
    # print('has recv===>')
    print(data)

phone.close()