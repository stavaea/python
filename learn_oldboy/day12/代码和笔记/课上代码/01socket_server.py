import socket

sk = socket.socket()
sk.bind(("127.0.0.1", 8000))
sk.listen(5)


while 1:
    conn, addr = sk.accept()
    conn.recv(1024)
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')
    # conn.send(b'<h1>hello s20</h1>')
    with open("01.html", "rb") as f:
        data = f.read()
    conn.send(data)
    conn.close()
