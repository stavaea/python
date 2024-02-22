# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2024/2/22 16:09
# @Author : waxberry
# @File : Airtest-Selenium刷B站视频.py
# @Software : PyCharm

from airtest.core.api import *
from airtest_selenium.proxy import WebChrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading
import time
import random
import json

#保存以及调用cookie的线程
class UtilFunc():
    def cookie_is_exist_(self, cook_name='_'):# 检查txt文件是否存在
        if os.path.exists(f'{cook_name}cookies.txt'):
            return True
        return False

    def cookie_save_(self, driver, cook_name='_'):  # 保存cookie到txt文件中以便下次读取
        # 获取当前页面的所有cookie
        cookies = driver.get_cookies()
        # 将cookie转换为JSON字符串
        cookies_json = json.dumps(cookies)
        # 保存cookie到txt文件
        with open(f'{cook_name}cookies.txt', 'w') as file:
            file.write(cookies_json)
        print(f"保存cookies:{cookies}")

        def cookie_set_(self, driver, cook_name='_'):  # 读取cookie文件并给当前网站设置已存cookie
            # 从txt文件读取JSON_cookie数据
            with open(f'{cook_name}cookies.txt', 'r', encoding='gbk') as file:
                json_data = file.read()
            # 将JSON数据转换为列表
            data_list = json.loads(json_data)
            for cookie in data_list:
                driver.add_cookie(cookie)
            print("设置cookie")

# 创建一个实例，代码运行到这里，会打开一个chrome浏览器
driver = WebChrome()
isLogin = False   #存储登录状态值，False为未登录，True为已登录

#打开chrome浏览器并打开视频播放
def start_selenium():
    driver.implicitly_wait(20)
    driver.get("https://www.baidu.com/")
    # 输入搜索关键词并提交搜索
    search_box = driver.find_element_by_name('wd')
    search_box.send_keys('哔哩哔哩')
    search_box.submit()

    try:
    # 查找搜索结果中文本为 "哔哩哔哩" 的元素并点击
        results = driver.find_elements_by_xpath('//div[@id="content_left"]//span[contains(text(), "哔哩哔哩")]')
        if results:
            results[0].click()
            print("点击了哔哩哔哩搜索结果")
    except Exception as e:
        element = driver.find_element_by_xpath(
            "//div[@id='content_left']/div[@id='1']/div[@class='c-container']/div[1]/h3[@class='c-title t t tts-title']/a")
        element.click()
    driver.switch_to_new_tab()  # 切换界面

    util_cookie = UtilFunc()
    if util_cookie.cookie_is_exist_("Airtest酱登录"):  # 存在cookie文件，设置cookie
        util_cookie.cookie_set_(driver, "Airtest酱登录")
    # 输入搜索关键词并提交搜索
    search_box = driver.find_element_by_class_name('nav-search-input')
    search_box.send_keys('Airtest酱')
    # 模拟发送Enter键
    search_box.send_keys(Keys.ENTER)
    sleep(5)
    driver.switch_to_new_tab()  # 切换界面

    results_ = driver.find_elements_by_xpath(
        '//div[@class="bili-video-card__info--right"]//span[contains(text(),"Airtest酱")]')
    if results_:
        results_[0].click()
    driver.switch_to_new_tab()  # 切换界面
    driver.refresh()
    sleep(2)
    video_ele = driver.find_element_by_xpath("//div[@title='14天Airtest自动化测试小白课程']")
    # 滚动到指定元素处
    driver.execute_script("arguments[0].scrollIntoView(true);", video_ele)
    sleep(5)
    video_ele.click()
    driver.switch_to_new_tab()  # 切换界面

    # 获取所有视频
    video_list = driver.find_elements_by_xpath("//ul[@class='row video-list clearfix']//a[@class='title']")
    random_element = random.choice(video_list)
    random_element.click()  # 随机播放一个
    driver.switch_to_new_tab()  # 切换界面

#登录
def is_login():
    """线程检测登录弹窗"""

    def is_no_login(*args):
        global is_login# 在线程内修改外部常量的值
        no_login_tip = True
        while True:
            element = driver.find_elements_by_css_selector('.bili-mini-content-wp')
            if len(element) > 0:
                if no_login_tip:
                    print("未登录 请在五分钟内扫码")
                    no_login_tip = False
            else:
                print("未检测到登录弹窗")
                check_login_ele = driver.find_elements_by_css_selector('.bpx-player-dm-wrap')
                if not check_login_ele:
                    isLogin = True
                    UtilFunc().cookie_save_(driver, "Airtest酱登录")
                    print("保存cookie")
                    break
                log_text_array = [element.text for element in check_login_ele]  # 使用列表推导式简化代码
                if "请先登录或注册" in log_text_array:
                    loginbtn = driver.find_elements_by_xpath(
                        "//div[@class='bili-header fixed-header']//div[@class='header-login-entry']")
                    if loginbtn:
                        loginbtn[0].click()
                    isLogin = False
                    print("判断cookie文件是否存在，方便下次调用，设置后刷新页面")
                else:
                    isLogin = True
                    UtilFunc().cookie_save_(driver, "Airtest酱登录")
                    print("保存cookie")
                    break

    thread = threading.Thread(target=is_no_login, args=("args",))
    thread.start()

