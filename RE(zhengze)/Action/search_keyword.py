#coding:utf-8
from selenium import webdriver
from Action.search_keyword_nosign import *
from Action.optimiza_result import *
import re
import time

def CrawlKW(driver, keyword, url):
    driver.get('https://www.baidu.com/')
    search_input = driver.find_element('xpath', '//input[@id="kw"]')
    search_input.send_keys(keyword)
    driver.find_element('xpath', '//input[@id="su"]').click()
    time.sleep(1)
    source_code = driver.page_source
    kw_list1 = re.findall('(?<=官网</a>).+?(?=<div class="f13">)', source_code)
    if kw_list1 == [] and url == None:
        return '百度搜索不出官网'
    if kw_list1 == [] and url != None:
        result1 = CrawlKW_nosign(source_code, url)
        print ('reselt1=', result1)
        result2 = re.findall(r'(?<=match=).+(?=>)', result1)
        if result2 !=[]:
            last_result = clear_th(result2)
            return last_result
        else:
            last_result = clear_th(result1)
            return last_result
    kw_list2 = str(re.findall('(?<=<div class="c-abstract").+', str(kw_list1)[1:-1]))
    if str(kw_list2) == '[]':
        kw_list2 = str(re.findall('(?<=<div class="c-abstract").+', kw_list1[0]))
    time.sleep(1)
    last_result = clear_th(kw_list2[1:-1])
    return last_result

if __name__ == '__main__':
    from Util.excel import *
    from ProjectVar.var import *
    eins = Excel_r_w(excel_path, 'used_sheet')
    driver = webdriver.Firefox(executable_path=r'火狐路径')
    print (CrawlKW(driver, 'Idea', 'www.jetbrains.com'))