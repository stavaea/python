

# dic={'a':1}

# with open('db.txt','w',encoding='utf-8') as f:
#     f.write(str(dic))

# with open('db.txt','r',encoding='utf-8') as f:
#     dic=eval(f.read()) #"{'a':1}"
#     print(dic['a'])


# eval("[null,false,1]")



import json
# dic={'a':1}
# x=None

# res1=json.dumps(dic) #str(dic)
# res2=str(dic)
# print(res1,type(res1))
# print(res2,type(res2))

# res=json.dumps(x)
# print(res,type(res))


# json序列化
# import json,time
# user={'name':'egon','age':18,'nb':True}
# with open('user.json','w',encoding='utf-8') as f:
#     f.write(json.dumps(user))
#
# students=['alex','egon','wxx','yxx']
# json.dump(students,open('students.json','w',encoding='utf-8'))
#
# time.sleep(500)

# pickle序列化
import pickle,json

s={1,2,3}
# print(json.dumps(s))
# print(pickle.dumps(s))

# with open('s.pkl','wb') as f:
#     f.write(pickle.dumps(s))

pickle.dump(s,open('s.pkl','wb'))







