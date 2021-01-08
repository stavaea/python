name = 'HelloWorld'

# print len(name)
#
# print name[0]
# print name[9]
# print name[-1]
# print name[8] == name[-2]

count = len(name)
for i in range(0, count):
    print name[i]

print '-------------------'

count = -len(name)
for i in range(-1, count-1, -1):
    print name[i]

print name[0:10]
print name[5:]
print name[:5]
print name[:]
print name[0:6:2]
print name[::2]
print name[::-2]
print name[::-1]

# string "copy"
result = name[:]
print result is name

# list "copy"
name = [1, 2, 3]
result = name[:]
print result is name