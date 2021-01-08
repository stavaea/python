#coding:utf-8

#1
ren = ['刘能', '王老七', '谢广坤', '赵玉田', '杨晓燕', '刘大脑袋', '王长贵', '谢飞机', '赵四', '王大拿']

#1
# 转unicode字符串
result = []
for i in range(len(ren)):
    ren[i] = unicode(ren[i], 'utf-8')


# 取姓氏，去重
dic = {}
xing = dic.fromkeys([x[0] for x in ren]).keys()
ren.reverse()
for x in xing:
    for r in ren:
        if r.startswith(x):
            result.append(r)
            break
print ','.join(result)

#2
data = {
    '小明':{'语文':60, '数学':68, '英语':45},
    '小璐':{'语文':10, '数学':28, '英语':5},
    '小辉':{'语文':44, '数学':86, '英语':73},
    '小亮':{'语文':99, '数学':95, '英语':95},
    '田老师':{'语文':98, '数学':65, '英语':100},
    '刘老师':{'语文':77, '数学':97, '英语':65},
}

def avg(list):
    return sum(list)/len(list)

list = []
yuwen = {}
shuxue = {}
yingyu = {}

for name, score_dic in data.items():
    score_list = score_dic.values()
    yuwen[name] = (score_dic.get('语文', 0))
    shuxue[name] = (score_dic.get('数学', 0))
    yingyu[name] = (score_dic.get('英语', 0))
    score_dic.get('英语', 0)
    if avg(score_list) < 60:
        list.append(name)

print '平均分不足60的同学为：',' '.join(list)
print '语文最高分%d, 数学最高分%d, 英语最高分%d' %(max(yuwen.values()), max(shuxue.values()), max(yingyu.values()))
print '语文平均分%d, 数学平均分%d, 英语平均分%d' %(avg(yuwen.values()), avg(shuxue.values()), avg(yingyu.values()))
print '语文学霸:%s, 数学学霸:%s, 英语学霸:%s' % ((sorted(yuwen.items(), key=lambda x: x[1], reverse=True)[0][0]),
                                             (sorted(shuxue.items(), key=lambda x: x[1], reverse=True)[0][0]),
                                             (sorted(yingyu.items(), key=lambda x: x[1], reverse=True)[0][0])
                                             )

#3
text = '''A small sample of texts from Project Gutenberg appears in the NLTK corpus collection. 
However, you may be interested in analyzing other texts from Project Gutenberg. 
You can browse the catalog of 25,000 free online books at http://www.gutenberg.org/catalog/, 
and obtain a URL to an ASCII text file. Although 90% of the texts in Project Gutenberg are in English, 
it includes material in over 50 other languages, including Catalan, Chinese, Dutch, Finnish, French, German, Italian
'''

list = text.lower().split(' ')
dic = {}
for i in list:
    if i.endswith(',') or i.endswith('.'):
        i = i[:-1]

danci = {}.fromkeys(list, 0).keys()

for i in danci:
    dic[i] = list.count(i)

print sorted(dic.items(), key=lambda x: x[-1], reverse=True)[:5]
