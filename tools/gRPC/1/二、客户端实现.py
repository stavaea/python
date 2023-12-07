# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/12/7 15:13
# @Author : waxberry
# @File : 二、客户端实现.py
# @Software : PyCharm

import helloworld_pb2
import helloworld_pb2_grpc
import grpc


import helloworld_pb2
import helloworld_pb2_grpc
import grpc

def run():

    # 连接 rpc 服务器
    channel = grpc.insecure_channel('localhost:50051')
    # 调用 rpc 服务
    stub = helloworld_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(helloworld_pb2.HelloRequest(name='test'))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    run()


'''
其中，关键的步骤为：
1、连接rpc服务器；
2、对service获取一个stub用于调用接口；
3、发送数据、接收数据。

将代码保存为client.py，运行脚本就可以成功获取服务端返回的结果了，假设服务端返回的文本为"Hello"：
# python client.py
# Greeter client received: Hello
到这里，一次简单的gRPC接口连接、交互就算完成了，并实现了一个简易的gRPC客户端
'''