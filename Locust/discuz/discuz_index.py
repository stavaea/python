#coding:utf-8
from locust import HttpLocust, TaskSet, task

class Discuz_Task(TaskSet):

    @task(1)
    def index(self):
        self.client.get("/forum.php")

class Discuz_Locust(HttpLocust):
    task_set = Discuz_Task
    host = "http://192.168.1.201:8888"
    min_wait = 1000
    max_wait = 2000