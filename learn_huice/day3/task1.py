#!/usr/bin/env python
# _*_ coding:utf-8 _*_

'''1.大脚超市赊账人员名单如下：
['刘能', '王老七', '谢广坤', '赵玉田', '杨晓燕', '刘大脑袋', '王长贵', '谢飞机', '赵四', '王大拿']
大脚想移除掉里面的姓氏重复的人（不考虑复姓），但是对于每种姓氏大脚想保留最后出现的那个人。希望你来帮助她
'''



'''2.编写一组数据，记录组内每个人的语文成绩、数学成绩、英语成绩
    data = {
        '小明':{'语文':60, '数学':68, '英语':45},
        '小璐':{'语文':10, '数学':28, '英语':5},
        '小辉':{'语文':44, '数学':86, '英语':73},
        '小亮':{'语文':99, '数学':95, '英语':95},
        '田老师':{'语文':98, '数学':65, '英语':100},
        '刘老师':{'语文':77, '数学':97, '英语':65},
    }
    a.找到平均分不足60分的人，
    b.找出各科的最高分,平均分
    c.找出各科的学霸
 '''


# data = {
#         '小明':{'语文':60, '数学':68, '英语':45,},
#         '小璐':{'语文':10, '数学':28, '英语':5},
#         '小辉':{'语文':44, '数学':86, '英语':73},
#         '小亮':{'语文':99, '数学':95, '英语':95},
#         '田老师':{'语文':98, '数学':65, '英语':100},
#         '刘老师':{'语文':77, '数学':97, '英语':65},
#     }
#a
# for k, v in data.items():
#     if sum(v.values()) / len(v.values()) < 60:
#         print(k)



'''3.统计一篇英文文章每个单词的出现频率，并返回出现频率最高的前5个单词及其出现次数(字典形式)
A small sample of texts from Project Gutenberg appears in the NLTK corpus collection. However, you may 
be interested in analyzing other texts from Project Gutenberg. You can browse the catalog of 25,000 
free online books at http://www.gutenberg.org/catalog/, and obtain a URL to an ASCII text file. 
Although 90% of the texts in Project Gutenberg are in English, it includes material in over 50 other 
languages, including Catalan, Chinese, Dutch, Finnish, French, German, Italian
'''
s = '''A small sample of texts from Project Gutenberg appears in the NLTK corpus collection. However, you may
be interested in analyzing other texts from Project Gutenberg. You can browse the catalog of 25,000
free online books at http://www.gutenberg.org/catalog/, and obtain a URL to an ASCII text file.
Although 90% of the texts in Project Gutenberg are in English, it includes material in over 50 other
languages, including Catalan, Chinese, Dutch, Finnish, French, German, Italian'''

# words = s.split(' ')
# d = {}
# for word in words:
#     d.setdefault(word,s.count(word))
# print(sorted(d.items(),key=lambda x:x[-1],reverse=True))[:5]
# print(d)
