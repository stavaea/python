# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2024/1/19 9:30
# @Author : waxberry
# @File : Echo_server.py
# @Software : PyCharm



import asyncio
import socket

async def echo(conn: socket.socket):
    loop = asyncio.get_running_loop()
    # 无限循环等待来自客户端连接的数据
    try:
        while data := await loop.sock_recv(conn, 1024):
            # 收到数据之后再将其发送给客户端
            # 为了区分，我们发送的时候在结尾加一个 b"~"
            await loop.sock_sendall(conn, data + b"~")
    except Exception as e:
        print(f"服务出错: {e}")
    finally:
        conn.close()

async def listen_for_conn(server: socket.socket):
    loop = asyncio.get_running_loop()
    while True:
        conn, addr = await loop.sock_accept(server)
        conn.setblocking(False)
        print(f"收到客户端 {addr} 的连接")
        # 每次连接时，都创建一个任务来监听客户端的数据
        asyncio.create_task(echo(conn))

async def main():
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    server.setblocking(False)
    server.bind(("localhost", 12345))
    server.listen()

    await listen_for_conn(server)

asyncio.run(main())