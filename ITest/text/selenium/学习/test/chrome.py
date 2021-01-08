#coding:utf-8

from selenium import webdriver
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

driver = webdriver.Chrome(executable_path='E:\Google\Chrome\Application\chrome.exe')
# driver = webdriver.Firefox(executable_path='E:\Fox\\firefox.exe')
# driver = webdriver.Firefox()
# driver.maximize_window()

# driver.implicitly_wait(3)

driver.get('http://www.baidu.com')
driver.find_element_by_id('kw').send_keys('python+selenium')

driver.find_element_by_id('su').click()

# driver.quit()