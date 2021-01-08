#coding:utf-8

from appium import webdriver
import base64

desired_cpas = {}
desired_cpas['platforName'] = 'Android'
desired_cpas['platforVersion'] = '5.1'
desired_cpas['deviceName'] = 'Android Emulator'
desired_cpas['appPackage'] = 'com.android.calculator2'
desired_cpas['appActivity'] = '.Calculator'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cpas)

driver.find_element_by_name("1").click()
driver.find_element_by_name("5").click()
driver.find_element_by_name("9").click()
driver.find_element_by_name("delete").click()
driver.find_element_by_name("9").click()
driver.find_element_by_name("5").click()
driver.find_element_by_name("+").click()
driver.find_element_by_name("6").click()
driver.find_element_by_name("=").click()
driver.quit()



driver.lockDevice()  #android
driver.lockDevice(1000) #ios

driver.hide_keyboard()
driver.pull_file(path='')

content = ''
data = ''
driver.push_file()
