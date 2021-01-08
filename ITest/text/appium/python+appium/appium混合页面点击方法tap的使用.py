#coding:utf-8

from selenium.webdriver.common.touch_actions import TouchActions

def tap_element(locationType, locationExpression):
    try:
        element = getElement(driver, locationType=locationType, locationExpression=locationExpression)#element可根据自己的方式获取
        tas = TouchActions(driver)
        tas.tap(element).perform()
    except Exception as e:
        raise e

if __name__ == '__main__':
    launchApp_smy_noReset()#启动app，此方法自己封装
    sleep(10)#留足够时间点击到调试页，也可用程序跳转到h5页面
    switch_to_webview()#切换到webview
    tap_element('xpath', '//*[@id="detail"]/div[4]/a[2]')#调用刚封装好的tap_element方法

    print 'click  success'
    switch_to_native()#切换到原生
    print 'switch_to  success'