# 暂停播放
def video_pause_and_play(check_btn=False):
    if isLogin:
        try:
            paus_btn = driver.find_elements_by_xpath(
                "//*[@id=\"bilibili-player\"]//div[@class='bpx-player-ctrl-btn bpx-player-ctrl-play']")
            if paus_btn[0]:
                detection_time1 = driver.find_elements_by_xpath(
                    '//*[@class="bpx-player-control-bottom-left"]//div[@class="bpx-player-ctrl-time-label"]')
                start_time = detection_time1[0].text
                sleep(5)
                # 时间戳检测是否在播放
                detection_time2 = driver.find_elements_by_xpath(
                    '//*[@class="bpx-player-control-bottom-left"]//div[@class="bpx-player-ctrl-time-label"]')
                end_time = detection_time2[0].text
                if start_time == end_time or check_btn:
                    print("点击播放(暂停)按钮")
                    paus_btn[0].click()
        except Exception as e:
            print(f"点击播放(暂停)出错{e}")

#发送弹幕
def video_sms(sms_body="不错"):
    if isLogin:
        try:
            sms_input_edit = driver.find_element_by_xpath("//input[@class='bpx-player-dm-input']")
            sms_input_edit.send_keys(sms_body)
            # 模拟发送Enter键
            sms_input_edit.send_keys(Keys.ENTER)
        except Exception as e:
            print(f"发弹幕出错{e}")
    print(f"发送弹幕：{sms_body}")

#点赞
def video_love():
    if isLogin:
        print("点赞")
        try:
            sms_input_edit = driver.find_elements_by_xpath(
                "//div[@class='toolbar-left-item-wrap']//div[@class='video-like video-toolbar-left-item']")
            if not sms_input_edit:
                print("已经点赞")
                return
            sms_input_edit[0].click()
        except Exception as e:
            print(f"点赞出错{e}")

#收藏
def video_collect():
    if isLogin:
        print("收藏")
        try:
            colle_btn = driver.find_elements_by_xpath(
                "//div[@class='toolbar-left-item-wrap']//div[@class='video-fav video-toolbar-left-item']")
            if not colle_btn:
                print("已经收藏")
                return
            colle_btn[0].click()
            sleep(2)
            list_coll = driver.find_elements_by_xpath("//div[@class='group-list']//ul/li/label")
            random_element = random.choice(list_coll)  # 随机收藏
            # 滚动到指定元素处
            driver.execute_script("arguments[0].scrollIntoView(true);", random_element)
            sleep(2)
            random_element.click()  # 随机收藏一个
            sleep(2)
            driver.find_element_by_xpath("//div/button[@class='btn submit-move']").click()  # 确认收藏
        except Exception as e:
            print(f"收藏出错{e}")


# 等待元素出现
def wait_for_element(driver, selector, timeout=60 * 5):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, selector))
        )
        return element
    except Exception:
        print("元素未出现")
        return None

#头像元素初始化
selem = "//div[@class='bili-header fixed-header']//*[contains(@class, 'header-avatar-wrap--container mini-avatar--init')]"

if __name__ == "__main__":
    start_selenium()  # 开启浏览器找到视频播放
    is_login()  # 检测是否出现登录弹窗
    # 等待元素出现
    element = wait_for_element(driver, selem)
    if element:
        print("检测到已经登录")
        # 暂停和播放视频
        for _ in range(2):
            video_pause_and_play()
            sleep(3)
        driver.refresh()
        # 发送弹幕
        sms_list = ["感觉不错，收藏了", "666,这么强", "自动化还得看airtest", "干货呀", "麦克阿瑟直呼内行"]
        for item in sms_list:
            wait_time = random.randint(5, 10)  # 随机生成等待时间，单位为秒
            time.sleep(wait_time)  # 等待随机的时间
            video_sms(item)  # 评论

        # 点赞和收藏视频
        for action in [video_love, video_collect]:
            action()
            sleep(3)
    else:
        print("登录超时")