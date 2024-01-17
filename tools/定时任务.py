# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2024/1/17 14:17
# @Author : waxberry
# @File : 定时任务.py
# @Software : PyCharm



# while True: + sleep()
import datetime
import time
def time_printer():
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    print('do func time:', ts)
def loop_monitor():
    while True:
        time_printer()
        time.sleep(5)
if __name__ == '__main__':
    loop_monitor()
# 主要缺点：
# 只能设定间隔，不能指定具体的时间，比如每天早上8:00
# sleep 是一个阻塞函数，也就是说 sleep 这一段时间，程序什么也不能操作。



# Timeloop
import time
from timeloop import Timeloop
from datetime import timedelta
tl = Timeloop
@tl.job(interval=timedelta(seconds=2))
def sample_job_every_2s():
    print('2s job current time : {}'.format(time.ctime()))
@tl.job(interval=timedelta(seconds=5))
def sample_job_every_5s():
    print("5s job current time : {}".format(time.ctime()))
@tl.job(interval=timedelta(seconds=10))
def sample_job_every_10s():
    print("10s job current time : {}".format(time.ctime()))



# threading.Timer



# sched
import datetime
import time
import sched
def time_printer():
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    print('do func time :', ts)
    loop_monitor()
def loop_monitor():
    s = sched.scheduler(time.time, time.sleep)  # 生成调度器
    s.enter(5, 1, time_printer, ())
    s.run()
if __name__ == "__main__":
    loop_monitor()



# schedule
import schedule
import time
def job():
    print("I'm working...")
schedule.every(10).seconds.do(job)
schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every(5).to(10).minutes.do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().minute.at(":17").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
# 装饰器：通过 @repeat() 装饰静态方法
import time
from schedule import every, repeat, run_pending
@repeat(every().second)
def job():
    print('working...')
while True:
    run_pending()
    time.sleep(1)
# 传递参数：
import schedule
def greet(name):
    print('Hello', name)
schedule.every(2).seconds.do(greet, name='Alice')
schedule.every(4).seconds.do(greet, name='Bob')
while True:
    schedule.run_pending()
# 装饰器同样能传递参数：
from schedule import every, repeat, run_pending
@repeat(every().second, 'World')
@repeat(every().minute, 'Mars')
def hello(planet):
    print('Hello', planet)
while True:
    run_pending()
# 取消任务：
import schedule
i = 0
def some_task():
    global i
    i += 1
    print(i)
    if i == 10:
        schedule.cancel_job(job)
        print('cancel job')
        exit(0)
job = schedule.every().second.do(some_task)
while True:
    schedule.run_pending()
# 运行一次任务：
import time
import schedule
def job_that_executes_once():
    print('Hello')
    return schedule.CancelJob
schedule.every().minute.at(':34').do(job_that_executes_once)
while True:
    schedule.run_pending()
    time.sleep(1)
# 根据标签检索任务：
# 检索所有任务：schedule.get_jobs()
import schedule
def greet(name):
    print('Hello {}'.format(name))
schedule.every().day.do(greet, 'Andrea').tag('daily-tasks', 'friend')
schedule.every().hour.do(greet, 'John').tag('hourly-tasks', 'friend')
schedule.every().hour.do(greet, 'Monica').tag('hourly-tasks', 'customer')
schedule.every().day.do(greet, 'Derek').tag('daily-tasks', 'guest')
friends = schedule.get_jobs('friend')
print(friends)
# 根据标签取消任务：
# 取消所有任务：schedule.clear()
import schedule
def greet(name):
    print('Hello {}'.format(name))
    if name == 'Cancel':
        schedule.clear('second-tasks')
        print('cancel second-tasks')
schedule.every().second.do(greet, 'Andrea').tag('second-tasks', 'friend')
schedule.every().second.do(greet, 'John').tag('second-tasks', 'friend')
schedule.every().hour.do(greet, 'Monica').tag('hourly-tasks', 'customer')
schedule.every(5).seconds.do(greet, 'Cancel').tag('daily-tasks', 'guest')
while True:
    schedule.run_pending()
# 运行任务到某时间：
import schedule
from datetime import datetime, timedelta, time
def job():
    print('working...')
schedule.every().second.until('23:59').do(job)  # 今天23:59停止
schedule.every().second.until('2030-01-01 18:30').do(job)  # 2030-01-01 18:30停止
schedule.every().second.until(timedelta(hours=8)).do(job)  # 8小时后停止
schedule.every().second.until(time(23, 59, 59)).do(job)  # 今天23:59:59停止
schedule.every().second.until(datetime(2030, 1, 1, 18, 30, 0)).do(job)  # 2030-01-01 18:30停止
while True:
    schedule.run_pending()
# 马上运行所有任务（主要用于测试）：
import schedule
def job():
    print('working...')
def job1():
    print('Hello...')
schedule.every().monday.at('12:40').do(job)
schedule.every().tuesday.at('16:40').do(job1)
schedule.run_all()
schedule.run_all(delay_seconds=3)  # 任务间延迟3秒
# 并行运行：使用 Python 内置队列实现：
import threading
import time
import schedule
def job1():
    print("I'm running on thread %s" % threading.current_thread())
def job2():
    print("I'm running on thread %s" % threading.current_thread())
def job3():
    print("I'm running on thread %s" % threading.current_thread())
def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()
schedule.every(10).seconds.do(run_threaded, job1)
schedule.every(10).seconds.do(run_threaded, job2)
schedule.every(10).seconds.do(run_threaded, job3)
while True:
    schedule.run_pending()
    time.sleep(1)



# APScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
# 输出时间
def job():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# BlockingScheduler
sched = BlockingScheduler()
sched.add_job(my_job, 'interval', seconds=5, id='my_job_id')
sched.start()



# Celery




# Apache Airflow