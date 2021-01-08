#json反序列化
import json

# with open('user.json','r',encoding='utf-8') as f:
#     user=json.loads(f.read()) #json.dumps
#     print(user['name'])

# user=json.load(open('user.json','r',encoding='utf-8'))
# print(user['age'])
# print(user['nb'])


# json_str='{"count":1}'
# print(json.loads(json_str)['count'])

# json_str="{'count':1}"
# print(json.loads(json_str))


# print(json.load(open('user.json','r',encoding='utf-8')))


#pickle反序列化
import pickle

# with open('s.pkl','rb') as f:
#     s=pickle.loads(f.read())
#     print(s,type(s))

s=pickle.load(open('s.pkl','rb'))
print(s, type(s))


