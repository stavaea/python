# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/12/7 15:14
# @Author : waxberry
# @File : 三、实际应用.py
# @Software : PyCharm

'''
service test {
  rpc GetUsage(GetUsageRequest) returns (GetUsageResponse);
}


message GetUsageRequest {
  string appid = 1;
  string account_id = 4;
  string audience = 2;
  string metric = 3;
}


message GetUsageResponse {
  Usage usage = 1;
}

'''


def subcmd_GetUsage(args):
    # 连接 rpc 服务器
    channel = grpc.insecure_channel(ADDRESS)
    # 调用 rpc 服务
    stub = test_pb2_grpc.testStub(channel)
    response = stub.GetUsage(auth_pb2.GetUsageRequest(appid=args.appid,account_id=args.account_id,audience=args.audience,metric=args.metric))
    print("GetUsage received: \n" + str(response.usage))


# 首先利用pyinstaller工具将脚本编译为可执行程序：
# pyinstaller -F auth_client.py