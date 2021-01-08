import re

# print(re.findall('\w','egon 123 + _ - *'))
# print(re.findall('\W','egon 123 + _ - *'))
# print(re.findall('\s','ego\tn 12\n3 + _ - *'))
# print(re.findall('\S','ego\tn 12\n3 + _ - *'))
# print(re.findall('\d','ego\tn 12\n3 + _ - *'))
# print(re.findall('\D','ego\tn 12\n3 + _ - *'))
# print(re.findall('\n','ego\tn 12\n3 + _ - *'))
# print(re.findall('\t','ego\tn 12\n3 + _ - *'))
# print(re.findall('e','ego\tn 12\n3 +hello _ - *'))
# print(re.findall('^e','ego\tn 12\n3 +hello _ - *'))
# print(re.findall('o$','ego\tn 12\n3 +hello'))

#重复：.|?|*|+|{m,n}|.*|.*?
#.代表任意一个字符
# print(re.findall('a.b','a1b a b a-b aaaaaab'))
                    #   a.b
# print(re.findall('a.b','a1b a b a\nb a-b aaaaaab',re.DOTALL))
                    #   a.b

#?:代表?号左边的字符出现0次或者1
# print(re.findall('ab?','a ab abb abbbb a1b')) #['a','ab','ab','ab','a']
#                       #                  ab?

#*:代表*号左边的字符出现0次或者无穷次
# print(re.findall('ab*','a ab abb abbbb a1b')) #['a','ab','abb','abbbb','a']
                      #                  ab*

#+:代表+号左边的字符出现1次或者无穷次
# print(re.findall('ab+','a ab abb abbbb a1b')) #['ab','abb','abbbb']
#                       #                  ab+

# {m,n}:代表左边的字符出现m次到n次
# print(re.findall('ab{0,1}','a ab abb abbbb a1b')) #['ab','abb','abbbb']
# print(re.findall('ab?','a ab abb abbbb a1b')) #['ab','abb','abbbb']

# print(re.findall('ab{0,}','a ab abb abbbb a1b')) #['ab','abb','abbbb']
# print(re.findall('ab*','a ab abb abbbb a1b')) #['ab','abb','abbbb']

# print(re.findall('ab{1,}','a ab abb abbbb a1b')) #['ab','abb','abbbb']
# print(re.findall('ab+','a ab abb abbbb a1b')) #['ab','abb','abbbb']

# print(re.findall('ab{2,4}','a ab abb abbbb a1b')) #['abb', 'abbbb']

#.*:贪婪匹配
# print(re.findall('a.*b','xxxy123a123b456b'))
                        #        a.*b
#.*?:非贪婪匹配
# print(re.findall('a.*?b','xxxy123a123b456b'))

#|:或者
# print(re.findall('compan(y|iess)','too many companiess have gone bankrupt, and the next one is my company'))
# print(re.findall('compan(?:y|iess)','too many companiess have gone bankrupt, and the next one is my company'))
                                 #                                                                         compan(y|iess)

# print(re.findall('href="(.*?)"','<a href="http://www.baidu.com">点击我</a>'))

#rawstring：
# print(re.findall(r'a\\c','a\c a1c aBc')) #a\\c->a\c

#[]:取中括号内任意的一个
# print(re.findall('a[a-z]b','axb azb aAb a1b a-b a+b'))
# print(re.findall('a[A-Z]b','axb azb aAb a1b a-b a+b'))
# print(re.findall('a[a-zA-Z]b','axb azb aAb a1b a-b a+b'))
# print(re.findall('a[0-9]b','axb azb aAb a1b a-b a+b'))
# print(re.findall('a[-+*/]b','axb azb aAb a1b a-b a+b'))
# print(re.findall('a[^-+*/]b','axb azb aAb a1b a-b a+b'))


#re模块的其他方法
#re.search :只匹配成功一次就返回
# print(re.search('a[*]b','axb azb aAb a1b a-b a+b'))
# print(re.search('a[0-9]b','axb azb aAb a1b a-b a2b a+b').group())

# re.match:从开头取
# print(re.match('a[0-9]b','axb azb aAb a1b a-b a2b a+b'))
# print(re.match('a[0-9]b','a1b axb azb aAb a1b a-b a2b a+b').group())
# print(re.search('^a[0-9]b','a1b axb azb aAb a1b a-b a2b a+b').group())

# re.split
# print(re.split(':','root:x:0:0::/root:/bin/bash',maxsplit=1))
# 'root:x:0:0::/root:/bin/bash'.split(':')

# re.sub
# print(re.sub('root','admin','root:x:0:0::/root:/bin/bash',1))
#了解
# print(re.sub('^([a-z]+)([^a-z]+)(.*?)([^a-z]+)([a-z]+)$',r'\5\2\3\4\1','root:x:0:0::/root:/bin/bash'))

# re.compile
obj=re.compile('a\d{2}b')
print(obj.findall('a12b a123b a12345b abbb'))
print(obj.search('a12b a123b a12345b abbb').group())