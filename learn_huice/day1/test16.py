a = eval('1+2')
print a

b = '[1,2,3]'
print type(eval(b))
print b
#
# code = "[x for x in range(10)]"
# print eval(code)
#
input_str = "__import__('os').system('dir')"
eval(input_str)
