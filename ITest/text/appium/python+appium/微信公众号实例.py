#coding:utf-8

'''微信其实就是一个混合的app，客户端里嵌入的webview，app中的native可以用uiautomatorviewer来查看元素，但webview里是不行的，但是可以使用chrome来查看。

01
手机设置

如何查看微信webview中的元素，几个前提：

1、手机打开【开发者模式】

2、app必须是debug模式

3、手机通过USB连接电脑，且能够识别出来手机，如下图。如果识别不了，请自行百度。


02
chrome设置

有了这几个前提之后就可以正式开始了

1、打开微信，在任意对话框中输入debugx5.qq.com并发送

2、点击发送成功的debugx5.qq.com，稍等片刻进入设置页面

3、切换到【信息】，勾选【是否打开tbs内核】，如下图


 4、打开chrome，地址栏输入chrome://inspect/#devices，可以看到设备或者你访问的资源，如果查看不到请自行百度，如下图


 5、点击上图中【寄件】对应的【inspect】就可以看到页面了，接下来就可以轻松识别元素了，和用f12查看元素没有区别，如果你不会请面壁思过。

（此处需要翻墙或者通过其他方式，请自行解决，否则显示的是白页）


03
appium中的chromedriver替换成手机webview对应的版本
由于app的webview自动化是依赖于chromedriver的，并且每个手机app的webview版本号都不太一样，版本不匹配的话一般会报错：

An unknown server-side error occurred while processing the command.

Original error: unknown error: Chrome version must be >= 55.0.2883.0

appium里面chromedriver版本的路径地址，appium1.7以后版本默认安装在c盘，找到如下路径可以看版本号，笔者的chromedriver路径如下：

C:\Users\HP\AppData\Local\appium-desktop\app-1.5.0\resources\app\node_modules\appium\node_modules\appium-chromedriver\chromedriver\win

1、找到手机APP的webview的版本

[设置] ->【更多设置】->【应用程序】->【全部】，如下图


 再查看webview详情，找到版本号，笔者的版本为55.0.2883.91，如下图：


 2、下载与webview版本对应的chromedriver


下载链接：

https://chromedriver.storage.googleapis.com/index.html

3、将下载后的chromedriver.exe覆盖appium中的chromedriver。

最后再重启appium。

04
代码要点
1、desired_caps增加'chromeOptions'

'chromeOptions':{'androidProcess': 'com.tencent.mm:tools'}

2、如果是webview元素，使用下面的语句切换到webview

driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')

通过以下语句，查看webview名称：

contexts=driver.contexts

print contexts

3、切换到webview里面，剩下的定位方式和web一模一样

4、如果返回原生态的native，用下面的语句

driver.switch_to.context("NATIVE_APP")

5、对于webview与native的判断，笔者经过尝试，通过uiautomatorviewer可以识别的控件就按照native的方式定位；反之就切换到webview，按照web元素的定位方式定位。
'''

from appium import webdriver
import time

desired_caps = {
                'platformName': 'Android',
                'platformVersion': '7.1.2',
                'deviceName': '60c9dcf1',
                'appPackage': 'com.tencent.mm',
                'appActivity': '.ui.LauncherUI',
                # 'automationName': 'Appium',
                'unicodeKeyboard': True,
                'resetKeyboard': True,
                'noReset': True,#如果程序已安装了，不需重置，设置为True
                'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'}
                }

#启动微信，等待加载
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(5)

#搜索公众号‘e栈快递柜’，进入‘我的->我的快递’界面
driver.find_element_by_xpath("//*[@content-desc='搜索']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@text='搜索']").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@text='搜索']").send_keys(u'e栈快递柜')
time.sleep(3)
driver.find_element_by_xpath("//*[@text='e栈快递柜'and @resouce-id='com.tencent.mm:/id/nr']/ancestor::*[1]/parent::*").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@text='我的']").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@text='我的快递']").click()
time.sleep(3)

#在‘我的快递’界面，是webview页面，要切入webview，再操作元素
driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
time.sleep(3)
driver.find_element_by_id("//*[@content-desc='返回']").click()
time.sleep(3)

#在‘我的快递’界面上方的返回图标‘X’是native，要切回native，再操作元素
driver.switch_to.context("NATIVE_APP")
driver.find_element_by_xpath("//*[@content-desc='返回']").click()
time.sleep(3)
driver.quit()


