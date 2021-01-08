# -*- coding:UTF-8 -*-

str = '慧测'

print str.decode('utf-8').encode('gbk')

a = [1, 2]
b = [1, 2]
print id(a)
print id(b)

"""
不可变数据类型
#数字 字符串 元组 布尔值

引用计数
"""
print type(1)     #查询数据类型

#float lang int

print ord('A')  #整数转换ASCII码
print chr(97)   #字符转换ASCII码

a = 'i" \'m xxx'    #

print r''  #r代表原始字符串

str = "Bob said\ni'm ok"
str = """Bob said
i'm ok"""

str = r'路径/正则'
print (str)

a = 10
b = 3
#if x%2==0

print()


name = 'AJ'
mouth = '12'
money = '50.0'
free = '21.12'
print "亲爱的%s,你好！你%s月的话费是%s,余额是%s" % (name, mouth, money, free)

info = "亲爱的{name},你好！你{mouth}月的话费是{money},余额是{free}"
#info = "亲爱的[0],你好！你[1]月的话费是[2],余额是[3]"
info = info.format(name='AJ', mouth='12', money=50.0, free='21.12')
#info = info.format(AJ,1,100,20.09)
print info

str = '{protocol}://{domin}/{url}?data'
protocol = 'http'
domin = '192.168.2.111'
url = 'huice/event/api/add'
data = 'title=python大会&time=2018-01-06'
# get = "%s://%s/%s?%s"
# get = get.format(protocol='http', domin='192.168.2.111', url='huice/event/api/add', data='title=python大会&time=2018-01-06')
print str.format(protocol=protocol,
                 domin=domin,
                 url=url,
                 data=data)


str = """def test_{case}(self):
    '{desc}'
    execute_case({data})
"""
case = 'case01'
desc = '测试用例1'
data = 'id=1'
print str.format(case=case,
                 desc=desc,
                 data=data)


a = '￥3010元'
b = a[3:-3]
print (b)

# str.replace() 替换
# str.cmp 比较
# str.find()  查找
# str.split() 切割


a = 'title=华为春季新品发布会&sign=0&limit=100&status=0&address=国家会议中心&time=2018-03-28'
b = a.split('&')
# for sign in b:
#     str.replace('')

print b
