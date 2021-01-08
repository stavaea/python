# nums=[11,22,33,44,55,66,77,88,99,90]
# d={'k1':[],'k2':[]}
#
# for num in nums:
#     if num > 66:
#         d['k1'].append(num)
#     if num < 66:
#         d['k2'].append(num)
#
# print(d)


s='hello alex alex say hello sb sb'
words=s.split()
d={}
for word in words:
    # print(word)
    d.setdefault(word,s.count(word)) #{'hello':2}
print(d)











