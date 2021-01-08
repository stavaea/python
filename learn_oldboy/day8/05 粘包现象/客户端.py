from socket import *
import time

client=socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',8091))

client.send('hello'.encode('utf-8')) #b'hello'
time.sleep(5)
client.send('world'.encode('utf-8')) #b'world'

client.close()