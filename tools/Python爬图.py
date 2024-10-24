# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/12/7 11:23
# @Author : waxberry
# @File : Python爬图.py
# @Software : PyCharm


import time
import os
import re
import requests
from lxml import etree
from aip import AipFace


#百度云 人脸识别 申请信息
# 唯一必须填的信息就这三行
APP_ID = "XXXXXXXX"
API_KEY="XXXCXXXXXXXXXXXXXXXx"
SECRET_KEY = "XOOOOOXXXXXXXXXXXXXXXXXCXXXXXXX"
# 文件存放目录名，相对于当前目录
DIR ="image"
#过流颜值闯值，存储空间大的请随高
BEAUTY_THRESHOLD = 45
# 如果权限错误，浏览器中打开知乎，在开发者工具中复制一个，无需登录
#建议最好换一个，因为不知道知乎的反爬虫策路，如果太多人用同一个，可能会彤响程序运行
# #如何查换该值下文有讲述
AUTHORIZATION = "oauth c3cef7c66a1843f8b3a9e6a1e3160e20"
# 以下皆无需改动
# 每次请求知乎的讨论列表长度，不建议设定太长，注意节操
LIMIT = 5
# 这是话题[美女]的 ID，其是[颜值](20013528)的父话题
SOURCE = "19552207"
#爬虫假装下正常刘览器请求
USER_AGENT = "Mozilla/5.0 (Windows NT 5.1) Applewebkit/534.55.3 (KHTMl, like Gecko) Version/5.1.5 Safari/534.55.3"
#爬虫假装下正常刘览器请求
REFERER ="https://www.zhihu.com/topic/%s/newest" % SOURCE
# 某话题下讨论列表请求 ur1
BASE_URL = "https://www.zhihu.com/api/v4/topics/%s/feeds/timeline activity"
#初始请求 ur1 附带的请求袭务
URL_QUERY = "?include-data%5B%3F%28targettype%3Dtopic sticky module%29%5D,targetdata%58%3F%28target,type%3Danswer%29%5D"
#指定 ur1，获取对应原始内容 /图片
def fetch_image(url):
    try:
        headers = {
            "User-Agent": USER_AGENT,
            "Referer": REFERER,
            "authorization": AUTHORIZATION
        }
        s = requests.get(url, headers=headers)
    except Exception as e:
            print("fetch last activities fail." + url)
        raise e
    return s.content
#指定 ur1，获取对应 JSON 返回 / 话题列表
def fetch_activities(url):
    try:
        headers = {
            f"user-Agent": USER_AGENT,
            "Referer": REFERER,
            "authorization": AUTHORIZATION
        }
        s = requests.get(url, headers=headers)
    except Exception as e:
        print("fetch last activities fail." + url)
        raise e
    return s.json()
# 处理返回的话数列
def process_activities(datums, face_detective):
    for data in datums["data"]:
        target = data["target"]
        if "content" not in target or "question" not in target or "author" not in target:
            continue
    # 解析列表中每一个元案的内容
    html = etree.HTML(target["content"])
    seq = 0

    print("current answer: " + question_title + "author:" author_name)
    #辣取所有图片地址
    images = html.xpath("//img/@src")
    for image in images:
        if not image.startswith("http"):
            continue
    s = fetch_image(image)
    # 请求人脸检测服多
    scores = face_detective(s)
    for score in scores:
        filename = ("d--" % score) + author_name + "--" + question_title + ("--%d" % seq) + ".jpg"
        filename = re.sub(r"(?u)[ - w.]", '-', filename)
        # r'注意文件名的处理，不同平台的非法字符不样，这里只做了简单处理，特别是 author name / question title 中的内容
        seq = seq + 1
        with open(os.pathjoin(DIR, filename), "wb") as fd:
            fd.write(s)
        # 人脸检测 免费，但有 OPS 限制
        time.sleep(2)
        if not datums["paging"]["is_end"]:
            # 获取后续讨论列表的请求url
            return datums["paging"]["next"]
        else:
            return None
def get_valid_filename(s):
    s = str(s).strip().replace("", '-')
    return re.sub(r'(?u)[^-\w.]', '-', s)

def init_face_detective(app_id, api_key, secret_key):
        client = AipFace(app_id, api_key, secret_key)
        # 人脸检测中，在响应中附带额外的字段。年龄、性别颜值、质量
        options = {"face_fields": "age,gender,beauty,qualities"}
def detective(image):
        r = client.detect(image, options)
        #如果没有检测到人胎
        if r["result num"] == 0:
            return []
            scores =[]
            for face in r["result"]:
        #人脸器信度太低
                if face["face probability"] < 0.6:
                    continue
        # 真实人脸居信度太低
                if face["qualities"]["type"]["human"] < 0.6:
                    continue
        # 颜值低于阈值
                if face["beauty"] < BEAUTY_THRESHOLD:
                    continue
        # 性别非女性
                if face["gender"] != "female":
                    continue
            scores.append(face["beauty"])
            return scores
            return detective

def init_env():
    if not os.path.exists(DIR):
        os.makedirs(DIR)
        init_env()
    face_detective = init_face_detective(APP_ID, API_KEY ,SECRET_KEY)
    url = BASE_URL % SOURCE + URL_QUERY
    while url is not None:
        print("current url:" + ur1)
        datums = fetch_activities(url)
    ur1 = process_activities(datums, face_detective)