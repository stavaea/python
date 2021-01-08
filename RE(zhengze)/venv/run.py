#coding:utf-8
from Util.excel import *
from ProjectVar.var import *
import requests
from Action.search_keyword import *
from Util.write_excel import *
from Action.optimiza_result import *


eins = Excel_r_w(excel_path, 'used_sheet')
max_col=eins.get_max_row()
driver = webdriver.Firefox(executable_path=r'火狐路径')

for ir in range(2, eins.get_max_row()+1):
    keyword = CrawlKW(driver, eins.get_value('B'+str(ir)), eins.get_value('C'+str(ir)))
    write_resul(eins, 'E'+str(ir), str(keyword))
driver.quit()