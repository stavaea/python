# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/5/26 14:15
# @Author : waxberry
# @File : cases.py
# @Software : PyCharm
import threading

from cffi.cparser import lock

from tools.快速冒烟测试小工具.Config.ProjVar import *
from tools.快速冒烟测试小工具.Util.ReadConfig import *
from tools.快速冒烟测试小工具.Driver.GetSessionOfCookie import *
from GetUrlFromOra import *
from DateToday import *
import logging

def get_urls(domain, q):
    # 判断是前端uc还是后端eclp去获取对应的登录数据
    if domain == 'eclp':
        login_url = read_ini_file(dbuser_ini_path, 'eclp', 'center_url')
        account = read_ini_file(dbuser_ini_path, 'eclp', 'center_account')
        password = read_ini_file(dbuser_ini_path, 'eclp', 'center_password')
    elif domain == 'uc':
        login_url = read_ini_file(dbuser_ini_path, 'uc', 'uc_url')
        account = read_ini_file(dbuser_ini_path, 'uc', 'uc_account')
        password = read_ini_file(dbuser_ini_path, 'uc', 'uc_password')
    # 获取eclp或uc的绑定cookie的session对象
    s = get_session_of_cookie(domain, login_url, account, password)
    # 从配置文件获取数据库的连接配置
    ora_ip = read_ini_file(dbuser_ini_path, 'db', 'oracle_ip')
    ora_account = read_ini_file(dbuser_ini_path, 'db', 'oracle_account')
    ora_password = read_ini_file(dbuser_ini_path, 'db', 'oracle_password')
    # 从数据库获取所有的url
    url_datas = get_url_from_oracle(ora_ip, ora_account, ora_password, domain)
    # 将获取到的所有url放入队列中
    for data in url_datas:
        q.put(data)
    return s

def get_urls_info():
    # 设置测试结果为全局变量
    global share_result
    global success_case_num
    global fail_case_num
    flagDict = {0: 'red', 1: '#00AC4E'}
    # 队列不为空时,循环获取数据
    while not q.empty():
        # 每个测试数据的测试结果,success或fail
        test_case_result = ''
        start = time.time()
        start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # 取队列
        data = q.get()
        # 分别取出要用到的菜单名称、url、断言关键词等数据
        sub_system_id = data[0]
        url_name = data[1]
        url = data[2]
        assert_word = data[3]
        # 存放断言失败的菜单的源码文件路径
        html_file_path = os.path.join(result_report_path, url_name + ".html")
        # 访问菜单页面并记录结果
        try:
            # 判断是eclp的还是uc的菜单,用不同的session对象去访问
            if sub_system_id == 0:
                r = uc_s.get(url)
            else:
                r = eclp_s.get(url)
            # 断言
            assert assert_word in r.text
            flag = 1
            debug('菜单：' + url_name + '断言成功：')
            # 记录当次是否访问成功
            test_case_result = 'Success'
            # 获得资源锁，记录成功个数
            lock.acquire()
            success_case_num += 1
            lock.release()
        except AttributeError as e:
            flag = 0
            error('菜单：' + url_name + '关键词断言失败，错误信息：' + str(traceback.format_exc()))
            test_case_result = 'Fail'
            # 如果失败,获取资源锁,记录失败数
            lock.acquire()
            fail_case_num += 1
            lock.release()
            # 将失败的菜单页面的源码保存为一个html文件,存到测试结果目录
            with open(html_file_path, 'w', encoding='utf-8') as fp:
                fp.write(r.text)
        except Exception as e:
            flag = 0
            error("菜单：" + url_name + "发送未知异常，错误信息：" + str(traceback.format_exc()))
            test_case_result = 'Fail'
            lock.acquire()
            fail_case_num += 1
            lock.release()
            with open(html_file_path, 'w', encoding='utf-8') as fp:
                fp.write(r.text)
        finally:
            end = time.time()
            waste_time = int((end - start) * 1000)
            # 获取资源锁,将当次访问的菜单名称、url断言关键词、时间等添加到html字符串
            lock.acquire()
            # 每一组数据测试结束后,都将其测试结果信息插入表格行的HTML代码中
            share_result += '''
                <tr>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td style="color:%s">%s</td>
                </tr>''' % (url_name, url, assert_word, waste_time, start_time, flagDict[flag], test_case_result)
            lock.release()

class MyThread(threading.Thread):
    def __init__(self, func):
        threading.Thread.__init__(self)
        self.func = func

    def run(self):
        self.func()


def htmlTemplate(share_result, result_report_path, success_case_num, fail_case_num):
    pass


if __name__ == '__main__':
    # 创建用来存放日志和报告的文件夹
    result_report_path = make_report_dir()
    # 建一个线程共享资源锁
    lock = threading.Lock()
    # 定义一个队列
    share_result = ""
    success_case_num = 0
    fail_case_num = 0
    # 获取前后台的绑定了cookie的session对象
    eclp_s = get_urls('eclp', q)
    uc_s = get_urls('uc', q)

    # 创建多个线程,并将get_urls_info任务传入处理
    threads = []
    for i in range(4):
        thread = MyThread(get_urls_info)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    # 将测试结果与模板拼接得到HTML报告
    htmlTemplate(share_result, result_report_path, success_case_num, fail_case_num)