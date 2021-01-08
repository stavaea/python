#coding=utf-8
a = True
b = False

not(a and b)
print ('(a and b) = ', (a and b))
print ('(a or b) = ', (a or b))
print ('not(a and b) = ', not(a and b))

a = 10
b = 20
list = [1, 2, 3, 4, 5]

if ( a in list ):
   print ("a 存在")
else:
   print ("a 不存在")

c = b/a
if ( c in list ):
   print ("c 存在")
else:
   print ("c 不存在")