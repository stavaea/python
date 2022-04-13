def my_max(x, y):
    if x >= y:
        return x
    else:
        return y

x = 10
y = 20

# res=x if x >= y else y
# print(res)

name = input('>>: ').strip()

res = 'Sb' if name == 'alex' else 'NB'
print(res)