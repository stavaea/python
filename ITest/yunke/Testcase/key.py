#coding:utf-8
import json, time, hashlib
import requests
from cases.TestBase import TestBase
#
def key(time, params):
    para = json.dumps(params, separators=(',', ':'))
    # t = int(time.time())
    salt = "gn1002015"
    params = para+str(time)+salt
    key = hashlib.md5(hashlib.md5(params).hexdigest()).hexdigest()
    return key

print (key)


# 生成key
# def key():
#     para = json.dumps({"name": "18201274484", "password": "111111"}, separators=(',', ':'))
#     t = int(time.time())
#     salt = "gn1002015"
#     params = para + str(t) + salt
#     key = hashlib.md5(params).hexdigest()
#     key_str = hashlib.md5(key).hexdigest()
#     return key_str
#
# print key

#
# # n级台阶，每次走1或2，有多少种方法
# def f(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     else:
#         return f(n-1) + f(n-2)

#
# def getToken():
#     data = {"time": t,
#             "params": {"name": "18201274484", "password": "123456"},
#             "key": key
#             }
#     r = requests.post(
#         url="http://dev.gn100.com/interface/login/",
#         json=data,
#         headers={"Content-Type": "application/json"},
#     )
#     return r.text
#
# print getToken()



def get_token():
    t = int(time.time())
    url = "http://dev.gn100.com/interface/login"
    headers = {'Content-Type': 'application/json'}
    data = {"time": t,
            'u': 'a',
            "params": {"name": "18201274484", "password": "111111"},
            "key": key}
    r1 = requests.post(url=url, json=data, headers=headers)
    print (r1.text)
    return r1.json()['result']['token']
# token = r1.json()['result']['token']
# print token
    # print r1.status_code
# print data

print (get_token)




para = json.dumps({"name": "18201274484", "password": "111111"}, separators=(',', ':'))
t = int(time.time())
salt = "gn1002015"
params = para + str(t) + salt
key = hashlib.md5(hashlib.md5(params).hexdigest()).hexdigest()
print (key)


t = int(time.time())
url = "http://dev.gn100.com/interface/login"
headers = {'Content-Type': 'application/json'}
data = {"time": t,
        'u': 'a',
        "params": {"name": "18201274484", "password": "111111"},
        "key": key}
r1 = requests.post(url=url, json=data, headers=headers)
print (r1.text)
token = r1.json()['result']['token']
print (token)


encryptStr = json.dumps({"name": "18201274484", "password": "111111"}, separators=(",", ":"), ensure_ascii=False) + str(t) + salt
md5 = hashlib.md5()
encryptStr = encryptStr.encode("utf8")
md5.update(encryptStr)
encryptStr = md5.hexdigest()
md5 = hashlib.md5()
md5.update(encryptStr.encode("utf8"))
key = md5.hexdigest()

print (key, t)