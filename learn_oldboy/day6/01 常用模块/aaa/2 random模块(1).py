import random

# print(random.random())
# print(random.randint(1,3))
# print(random.randrange(1,3))
# print(random.choice([1,'alex','sb']))
# print(random.sample([1,'alex','sb'],2))
# print(random.uniform(1,4))

# l=[1,3,4,2,5]
# random.shuffle(l)
# print(l)

def make_code(n):
    res=''
    for i in range(n):
        s1=str(random.randint(0,9))
        s2=chr(random.randint(65,90))
        res+=random.choice([s1,s2])
    return res

print(make_code(7))