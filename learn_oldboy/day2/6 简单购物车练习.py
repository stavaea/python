msg_dic={
'apple':10,
'tesla':100000,
'mac':3000,
'lenovo':30000,
'chicken':10,
}
goods=[]
while True:
    for k in msg_dic:
        print(k,msg_dic[k])
    choice=input('商品名: ').strip()
    if len(choice) == 0 or choice not in msg_dic:
        print('商品名非法')
        continue
    while True:
        num=input('购买个数: ').strip()
        if num.isdigit():
            break
    goods.append((choice,msg_dic[choice],int(num)))
    print('购物车',goods)
