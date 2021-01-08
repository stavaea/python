#coding:utf-8
from selenium import webdriver
import re
import time

def CrawlKW_nosign(sourec_code, url):
    sourec_code_nospace = ''
    for i in sourec_code:
        if i != ' ' and i != '\n':
            sourec_code_nospace += i
    # print ('源码=', sourec_code_nospace)
    for ir in range(1, 11):
        re_result = eval("re.findall(r'(?<=id=\""+str(ir)+"\").+(?=id=\""+str(ir+1)+"\")', source_code_nospace)")
        print ('re_result=,', re_result)
        if url in str(re_result):
            result = re.search(r'(?<=<div class="c-acstract">).+?(?=</div>)', str(re_result)).group()
            print ('result=', result)
            if result != None:
                return result

if __name__ == '__main__':
    driver = webdriver.Firefox(executable_path=r'F:\webdriver\geckodriver.exe')
    driver.get("https://www.baidu.com")
    search_input = driver.find_element('xpath', '//input[@id="kw"]')
    search_input.send_keys('财务经理人')
    driver.find_element('xpath', '//input[@id="su"]').click()
    time.sleep(1)
    source_code = driver.page_source
    print (CrawlKW_nosign(source_code, 'www.cqicpa.org.cn'))