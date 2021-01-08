str = "this is string example....wow!!! this is really string"
print str.replace("is", "was")
print str.replace("is", "was", 3)

sStr1 = 'strch'
sStr2 = 'strch'
print cmp(sStr1, sStr2)

str3 = 'hello'
print str3.find('l')
print str3.find('ello')
print str3.find('l', 3)
print str3.find('l', 0, 2)

print str3.index('ello')
# print str3.index('elo')

info = 'name:haha,age:20$name:python,age:30$name:fef,age:55'
content = info.split('$')
print type(content)
print content

content = info.split('$', 1)
print content
#
content = info.split()
print content
#
info = "hello world my name is python"
content = info.split()
print content
print content[len(content)-1]

