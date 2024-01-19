# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2024/1/19 9:18
# @Author : waxberry
# @File : server.py
# @Software : PyCharm


import socket

# socket.socket() 会返回一个「主动套接字」
server = socket.socket(
    # 表示使用 IPv4，如果是 socket.AF_INET6
    # 则表示使用 IPv6
    socket.AF_INET,
    # 表示建立 TCP 连接，如果是 socket.SOCK_DGRAM
    # 则表示建立 UDP 连接
    socket.SOCK_STREAM
)
# 当然这两个参数也可以不传，因为默认就是它

# 设置套接字属性，这里让端口释放后立刻就能再次使用
server.setsockopt(socket.SOL_SOCKET,
                  socket.SO_REUSEADDR, True)

# 将「主动套接字」绑定在某个 IP 和端口上
server.bind(("localhost", 12345))
# 监听，此时「主动套接字」会变成「监听套接字」
server.listen(5)

# 调用 accept，等待客户端连接，此时会阻塞在这里
# 如果客户端连接到来，那么会返回「已连接套接字」，也就是这里的 conn
# 至于 addr 则是一个元组，保存了客户端连接的信息（IP 和端口）
conn, addr = server.accept()

# 下面我们通过「已连接套接字」conn 和客户端进行消息的收发
# 收消息使用 recv、发消息使用 send，和 read、write 本质是一样的
while True:
    msg = conn.recv(1024)
    # 当客户端断开连接时，msg 会收到一个空字节串
    if not msg:
        print("客户端已经断开连接")
        conn.close()
        break
    print("客户端发来消息:", msg.decode("utf-8"))
    # 然后我们加点内容之后，再给客户端发过去
    conn.send("服务端收到, 你发的消息是: ".encode("utf-8") + msg)