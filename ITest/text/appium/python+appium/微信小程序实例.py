#coding:utf-8

'''微信小程序不过是正常的webview而已. 只是产品概念上的不同. 本质还是h5。所以用appium是可以进行自动化的。
以下例子中，都是native元素，与手机APP的元素定位方式一模一样。

笔者也试过几个小程序，基本都是native元素，如果存在webview的元素，请参考下一篇微信公众号自动化实例的文章。'''

from appium import webdriver
import time
desired_caps = {
                'platformName': 'Android',
                'platformVersion': '7.1.2',
                'deviceName': '60c9dcf1',
                'appPackage': 'com.tencent.mm',
                'appActivity': '.ui.LauncherUI',
                'automationName': 'Appium',
                # 'unicodeKeyboard': True,
                # 'resetKeyboard': True,
                'noReset': True,#如果程序已安装了，不需重置，设置为True
                }

def swipeDown(driver, t=500, n=1):
    '''向下滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.5      #x坐标
    y1 = l['heigth'] * 0.25    #起始y坐标
    y2 = l['heigth'] * 0.75    #终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)

#启动微信，等待加载
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(5)

#向下滑动，显示小程序图标
swipeDown(driver)
time.sleep(2)

#点开小程序，下面例子中使用'芭比商城'小程序
driver.find_elements_by_id("com.tencent.mm:id/t7")[0].click()
time.sleep(3)

#在小程序界面，进行下单付款操作
driver.find_element_by_xpath("//*[@content-desc='一键订餐']/parent::*").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@content-desc='公告：欢迎光临，很高兴为您服务']/parent::*/following-sibling::*[1]//*[@content-desc='馒头']").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@content-desc='葱油花卷']/following-sibling::*[2]/android.view.View").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@content-desc='去结算']").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@content-desc='确认支付']").click()
time.sleep(3)
driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/bvs"]/android.widget.RelativeLayout').send_keys("875493")
time.sleep(3)
driver.quit()

'''小提示
1、 'noReset': True设置：如果程序安装了，不需重置，则设置为True，否则每次程序都重置为第一次安装后的状态。

2、 appium自动化测试中，建议操作元素定位封装成函数，并设置显式等待时间，否则每个控件定位都需要设置等待时间，
在硬件环境复杂、网络情况不好的情况下，程序容易出现异常情况。

3、 微信小程序或者app中的元素比较难定位，建议多使用xpath中的轴定位、属性定位、以及相对路径的定位方式。

4、 在元素定位表达式正确，元素仍定位不到的情况下，或者程序偶尔出现异常，建议增加等待时间，或者重启appium试试。'''