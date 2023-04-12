#coding:utf-8

from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import traceback
from PageObject.LoginPage import *
from PageObject.AddressBook import *
from Action.add_contact import *
from Action.login import *
from ProjectVar.var import *
from Util.Excel import *
from Util.log import *
from Util.FormatTime import *

# driver = webdriver.Firefox(executable_path='F:\\Mozilla Firefox')
driver = webdriver.Chrome(executable_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe")
driver.get('http://mail.126.com')
pe = parseExcel(r"G:\python\-dataDrivenTestPractice1\TestData\mail.xlsx")
pe.set_sheet_by_name(u'126帐号')
print (pe.get_default_sheet())
rows = pe.get_all_rows()[1:]

for id, row in enumerate(rows):
    if row[4].value == 'y':
        username = row[1].value
        password = row[2].value
        print (username, password)

        try:
            login(driver, username, password)
            pe.set_sheet_by_name(u'联系人')
            print (pe.get_default_sheet())
            rows1 = pe.get_all_rows()[1:]
            print ('rows1:', rows1)
            test_data_pass_flag=True#结果表示，用于最后写入excel结果

            for id1, row in enumerate(rows1):
                if row[7.].value == 'y':
                    try:
                        # print row[1].value, row[2].value, row[3].value, row[4].value, row[5].value
                        # print 'execute1'
                        print ("log0711", row[1], row[1].value)
                        print ("log0711", type(row[1].value))
                        #进行添加联系人的实际操作
                        add_contact(driver, row[1].value, row[2].value, row[3].value, row[4].value, row[5].value)
                        print ('assert word:', row[6].value in driver.page_source)
                        print (row[6].value)
                        pe.write_cell_content(id1+2, 10, 'pass')#assert没有报错，说明断言成功
                    except Exception as e:
                        print (u'异常信息:' ,e.message)
                        pe.write_cell_content(id1+2, 10, 'fail')
                        pe.write_cell_content(id1+2, 9, date_time())
                        test_data_pass_flag=False#代码走到这里，说明有异常，测试失败
                        info(u'异常信息' + e.message)#输出日志
                else:#说明标识为n，忽略该数据
                    pe.write_cell_content(id1+2, 10, u'忽略')
                    pe.write_cell_content(id1 + 2, 9, date_time())
                    continue
            if test_data_pass_flag == True:#如果标识是Ture，说明结果是成功
                pe.set_sheet_by_name(u'126帐号')
                pe.write_cell_content(id+2, 5, '成功')
            else:#说明标识是false
                pe.set_sheet_by_name(u'126帐号')
                pe.write_cell_content(id + 2, 5, '失败')
        except Exception as e:
            pe.set_sheet_by_name(u'126帐号')
            # print u'异常信息', e
            pe.write_cell_content(id+2, 6, 'fail')
            info(u'异常信息02:'+e.message)#输出日志
        time.sleep(2)
        driver.quit()
    else:#走这个分支，说明标识为n
        pe.set_sheet_by_name(u'126帐号')
        pe.write_cell_content(id+2, 6, u'忽略')
        continue
# login(driver, "stavaea", "wxy900418")
# add_contact(driver, '王xx', '451009894@qq.com', True, '18511437672', 'my life')
# driver.quit()

# lp = LoginPage(driver)

# loginPage = LoginPage(driver)
# addressBook = AddressBook(driver)
# loginPage.login()
# addressBook.add_content()
# wait = WebDriverWait(driver, 10, 0.2)

# try:
#     lp.login()
#     wait = WebDriverWait(driver, 10, 0.2)
#     driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='x-URS-iframe']"))#切换到用户名和密码输入框所在的frame元素
#     name = wait.until(lambda x: x.find_element_by_xpath("//input[@placeholder='邮箱帐号或手机号' and @name='email']"))
#     name.send_keys('stavaea')
#     password = wait.until(lambda x: x.find_element_by_xpath("//input[@placeholder='密码']"))
#     password.send_keys('wxy900418')
#     submit = wait.until(lambda x: x.find_element_by_xpath("//a[@id='dologin']"))
#     submit.click()
#     driver.switch_to.default_content()#在pycharm里用switch_to_default_content会被加删除线
#     time.sleep(5)
#     assert u'退出' in driver.page_source, "no exist in page_source"
#     address_book_link = wait.until(lambda x: x.find_elements_by_xpath('//div[text()="通讯录"]'))
#     address_book_link.click()
#     # assert u'新建联系人' in driver.page_source
#     add_contact_button = wait.until(lambda x: x.find_elements_by_xpath('//span[text()="新建联系人"]'))
#     address_book_link.click()
#     contact_name = wait.until(lambda x: x.find_elements_by_xpath('//a[@title="编辑详细姓名"]/preceding-sibling::div/input'))
#     contact_name.send_keys('王xx')
#     contact_email = wait.until(lambda x: x.find_elements_by_xpath('//*[@id="iaddress_MAIL_wrap"]//input'))
#     contact_email.send_keys('451009894@qq.com')
#     contact_is_star = wait.until(lambda x: x.find_elements_by_xpath('//span[text()="设为星标联系人"]/preceding-sibling::span/b'))
#     contact_is_star.click()
#     contact_mobile = wait.until(lambda x: x.find_elements_by_xpath('//*[@id="iaddress_TEL_wrap"]//dd//input'))
#     contact_email.send_keys('18511437672')
#     contact_other_info = wait.until(lambda x: x.find_elements_by_xpath('//textarea'))
#     contact_email.send_keys('my life')
#     contact_save_button = wait.until(lambda x: x.find_elements_by_xpath('//span[.="确定"]'))
#     contact_save_button.click()
# except TimeoutException, e:
#     #捕获TimeoutException异常
#     print traceback.print_exc()
#
# except NoSuchElementException, e:
#     #捕获NoSuchElementException异常
#     print traceback.print_exc()
#
# except Exception, e:
#     #捕获其他异常
#     print traceback.print_exc()