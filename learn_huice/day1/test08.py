a = 123
b = 123

print a is b
print a == b

a = 456
print a is b
print a == b

a = 'aaaaaa aaaaa'
b = 'aaaaaa aaaaa'
print a is b
print a == b

a = [1, 2, 3]
b = [1, 2, 3]
print a is b
print a == b


def a():
    print 'A'
    return 1

def b():
    print 'B'

def c():
    print 'C'
    return 1

def d():
    print 'D'
    return []

if a() or b() or c() or d():
    print 'ok'
