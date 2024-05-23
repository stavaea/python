#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/23 15:06
@Author  : waxberry
@File    : 字符串常用操作.py
@Software: PyCharm
"""

# 字符串切片操作
test = "Python Programming"
print("String: ", test)

# First one character
first_character = test[:1]
print("First Character: ", first_character)

# Last one character
last_character = test[-1:]
print("Last Character: ", last_character)

# Everything except the first one character
except_first = test[1:]
print("Except First Char.: ", except_first)

# Everything except the last one character
except_last = test[:-1]
print("Except First Char.: ", except_last)

# Everything between first and last two character
between_two = test[2:-2]
print("Between two character: ", between_two)

# Skip one character
skip_one = test[0:18:2]  # [start:stop:step]
print("Skip one character: ", skip_one)

# Reverse String
reverse_str = test[::-1]
print("Reverse String: ", reverse_str)



# 检查字符串是否为空
import re
from collections import Counter

sentence = 'Canada is located in the northern part of North America'
# Example I
counter = len(re.findall("a", sentence))
print(counter)

# Example II
counter = sentence.count('a')
print(counter)

# Example III
counter = Counter(sentence)
print(counter['a'])



# 计算字符串中字符出现次数的多种方法
import re
from collections import Counter

sentence = 'Canada is located in the northern part of North America'
# Example I
counter = len(re.findall("a", sentence))
print(counter)

# Example II
counter = sentence.count('a')
print(counter)

# Example III
counter = Counter(sentence)
print(counter['a'])




# 将String变量转换为float、int或boolean
# String to Float
float_string = "254.2511"
print(type(float_string))

string_to_float = float(float_string)
print(type(string_to_float))

# String to Integer
int_string = "254"
print(type(int_string))

string_to_int = int(int_string)
print(type(string_to_int))

# String to Boolean
bool_string = "True"
print(type(bool_string))

string_to_bool = bool(bool_string)
print(type(string_to_bool))



# 向字符串填充或添加零的不同方法
num = 7

print('{0:0>5d}'.format(num))  # left
print('{0:0<5d}'.format(num))  # right

print('{:05d}'.format(num))

print("%0*d" % (5, num))
print(format(num, "05d"))

temp = 'test'
print(temp.rjust(10, '0'))
print(temp.ljust(10, '0'))



# 去掉字符串中的space字符
string_var = "  \t a string example\n\t\r  "
print(string_var)

string_var = string_var.lstrip()  # trim white space from left
print(string_var)

string_var = "  \t a string example\t  "
string_var = string_var.rstrip()  # trim white space from right
print(string_var)

string_var = "  \t a string example\t  "
string_var = string_var.strip()  # trim white space from both side
print(string_var)




# 生成N个字符的随机字符串
import string
import random
def string_generator(size):
    chars = string.ascii_uppercase + string.ascii_lowercase
    return ''.join(random.choice(chars) for _ in range(size))


def string_num_generator(size):
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))


# Random String
test = string_generator(10)
print(test)

# Random String and Number
test = string_num_generator(15)
print(test)



# 以不同的方式反转字符串
test_string = 'Python Programming'
string_reversed = test_string[-1::-1]
print(string_reversed)

string_reversed = test_string[::-1]
print(string_reversed)

# String reverse logically
def string_reverse(text):
    r_text = ''
    index = len(text) - 1

    while index >= 0:
        r_text += text[index]
        index -= 1

    return r_text

print(string_reverse(test_string))

# 将Camel Case转换为Snake Case并更改给定字符串中特定字符的大小写
import re

def convert(oldstring):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', oldstring)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

# Camel Case to Snake Case
print(convert('CamelCase'))
print(convert('CamelCamelCase'))
print(convert('getHTTPResponseCode'))
print(convert('get2HTTPResponseCode'))

# Change Case of a particular character
text = "python programming"
result = text[:1].upper() + text[1:7].lower() \
         + text[7:8].upper() + text[8:].lower()
print(result)

text = "Kilometer"
print(text.lower())

old_string = "hello python"
new_string = old_string.capitalize()
print(new_string)

old_string = "Hello Python"
new_string = old_string.swapcase()
print(new_string)

# 检查给定的字符串是否是Python中的回文字符串
import re

Continue = 1
Quit = 2

def main():
    choice = 0

    while choice != Quit:
        # Display the menu.
        display_menu()
        # Constant to assume string is Palindrome
        is_palindrome = True

        # Get the user's choice.
        choice = int(input('\nEnter your choice: '))

        # Perform the selected action.
        if choice == Continue:
            line = input("\nEnter a string: ")
            str_lower = re.sub("[^a-z0-9]", "", line.lower())
            for i in range(0, len(str_lower) // 2):
                if str_lower[i] != str_lower[len(str_lower) - i - 1]:
                    is_palindrome = False

            if is_palindrome:
                print(line, "is a palindrome")
            else:
                print(line, "is not a palindrome")
        else:
            print('Thank You.')

def display_menu():
    print('\n*******MENU*******')
    print('1) Continue')
    print('2) Quit')

main()



# 检查字符串是否以列表中的一个字符串结尾
str_list = ['aaa', 'bbb', 'ccc', 'ddd']  # list of items
str_test = 'testccc'  # string need to test

for str_item in str_list:
    if str_test.endswith(str_item):
        print("found")
        break  # loop ends when result found
    else:
        print("not found")



# 在字符串中应用查找模式
import re
s1 = 'abccba'
s2 = 'abcabc'
s3 = 'canadajapanuaeuaejapancanada'
p = '123321'

def match(s, p):
    nr = {}
    regex = []
    for c in p:
        if c not in nr:
            regex.append('(.+)')
            nr[c] = len(nr) + 1
        else:
            regex.append('\\%d' % nr[c])
    return bool(re.match(''.join(regex) + '$', s))

print(match(s1, p))
print(match(s2, p))
print(match(s3, p))



# 如果是 Python 中的反斜杠，则删除最后一个字符
x = 'Canada\\'
print(x.rstrip('\\'))



# 在Python中拆分字符串而不丢失拆分字符
import re
string = 'canada-japan-india'

print(re.split(r'(\-)', string))



# 从字符串 Python 中提取大写和小写字符
string = "asdfHRbySFss"

uppers = [l for l in string if l.isupper()]
print (''.join(uppers))

lowers = [l for l in string if l.islower()]
print (''.join(lowers))



# 如何在 Python 中比较字符串的索引是否相等
myString = 'AAABBB'
for idx, char in enumerate(myString, ):
    if idx + 1 == len(myString):
        break
    if char == myString[idx + 1]:
        print(idx, char, myString[idx + 1])



# 在每个第 4 个字符上添加空格
string = 'Test5412Test8745Test'
print([string[i:i + 4] for i in range(0, len(string), 4)])



# 在 Python 中以多行方式连接字符串
str1 = "This is a demo string"
str2 = "This is another  demo string"
strz = ("This is a line\n" +
       str1 + "\n" +
       "This is line 2\n" +
       str2 + "\n" +
       "This is line 3\n")

print(strz)



# 在 Python 中将多个变量附加到列表中
volumeA = 100
volumeB = 20
volumeC = 10

vol1 = []
vol2 = []

vol1.extend((volumeA, volumeB, volumeC))
vol2 += [val for name, val in globals().items() if name.startswith('volume')]

print(vol1)
print(vol2)



# 将字符串拆分为 Python 中的字符列表
s = 'canada'
l = list(s)
print(l)



# 如何在 Python 中小写字符串
text = ['Canada', 'JAPAN']

text = [txt.lower() for txt in text]
print(text)

# 通过多个标点符号分割字符串
import re

s = 'a,b,c d!e.f\ncanada\tjapan&germany'

l = re.split('[?.,\n\t&! ]', s)

for i in l:
    print(i)



# Python 字符串填充
lines_of_text = [
    (123, 5487, 'Testing', 'Billy', 'Jones'),
    (12345, 100, 'Test', 'John M', 'Smith')
]

for mytuple in lines_of_text:
    name = '{}, {}'.format(mytuple[4], mytuple[3])
    value = '$' + str(mytuple[1])
    print('{name:<20} {id:>8} {test:<12} {value:>8}'.format(
        name=name, id=mytuple[0], test=mytuple[2], value=value)
    )



# 在 Python 中检查两个字符串是否包含相同的字符
str1 = 'caars'
str2 = 'rats'
str3 = 'racs'

print(set(str1)==set(str2))
print(set(str1)==set(str3))



# 在 Python 中查找给定字符串中的整个单词
def contains_word(s, w):
    return (' ' + w + ' ') in (' ' + s + ' ')


result = contains_word('those who seek shall find', 'find')
print(result)
result = contains_word('those who seek shall find', 'finds')
print(result)



# 查找所有出现的子字符串
import re

aString = 'this is a string where the substring "is" is repeated several times'
print([(a.start(), a.end()) for a in list(re.finditer('is', aString))])



# 在 Python 中去除所有开头在Python中的正斜杠上拆分字符串和结尾标点符号
from string import punctuation
s = '.$958-5-Canada,#'

print(s.strip(punctuation))



# 用Python中的正斜杠上拆分字符串
s = 'canada/japan/australia'
l = s.split('/')

print(l)



# 根据 Python 中的索引位置将字符串大写
def capitalize(s, ind):
    split_s = list(s)
    for i in ind:
        try:
            split_s[i] = split_s[i].upper()
        except IndexError:
            print('Index out of range : ', i)
    return "".join(split_s)


print(capitalize("abracadabra", [2, 6, 9, 10, 50]))



# 检查字符串中的所有字符是否都是Python中的数字
a = "1000"
x = a.isdigit()
print(x)

b = "A1000"
x = b.isdigit()
print(x)



# 为什么使用'=='或'is'比较字符串有时会产生不同的结果
a = 'canada'
b = ''.join(['ca', 'na', 'da'])
print(a == b)
print(a is b)

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(a is b)

c = b
print(c is b)



# 如何在 Python 中为字符串添加 X 个空格
print('canada'.ljust(10) + 'india'.ljust(20) + 'japan')



# 如何在Python中替换字符串中的特定字符串实例
def nth_replace(str,search,repl,index):
    split = str.split(search,index+1)
    if len(split)<=index+1:
        return str
    return search.join(split[:-1])+repl+split[-1]

str1 = "caars caars caars"
str2 = nth_replace(str1, 'aa', 'a', 1)

print(str2)



# 如何连接两个变量，一个是字符串，另一个是 Python 中的 int
int1 = 10
str1 = 'test'

print(str(int1) + str1)



# 在 Python 中的反斜杠上拆分字符串
s = r'canada\japan\australia'
l = s.split('\\')

print(l)



# 在Python中随机大写字符串中的字母
from random import choice

x = "canada japan australia"
print(''.join(choice((str.upper, str.lower))(c) for c in x))



# 在单词处拆分字符串并且或不保留分隔符
import re

string = "Canada AND Japan NOT Audi OR BMW"

l = re.split(r'(AND|OR|NOT)', string)
print(l)



# 在Python中填充n个字符

def header(txt: str, width=30, filler='*', align='c'):
    assert align in 'lcr'
    return {'l': txt.ljust, 'c': txt.center, 'r': txt.rjust}[align](width, filler)

print(header("Canada"))
print(header("Canada", align='l'))
print(header("Canada", align='r'))



# 检查变量是否等于一个字符串或另一个字符串
x = 'canada'

if x in ['canada', 'japan', 'germany', 'australia']:
    print("Yes")



# Python字符串格式化固定宽度
num1 = 0.04154721841
num2 = 10.04154721841
num3 = 1002.04154721841

print ("{0:<12.11g}".format(num1)[:12])
print ("{0:<12.11g}".format(num2)[:12])
print ("{0:<12.11g}".format(num3)[:12])



# 在Python中查找字符串中字符的所有位置
test = 'canada#japan#uae'
c = '#'
print([pos for pos, char in enumerate(test) if char == c])



# 在Python中从左右修剪指定数量的空格
def trim(text, num_of_leading, num_of_trailing):
    text = list(text)
    for i in range(num_of_leading):
        if text[i] == " ":
            text[i] = ""
        else:
            break

    for i in range(1, num_of_trailing+1):
        if text[-i] == " ":
            text[-i] = ""
        else:
            break
    return ''.join(text)


txt1 = "   Candada     "
print(trim(txt1, 1, 1))
print(trim(txt1, 2, 3))
print(trim(txt1, 6, 8))



# 在Python中按字符串中字符的位置拆分字符串
str = 'canadajapan'
splitat = 6
l, r = str[:splitat], str[splitat:]
print(l)
print(r)



# 将Python字符串中的第一个和最后一个字母大写
string = "canada"

result = string[0:1].upper() + string[1:-1].lower() + string[-1:].upper()
print(result)



# 检查字符串是否以Python中的给定字符串或字符结尾
txt = "Canada is a great country"

x = txt.endswith("country")

print(x)



# 如何在Python中比较两个字符串
str1 = "Canada"
str2 = "Canada"
print(str1 is str2)  # True
print(str1 == str2)  # True

string1 = ''.join(['Ca', 'na', 'da'])
string2 = ''.join(['Can', 'ada'])
print(string1 is string2)  # False
print(string1 == string2)  # True



# 在Python中将整数格式化为带有前导零的字符串
x = 4
x = str(x).zfill(5)
print(x)



# 在Python中替换字符串的多个子字符串
s = "The quick brown fox jumps over the lazy dog"
for r in (("brown", "red"), ("lazy", "quick")):
    s = s.replace(*r)

print(s)



# Python字符串替换字符
s = "The quick brown fox jumps over the lazy dog"
for r in (("brown", "red"), ("lazy", "quick")):
    s = s.replace(*r)

print(s)



# 在Python中查找字符串中所有出现的单词的所有索引
import re

sentence = 'this is a sentence this this'
word = 'this'

for match in re.finditer(word, sentence):
    print(match.start(), match.end())



# 在 Python 中将字符串中每个单词的首字母大写
import string

x = "they're bill's friends from the UK"
x = string.capwords(x)
print(x)

x = x.title()
print(x)



# 仅在 Python 中的双引号后拆分字符串
s = '"Canada", "Japan", "Germany", "Russia"'
l = ['"{}"'.format(s) for s in s.split('"') if s not in ('', ', ')]

for item in l:
    print(item)



# 在 Python 中以字节为单位获取字符串的大小
string1 = "Canada"
print(len(string1.encode('utf-16')))



# 在 Python 中比较字符串中的字符
myString = 'AAABBB'
for idx, char in enumerate(myString, ):
    if idx + 1 == len(myString):
        break
    if char == myString[idx + 1]:
        print(idx, char, myString[idx + 1])



# 在 Python 中的括号和字符串之间添加空格
import re

test = "example(test)"
test2 = "example(test)example"
test3 = "(test)example"
test4 = "example (test) example"

for i in [test, test2, test3, test4]:
    print(re.sub(r"[^\S]?(\(.*?\))[^\S]?", r" \1 ", i).strip())



# 在 Python 中删除开头和结尾空格
s = '   canada   '
print(s.strip())



# 在 Python 中拆分字符串以获得第一个值
s = 'canada-japan-australia'
l = s.split('-')[0]
print(l)

string = 'canada-japan-australia'
print(string[:string.index('-')])



# 在 Python 中检查字符串是大写、小写还是混合大小写
words = ['The', 'quick', 'BROWN', 'Fox',
         'jumped', 'OVER', 'the', 'Lazy', 'DOG']

print([word for word in words if word.islower()])

print([word for word in words if word.isupper()])

print([word for word in words if not word.islower() and not word.isupper()])




# Python计数字符串出现在给定字符串中
txt = "I love Canada, Canada is one of the most impressive countries in the world. Canada is a great country."

x = txt.count("Canada")

print(x)



# 在 Python3 中用前导零填充字符串
hour = 4
minute = 3

print("{:0>2}:{:0>2}".format(hour, minute))
print("{:0>3}:{:0>5}".format(hour, minute))
print("{:0<3}:{:0<5}".format(hour, minute))
print("{:$<3}:{:#<5}".format(hour, minute))



# 在 Python 中检查两个字符串是否包含相同的字母和数字
from string import ascii_letters, digits

def compare_alphanumeric(first, second):
    for character in first:
        if character in ascii_letters + digits and character not in second:
            return False
    return True

str1 = 'ABCD'
str2 = 'ACDB'
print(compare_alphanumeric(str1, str2))

str1 = 'A45BCD'
str2 = 'ACD59894B'
print(compare_alphanumeric(str1, str2))

str1 = 'A45BCD'
str2 = 'XYZ9887'
print(compare_alphanumeric(str1, str2))



# 在Python中的字符串中的字符之间添加空格的有效方法
s = "CANADA"

print(" ".join(s))
print("-".join(s))
print(s.replace("", " ")[1: -1])



# 在Python中查找字符串中最后一次出现的子字符串的索引
s = 'What is Canada famous for?'

print(s.find('f'))
print(s.index('f'))
print(s.rindex('f'))
print(s.rfind('f'))



# 在Python中将字符串大写
x = 'canada'
x = x.capitalize()

print(x)



# 拆分非字母数字并在 Python 中保留分隔符
import re

s = "65&Can-Jap#Ind^UK"
l = re.split('([^a-zA-Z0-9])', s)
print(l)



# 计算Python中字符串中大写和小写字符的数量
string = "asdfHRbySFss"

uppers = [l for l in string if l.isupper()]
print(len(uppers))

lowers = [l for l in string if l.islower()]
print(len(lowers))



# 在 Python 中将字符串与枚举进行比较
from enum import Enum, auto

class Signal(Enum):
     red = auto()
     green = auto()
     orange = auto()

     def equals(self, string):
          return self.name == string

brain_detected_colour = "red"
print(Signal.red.equals(brain_detected_colour))

brain_detected_colour = "pink"
print(Signal.red.equals(brain_detected_colour))



# Python中的段落格式
import textwrap

hamlet = '''\
Lorum ipsum is the traditional Latin placeholder text, used when a designer needs a chunk of text for dummying up a layout.
Journo Ipsum is like that, only using some of the most common catchphrases, buzzwords, and bon mots of the future-of-news crowd.
Hit reload for a new batch. For entertainment purposes only.'''

wrapper = textwrap.TextWrapper(initial_indent='\t' * 1,
                               subsequent_indent='\t' * 2,
                               width=40)

for para in hamlet.splitlines():
    print(wrapper.fill(para))



# 从 Python 中的某个索引替换字符
def nth_replace(str,search,repl,index):
    split = str.split(search,index+1)
    if len(split)<=index+1:
        return str
    return search.join(split[:-1])+repl+split[-1]

str1 = "caars caars caars"
str2 = nth_replace(str1, 'aa', 'a', 1)

print(str2)



# 如何连接 str 和 int 对象
i = 123
a = "foobar"
s = a + str(i)
print(s)



# 仅在 Python 中将字符串拆分为两部分
s = 'canada japan australia'
l = s.split(' ', 1)
print(l)



# 将大写字符串转换为句子大小写
text = ['CANADA', 'JAPAN']

text = [txt.capitalize() for txt in text]
print(text)



# 在标点符号上拆分字符串
string = 'a,b,c d!e.f\ncanada\tjapan&germany'
identifiers = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~\n\t '

listitems = "".join((' ' if c in identifiers else c for c in string)).split()

for item in listitems:
    print(item)



# 在Python中比较字符串
str1 = "Canada"
str2 = "Canada"
print(str1 is str2)  # True
print(str1 == str2)  # True

string1 = ''.join(['Ca', 'na', 'da'])
string2 = ''.join(['Can', 'ada'])
print(string1 is string2)  # False
print(string1 == string2)  # True



# 用零填充数字字符串
num = 123
print('{:<08d}'.format(num))
print('{:>08d}'.format(num))

string = '123'
print(string.ljust(8, '0'))
print(string.rjust(8, '0'))

print(string[::-1].zfill(8)[::-1])



# 找到两个字符串之间的差异位置
def dif(a, b):
    return [i for i in range(len(a)) if a[i] != b[i]]

print(dif('stackoverflow', 'stacklavaflow'))



# Python填充字符串到固定长度
number = 4

print(f'{number:05d}')  # (since Python 3.6), or
print('{:05d}'.format(number))  # or

print('{0:05d}'.format(number))
print('{n:05d}'.format(n=number))  # or (explicit `n` keyword arg. selection)
print(format(number, '05d'))



# Python中的字符串查找示例
import re

text = 'This is sample text to test if this pythonic '\
       'program can serve as an indexing platform for '\
       'finding words in a paragraph. It can give '\
       'values as to where the word is located with the '\
       'different examples as stated'

find_the_word = re.finditer('as', text)

for match in find_the_word:
    print('start {}, end {}, search string \'{}\''.
          format(match.start(), match.end(), match.group()))



# 删除字符串中的开头零和结尾零
list_num = ['000231512-n', '1209123100000-n00000',
            'alphanumeric0000', '000alphanumeric']

print([item.strip('0') for item in list_num])  # Remove leading + trailing '0'
print([item.lstrip('0') for item in list_num])  # Remove leading '0'
print([item.rstrip('0') for item in list_num])  # Remove trailing '0'



# Python在换行符上拆分
s = 'line 1\nline 2\nline without newline'
l = s.splitlines(True)

print(l)



# 将字符串中的每个第二个字母大写
s = 'canada'
s = "".join([x.upper() if i % 2 != 0 else x for i, x in enumerate(s)])

print(s)



# 在 Python 中查找一个月的最后一个营业日或工作日
import calendar

def last_business_day_in_month(year: int, month: int) -> int:
    return max(calendar.monthcalendar(year, month)[-1:][0][:5])

print(last_business_day_in_month(2021, 1))
print(last_business_day_in_month(2021, 2))
print(last_business_day_in_month(2021, 3))
print(last_business_day_in_month(2021, 4))
print(last_business_day_in_month(2021, 5))



# 比较两个字符串中的单个字符
def compare_strings(a, b):
    result = True
    if len(a) != len(b):
        print('string lengths do not match!')
    for i, (x, y) in enumerate(zip(a, b)):
        if x != y:
            print(f'char miss-match {x, y} in element {i}')
            result = False
    if result:
        print('strings match!')
    return result

print(compare_strings("canada", "japan"))



# 在 Python 中多次显示字符串
print('canada' * 3)
print(*3 * ('canada',), sep='-')



# Python从头开始替换字符串
def nth_replace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)

str1 = "caars caars caars caars caars"
str2 = nth_replace(str1, 'aa', 'a', 1)
print(str2)

str2 = nth_replace(str1, 'aa', 'a', 2)
print(str2)

str2 = nth_replace(str1, 'aa', 'a', 3)
print(str2)



# 在 Python 中连接字符串和变量值
year = '2020'

print('test' + str(year))
print('test' + year.__str__())



# 在每个下划线处拆分字符串并在第 N 个位置后停止
s = 'canada_japan_australia_us_uk'
l = s.split('_', 0)
print(l)

l = s.split('_', 1)
print(l)

l = s.split('_', 2)
print(l)



# Python中列表中第一个单词的首字母大写
text = ['johnny rotten', 'eddie vedder', 'kurt kobain',
           'chris cornell', 'micheal phillip jagger']

text = [txt.capitalize() for txt in text]
print(text)



# 如何在 Python 字符串中找到第一次出现的子字符串
test = 'Position of a character'
print(test.find('of'))
print(test.find('a'))



# 不同长度的Python填充字符串
data = [1148, 39, 365, 6, 56524]

for element in data:
    print("{:>5}".format(element))



# Python比较两个字符串保留一端的差异
def after(s1, s2):
    index = s1.find(s2)
    if index != -1 and index + len(s2) < len(s1):
        return s1[index + len(s2):]
    else:
        return None

s1 = "canada"
s2 = "can"

print(after(s1, s2))



# 如何用Python中的一个字符替换字符串中的所有字符
test = 'canada'
print('$' * len(test))



# 在字符串中查找子字符串并在 Python 中返回子字符串的索引
def find_str(s, char):
    index = 0

    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index + len(char)] == char:
                    return index

            index += 1

    return -1

print(find_str("India Canada Japan", "Canada"))
print(find_str("India Canada Japan", "cana"))
print(find_str("India Canada Japan", "Uae"))



# 从 Python 中的字符串中修剪特定的开头和结尾字符
number = '+91 874854778'

print(number.strip('+'))
print(number.lstrip('+91'))



# 在 Python 中按长度将字符串拆分为字符串
string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

x = 3
res = [string[y - x:y] for y in range(x, len(string) + x, x)]
print(res)



# 如何在 Python 中将字符串的第三个字母大写
s = "xxxyyyzzz"

# convert to list
a = list(s)

# change every third letter in place with a list comprehension
a[2::3] = [x.upper() for x in a[2::3]]

# back to a string
s = ''.join(a)

print(s)



# 将制表符大小设置为指定的空格数
txt = "Canada\tis\ta\tgreat\tcountry"

print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))



# 将两个字符串与某些字符进行比较
str1 = "Can"
str2 = "Canada"
print(str1 in str2)
print(str1.startswith(str2))
print(str2.startswith(str1))

print(str1.endswith(str2))

str3 = "CAN"
print(str3 in str2)



# 字符串格式化填充负数
n = [-2, -8, 1, -10, 40]

num = ["{1:0{0}d}".format(2 if x >= 0 else 3, x) for x in n]
print(num)



# 单独替换字符串中的第一个字符
str1 = "caars caars caars"
str2 = str1.replace('aa', 'a', 1)

print(str2)



# 连接固定字符串和变量
variable = 'Hello'
print('This is the Test File ' + variable)

variable = '10'
print('This is the Test File ' + str(variable))



# 将字符串拆分为多个字符串
s = 'str1, str2, str3, str4'
l = s.split(', ')

print(l)



# 在 Python 中将字符串大写
x = "canada japan australia"

x = x[:1].upper() + x[1:]
print(x)

x= x.capitalize()
print(x)

x= x.title()
print(x)



# 将字节字符串拆分为单独的字节
data = b'\x00\x00\x00\x00\x00\x00'

info = [data[i:i + 2] for i in range(0, len(data), 2)]
print(info)



# 用空格填写 Python 字符串
string = 'Hi'.ljust(10)
print(string)

string = 'Hi'.rjust(10)
print(string)

string = '{0: ^20}'.format('Hi')
print(string)

string = '{message: >16}'.format(message='Hi')
print(string)

string = '{message: <16}'.format(message='Hi')
print(string)

string = '{message: <{width}}'.format(message='Hi', width=20)
print(string)



# 比较两个字符串并检查它们共有多少个字符
from collections import Counter

def shared_chars(s1, s2):
    return sum((Counter(s1) & Counter(s2)).values())

print(shared_chars('car', 'carts'))



# 在 Python 中的数字和字符串之间添加空格
import re

s = "ABC24.00XYZ58.28PQR"
s = re.sub("[A-Za-z]+", lambda group: " " + group[0] + " ", s)
print(s.strip())



# 如何在Python中去除空格
s = '   canada  '
print(s.rstrip())  # For whitespace on the right side use rstrip.
print(s.lstrip())  # For whitespace on the left side lstrip.
print(s.strip())  # For whitespace from both side.

s = ' \t  canada  '
print(s.strip('\t'))
# This will strip any space, \t, \n, or \r characters from the left-hand side, right-hand side, or both sides of the string.



# 字符串中最后一次出现的分隔符处拆分字符串
s = 'canada-japan-australia-uae-india'
l = s.rsplit('-', 1)[1]
print(l)



# 在Python中将字符串的最后一个字母大写
string = "canada"

result = string[:-1] + string[-1].upper()
print(result)

result = string[::-1].title()[::-1]
print(result)



# 使用指定字符居中对齐字符串
txt = "canada"

x = txt.center(20)

print(x)



# 格式字符串中动态计算的零填充
x = 4
w = 5
print('{number:0{width}d}'.format(width=w, number=x))



# 在 Python 中使用 string.replace()
a = "This is the island of istanbul"
print (a.replace("is" , "was", 1))
print (a.replace("is" , "was", 2))
print (a.replace("is" , "was"))



# 在 Python 中获取字符的位置
test = 'Position of a character'
print(test.find('of'))
print(test.find('a'))



# Python字符串替换多次出现
s = "The quick brown fox jumps over the lazy dog"
for r in (("brown", "red"), ("lazy", "quick")):
    s = s.replace(*r)

print(s)



# 在索引后找到第一次出现的字符
string = 'This + is + a + string'
x = string.find('+', 4)
print(x)

x = string.find('+', 10)
print(x)



# 在 Python 中将字符串更改为大写
x = 'canada'
x = x.upper()

print(x)



# 在 Python 中拆分具有多个分隔符的字符串
import re

l = re.split(r'[$-]+', 'canada$-india$-japan$-uae')
print(l)



# 在 Python 中获取字符串的大小
string1 = "Canada"
print(len(string1))

string2 = "  Canada"
print(len(string2))

string3 = "Canada  "
print(len(string3))



# Python中的字符串比较 is vs ==

x = 'canada'
y = ''.join(['ca', 'na', 'da'])
print(x == y)
print(x is y)

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)

z = y
print(z is y)



# 每当数字与非数字相邻时，Python 正则表达式都会添加空格
import re

text = ['123', 'abc', '4x5x6', '7.2volt', '60BTU',
        '20v', '4*5', '24in', 'google.com-1.2', '1.2.3']

pattern = r'(-?[0-9]+\.?[0-9]*)'
for data in text:
    print(repr(data), repr(
        ' '.join(segment for segment in re.split(pattern, data) if segment)))



# 在 Python 中仅按第一个空格拆分字符串
s = 'canada japan australia'
l = s.split(' ', 1)
print(l)



# 在Python中将字符串中的一些小写字母更改为大写
indices = set([0, 7, 14, 18])

s = "i love canada and japan"
print("".join(c.upper() if i in indices else c for i, c in enumerate(s)))



# 将字符串拆分为具有多个单词边界分隔符的单词
import re

thestring = "a,b,c d!e.f\ncanada\tjapan&germany"
listitems = re.findall('\w+', thestring)

for item in listitems:
    print(item)



# 检查一个字符串在 Python 中是否具有相同的字符
str1 = 'caars'
str2 = 'rats'
str3 = 'racs'

print(set(str1)==set(str2))
print(set(str1)==set(str3))



# 在多个分隔符或指定字符上拆分字符串
import re

string_test = "Ethnic (279), Responses (3), 2016 Census - 25% Sample"
print(re.findall(r"[\w']+", string_test))

def split_by_char(s, seps):
    res = [s]
    for sep in seps:
        s, res = res, []
        for seq in s:
            res += seq.split(sep)
    return res

print(split_by_char(string_test, [' ', '(', ')', ',']))



# 将一个字符串附加到另一个字符串
# Example 1
str1 = "Can"
str2 = "ada"
str3 = str1 + str2
print(str3)

# Example 2
str4 = 'Ca'
str4 += 'na'
str4 += 'da'
print(str4)

# Example 3
join_str = "".join((str1, str2))
print(join_str)

# Example 4
str_add = str1.__add__(str2)
print(str_add)



# 在Python中遍历字符串
# Example 1
test_str = "Canada"
for i, c in enumerate(test_str):
    print(i, c)

print("------------------------")

# Example 2
indx = 0
while indx < len(test_str):
    print(indx, test_str[indx])
    indx += 1

print("------------------------")
# Example 3
for char in test_str:
    print(char)



# 从Python中的字符串中去除标点符号
import string
import re

# Example 1
s = "Ethnic (279), Responses (3), 2016 Census - 25% Sample"
out = re.sub(r'[^\w\s]', '', s)
print(out)

# Example 2
s = "Ethnic (279), Responses (3), 2016 Census - 25% Sample"
for p in string.punctuation:
    s = s.replace(p, "")
print(s)

# Example 3
s = "Ethnic (279), Responses (3), 2016 Census - 25% Sample"
out = re.sub('[%s]' % re.escape(string.punctuation), '', s)
print(out)



# 将列表转换为字符串
list_exp = ['Ca', 'na', 'da']
print(type(list_exp))

# Example 1
str_exp1 = ''.join(list_exp)
print(type(str_exp1))
print(str_exp1)

# Example 2
str_exp2 = ''.join(str(e) for e in list_exp)
print(type(str_exp2))
print(str_exp2)

# Example 3
str_exp3 = ''.join(map(str, list_exp))
print(type(str_exp2))
print(str_exp2)



# 将JSON转换为字符串
import json

# list with dict a simple Json format
json_exp = \
    [{"id": "12", "name": "Mark"}, {"id": "13", "name": "Rock", "date": None}]
print(type(json_exp))

str_conv = json.dumps(json_exp)  # string
print(type(str_conv))
print(str_conv)



# 对字符串列表进行排序
# Example 1
str_list = ["Japan", "Canada", "Australia"]
print(str_list)
str_list.sort()
print(str_list)

# Example 2
str_list = ["Japan", "Canada", "Australia"]
for x in sorted(str_list):
    print(x)

# Example 3
str_var = "Canada"
strlist = sorted(str_var)
print(strlist)



# 在Python中检查字符串是否以XXXX开头
import re

exp_str = "Python Programming"

# Example 1
if re.match(r'^Python', exp_str):
    print(True)
else:
    print(False)

# Example 2
result = exp_str.startswith("Python")
print(result)



# 在Python中将两个字符串网格或交错在一起的不同方法
str1 = "AAAA"
str2 = "BBBBBBBBB"

# Example 1
mesh = "".join(i + j for i, j in zip(str1, str2))
print("Example 1:", mesh)

# Example 2
min_len = min(len(str1), len(str2))
mesh = [''] * min_len * 2
mesh[::2] = str1[:min_len]
mesh[1::2] = str2[:min_len]
print("Example 2:", ''.join(mesh))

# Example 3
mesh = ''.join(''.join(item) for item in zip(str1, str2))
print("Example 3:", mesh)

# Example 4
min_len = min(len(str1), len(str2))
mesh = [''] * min_len * 2
mesh[::2] = str1[:min_len]
mesh[1::2] = str2[:min_len]
mesh += str1[min_len:] + str2[min_len:]
print("Example 4:", ''.join(mesh))