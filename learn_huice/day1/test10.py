a = "hello,world"
a = 'hello,world'

# let's go!
a = 'let\'s go!'
a = "let's go!"

# "hello"."world"
a = "\"hello\".\"world\""
a = '"hello"."world"'

a = ''' this is a very long string.
It continues here.
and it's not over yet.
'''
print a

a = 'hello world'
print repr(a)
print str(a)

b = 'hello, world\n'
print repr(b)
print str(b)

c = 100L
print repr(c)
print str(c)

