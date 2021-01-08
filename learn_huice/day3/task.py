#!/usr/bin/env python
# _*_ coding:utf-8 _*_

'''1.大脚超市赊账人员名单如下：
['刘能', '王老七', '谢广坤', '赵玉田', '杨晓燕', '刘大脑袋', '王长贵', '谢飞机', '赵四', '王大拿']
大脚想移除掉里面的姓氏重复的人（不考虑复姓），但是对于每种姓氏大脚想保留最后出现的那个人。希望你来帮助她
'''
# lst = ['刘能', '王老七', '谢广坤', '赵玉田', '杨晓燕', '刘大脑袋', '王长贵', '谢飞机', '赵四', '王大拿'];
# newLst = [];
# for k in lst:
#     newLst.append(k[0])
# print(newLst)
# n = [] # 去重的列表
# m = {}
# for k, v in zip(range(0, len(newLst)), newLst): # zip组装[(), ()]形式取得索引和值
#     if v not in n:
#         n.append(v)
#     else:
#         m[v] = k # 拿到重复姓名的最后一个人名的索引值
# print(n)
# print(m)
# for i in m:
#     print(lst[m[i]]) # 根据索引拿到真实姓名



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

# totalscore = {}
# num = 0
# for stu,score in data.items():
#     num += 1
#     if num == 1:
#         totalscore = score
#         continue
#     for k,v in zip(totalscore,score):
#         totalscore[k] += score[v]
# print(totalscore)


# cn = []
# math = []
# en = []
# for k, v in data.items():
#     # print(k, v)
#     math.append(v.values()[0])
#     cn.append(v.values()[1])
#     en.append(v.values()[2])
# print('语文最高分：%d, 数学最高分：%d, 英语最高分：%d' % (max(cn), max(math), max(en)))
# print('语文平均分：%.2f， 数学平均分：%.2f， 英语平均分：%.2f' % (sum(cn))/float(len(cn)),
#                                               (sum(math))/float(len(math)),
#                                               (sum(en))/float(len(en))
#                                                 )

# for v in data.values():
#     # print(k, v)
#     for i in v.values():
#         math.append(i)
#         cn.append(i)
#         en.append(i)
# # print('语文最高分：%d, 数学最高分：%d, 英语最高分：%d' % (max(cn), max(math), max(en)))
# print('语文平均分：%.2f， 数学平均分：%.2f， 英语平均分：%.2f' % (sum(cn))/float(len(cn)),
#                                               (sum(math))/float(len(math)),
#                                               (sum(en))/float(len(en))
#                                                 )


# 找出各科的最高分，平均分，找出各科的学霸
# data = {
#     '小明': {
#         '语文': 60, '数学': 68, '英语': 45},
#     '小璐': {
#         '语文': 10, '数学': 28, '英语': 5},
#     '小辉': {
#         '语文': 44, '数学': 68, '英语': 73},
#     '小亮': {
#         '语文': 99, '数学': 95, '英语': 95},
#     '田老师': {
#         '语文': 98, '数学': 65, '英语': 100},
#     '刘老师': {
#         '语文': 77, '数学': 97, '英语': 65}
# }
# l=[]
# for k, v in data.items():
#     v=dict(v)
#     for k1, v1 in v.items():
#         l1=[]
#         l1.append(k)
#         l1.append(k1)
#         l1.append(v1)
#         l.append(l1)
#
# lyw,lyy,lsx=[],[],[]
# for i in l:
#     if i[1]=='语文':
#         lyw1=[]
#         lyw1.append(i[2])
#         lyw1.append(i[0])
#         lyw.append(lyw1)
#     elif i[1]=='英语':
#         lyy1=[]
#         lyy1.append(i[2])
#         lyy1.append(i[0])
#         lyy.append(lyy1)
#     else:
#         lsx1=[]
#         lsx1.append(i[2])
#         lsx1.append(i[0])
#         lsx.append(lsx1)
# ywScore = []
# yyScore = []
# sxScore = []
# for yw in lyw:
#     ywScore.append(int(yw[0]))
#
# for yy in lyy:
#     yyScore.append(int(yy[0]))
#
# for sx in lsx:
#     sxScore.append(int(sx[0]))
#
# print(lyw)
# print(lyy)
# print(lsx)
# maxyw = max(ywScore)
# avgyw = sum(ywScore)/len(ywScore)
# maxyy = max(yyScore)
# avgyy = sum(yyScore)/len(yyScore)
# maxsx = max(sxScore)
# avgsx = sum(sxScore)/len(sxScore)
#
# maxywname,maxyyname,maxsxname=[],[],[]
#
# for i in lyw:
#     if i[0] == maxyw:
#         maxywname.append(i[1])
#
# for i in lyy:
#     if i[0] == maxyy:
#         maxyyname.append(i[1])
#
# for i in lsx:
#     if i[0] == maxsx:
#         maxsxname.append(i[1])
#
# print('语文最高分为{}，最高分得主为{}，平均分为{},'.format(maxyw, maxywname, avgyw))
# print('英语最高分为{}，最高分得主为{}，平均分为{}'.format(maxyy, maxyyname, avgyy))
# print('数学最高分为{}，最高分得主为{}，平均分为{}'.format(maxsx, maxsxname, avgsx))






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

words = s.split(' ')
d = {}
for word in words:
    d.setdefault(word, s.count(word))
print(sorted(d.items(), key=lambda x: x[-1], reverse=True))[:5]
print(d)
