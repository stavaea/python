#coding:utf-8
import time
from datetime import timedelta,date
import locale

# locale.setlocale(locale.LC_CTYPE, 'chinese')
def date_time_chinese():
    u'returns the current time string,format for YYYY年mm月dd日 HH时MM分SS秒'
    return time.strftime('%Y年%m月%d日 %H时%M分%S秒', time.localtime())