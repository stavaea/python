#coding:utf-8

from locust import HttpLocust, TaskSet, task
from random import choice

class Discuz_Login(TaskSet):

    @task(1)
    def index(self):
        url = "/forum.php"
        headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)"}
        self.client.get(url, headers=headers, name="打开首页")

    @task(1)
    def login(self):
        userinfo = choice(self.locust.userdata)
        userinfo = userinfo.split(",")

        print (userinfo)

        url = "/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1"
        headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)"}
        data = {"fastloginfieid": "username",
                "handkey": "ls",
                "password": userinfo[1],
                "quickforward": "yes",
                "username": userinfo[0]}
        with self.client.post(url, headers=headers, data=data, name='登录') as response:
            print (response.text)
            return response

class Discuz_User(HttpLocust):

    task_set = Discuz_Login
    min_wait = 1000
    max_wait = 3000
    host = "http://192.168.1.201:8888"

    userdata = []
    with open("data/userdata.csv", "r") as file:
        for line in file.readlines:
            userdata.append(line.strip())
