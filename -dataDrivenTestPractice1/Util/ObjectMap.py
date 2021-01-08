#coding:utf-8

from selenium.webdriver.support.ui import WebDriverWait


# 获取单个元素对象
def getElement(driver, locateType, locateExpression):
    try:
        element = WebDriverWait(driver, 10).until(lambda x: x.find_element(by=locateType, value=locateExpression))
        return element
    except Exception, e:
        raise e


# 获取多个相同页面元素对象，以list返回
def getElement(driver, locateType, locateExpression):
    try:
        elements = WebDriverWait(driver, 5).until(lambda x: x.find_elements(by=locateType, value=locateExpression))
        return elements
    except Exception, e:
        raise e


if __name__ == '__main__':
    # 测试代码
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe')
    driver.get('http://www.baidu.com')
    searchBox = getElement(driver, 'xpath', "//input[@id='kw']")
    driver.quit()