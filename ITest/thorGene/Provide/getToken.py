# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/5/24 9:30
# @Author : waxberry
# @File : getToken.py
# @Software : PyCharm

import hashlib
import json
import time
import requests
import ITest.thorGene.Provide.TestProvide

def key(TimeStamp, params):
    encryptStr = json.dumps(params, separators=(",", ":"), ensure_ascii=False) + str(TimeStamp) + ITest.thorGene.Provide.Configuration.salt
    md5 = hashlib.md5()
    encryptStr = encryptStr.encode("utf8")
    md5.update(encryptStr)
    encryptStr = md5.hexdigest()
    md5 = hashlib.md5()
    md5.update(encryptStr.encode("utf8"))
    key = md5.hexdigest()
    return key

def login(res, username, password):
    params = {}
    t = int(time.time())
    # params["u"] = "a"
    # params["v"] = "2"
    # params["time"] = t
    params["params"] = {
        "name": username,
        "password": password
    }
    params["key"] = key(t, params["params"])
    loginUrl = ITest.thorGene.Provide.Configuration.HostUrl + "/login"
    response = res.post(loginUrl, data=json.dumps(params, separators=(",", ":")))
    response.encoding = "utf-8"
    return res

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
    loginUrl = ITest.thorGene.Provide.Configuration.HostUrl + "/login"
    response = requests.post(loginUrl, data=json.dumps(params, separators=(",", ":")))
    response.encoding = "utf-8"
    result = response.json().get('result')
    if result:
        token = result.get('token')
    else:
        token = None

    # print token
    return token