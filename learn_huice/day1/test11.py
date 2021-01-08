#-*- coding:utf-8 –*-

a = '中文'
print a



# 命令行用的是cp936编码，而脚本用的是utf-8编码
# 方式一 解码再重新编码
print a.decode('utf-8').encode('cp936')

# 方式二 Unicode字符串
a = u'中文'
print a

# 1
print "I am %d years old." % 22
print "I am %s years old." % 22
print "I am %r years old." % 22

# 2
text = "I am %d years old." % 22
print "I said: %s." % text
print "I said: %r." % text

# 3
import datetime
d = datetime.date.today()
print "%s" % d
print "%r" % d


string = 'Hello, %s' % 'world'
print string

name = u'刘则'
month = 9
fee = 50.00
total = 49.99
string = u'亲爱的%s你好！你%d月的话费是%.2f，余额是%.2f' % (name, month, fee, total)
print string


