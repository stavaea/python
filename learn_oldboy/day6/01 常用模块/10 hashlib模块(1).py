import hashlib

# m=hashlib.md5()
# m.update('hello'.encode('utf-8'))
# m.update('world'.encode('utf-8'))
# m.update('world'.encode('utf-8'))
# m.update('world'.encode('utf-8'))
# m.update('world'.encode('utf-8'))
# m.update('world'.encode('utf-8'))
# m.update('world'.encode('utf-8'))
# m.update('world'.encode('utf-8'))
# m.update('world'.encode('utf-8'))
# m.update('world'.encode('utf-8'))
# m.update('world'.encode('utf-8'))
# print(m.hexdigest())

# fc5e038d38a57032085441e7fe7010b0


# m=hashlib.md5()
# m.update('hello'.encode('utf-8'))
# m.update('world'.encode('utf-8'))
# print(m.hexdigest())
#
# m1=hashlib.md5()
# m1.update('hellowor'.encode('utf-8'))
# m1.update('l'.encode('utf-8'))
# m1.update('d'.encode('utf-8'))
# print(m1.hexdigest())



# name=input('user:>> ')
# pwd=input('password:>> ')
# m=hashlib.md5()
# m.update(pwd.encode('utf-8'))
# pwd=m.hexdigest()
#
# print(name,pwd)

# cryt_pwd='aee949757a2e698417463d47acac93df'
# pwds=[
#     'alex3714',
#     'alex123',
#     '123alex'
# ]
# def make_dic(pwds):
#     dic={}
#     for pwd in pwds:
#         m=hashlib.md5(pwd.encode('utf-8'))
#         dic[pwd]=m.hexdigest()
#     return dic
#
# dic=make_dic(pwds)
# for pwd in dic:
#     if dic[pwd] == cryt_pwd:
#         print(pwd)


import hashlib

# m=hashlib.sha512()
# m=hashlib.md5('一行白鹭上青天'.encode('utf-8'))
# m.update('alex3714'.encode('utf-8'))
# m.update('两个黄鹂鸣翠柳'.encode('utf-8'))
# print(m.hexdigest())



# import hmac
# m=hmac.new('加盐'.encode('utf-8'))
# m.update('alex3714'.encode('utf-8'))
# print(m.hexdigest())



