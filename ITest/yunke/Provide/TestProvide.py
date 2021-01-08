#coding:utf-8

import hashlib
import json
import time

import requests
import yunke.Provide.Configuration


def key(TimeStamp, params):
    encryptStr = json.dumps(params, separators=(",", ":"), ensure_ascii=False) + str(TimeStamp) + yunke.Provide.Configuration.salt
    md5 = hashlib.md5()
    encryptStr = encryptStr.encode("utf8")
    md5.update(encryptStr)
    encryptStr = md5.hexdigest()
    md5 = hashlib.md5()
    md5.update(encryptStr.encode("utf8"))
    key = md5.hexdigest()
    return key

def login(res, mobile, password):
    params = {}
    t = int(time.time())
    params["u"] = "a"
    params["v"] = "2"
    params["time"] = t
    params["params"] = {
        "name": mobile,
        "password": password
    }
    params["key"] = key(t, params["params"])
    loginUrl = yunke.Provide.Configuration.HostUrl + "/interface/login"
    response = res.post(loginUrl, data=json.dumps(params, separators=(",", ":")))
    response.encoding = "utf-8"
    return res

# def get_token(mobile, password):
#     params = {}
#     t = int(time.time())
#     params["u"] = "a"
#     params["v"] = "2"
#     params["time"] = t
#     params["params"] = {
#         "name": mobile,
#         "password": password
#     }
#     params["key"] = key(t, params["params"])
#     loginUrl = yunke.Provide.Configuration.HostUrl + "/interface/login"
#     response = requests.post(loginUrl, data=json.dumps(params, separators=(",", ":")))
#     response.encoding = "utf-8"
#     result = response.json().get('result')
#     if result:
#         token = result.get('token')
#     else:
#         token = None
#
#     # print token
#     return token

def get_token(code, iv, encryptedData):
    params = {}
    t = int(time.time())
    params["appid"] = "110"
    params["apphash"] = key
    params["time"] = t
    params["params"] = {
        "code": "",
        "encryptedData": "",
        "iv": ""
    }
    loginUrl = yunke.Provide.Configuration.HostUrl + "/openapi/mobile/miniprogram"
    response = requests.post(loginUrl, data=json.dumps(params, separators=(",", ":")))
    response.encoding = "utf-8"
    result = response.json().get('result')
    if result:
        token = result.get('token')
    else:
        token = None

    # print token
    return token
