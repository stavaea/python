import socket

phone=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #tcp协议
# print(phone)
# phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
phone.bind(('127.0.0.1', 8083)) #0-65535
phone.listen(5)

print('starting...')
while True: #链接循环
    conn, client_addr = phone.accept() #(conn,client_addr)
    # print(conn,client_addr)
    print(client_addr)

    while True: #通信循环
        try:
            data = conn.recv(1024) #1024bytes?
            if not data:
                break #针对的是linux系统
            print('客户端消息',data)
            conn.send(data.upper())
            # print('====has send')
        except ConnectionResetError:
            break
    conn.close()

phone.close()

