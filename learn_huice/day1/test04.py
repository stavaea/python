# coding:utf-8

# 请写出以下程序的运行结果
a = 1
b = 1
print id(a) == id(b)
print (a is b)

a = 2;
print id(a) == id(b)


c = "very good morning"
d = "very good morning"
print id(c) == id(d)

c = True
d = True
print id(c) == id(d)


e = [1, 2, 3]
f = [1, 2, 3]
print id(e) == id(f)
print e == f
print e is f

g = [4, 5, 6]
id1 = id(g)
g.append(7)
id2 = id(g)
print id1 == id2


