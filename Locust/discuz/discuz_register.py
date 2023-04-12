# coding:utf-8

from locust import HttpLocust, TaskSet, task
from Wxytools import fetchStringByBoundary
import Queue
from Wxy_locust import *

class RegisterTaskSet(TaskSet):
    @task
    def register(self):
        "打开首页，获取服务器返回的formhash"
        with self.client.get("/forum.php") as response:
            formhash = Wxytools.fetchStringByBoundary(response.text)

        url = "/bbs/member.php?mod=register&inajax=1"
        try:
            userinfo = self.locust.user_data.get()#获取唯一的用户信息
        except Queue.Empty:
            print ('数据已取完')
            exit(0)

        userinfo = userinfo.split(',')

        headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)"}
        data = {"activationauth": "",
                "formhash": formhash,
                "password": userinfo[1],
                "repassword": userinfo[1],
                "username": userinfo[0],
                "email": userinfo[2]+'@qq.com',
                "resubmit": "yes",
                "referer": "http://192.168.1.201/forum.php"}
        with self.client.post(url, headers=headers, data=data) as response:
            pass
        self.discuz.logout(self.formhash)


class Discuz_User(HttpLocust):
    task_set = Discuz_Login
    min_wait = 1000
    max_wait = 3000
    host = "http://192.168.1.201:8888"

    userdata = []
    with open("data/userdata.csv", "r") as file:
        for line in file.readlines:
            userdata.append(line.strip())
