class Teacher:
    school='oldboy'
    count=0

    def __init__(self,name,sex,age,level,salary):
        self.name=name
        self.sex=sex
        self.age=age
        self.level=level
        self.salary=salary
        Teacher.count+=1

    def teach(self):
        print('%s is teaching' %self.name)

t1=Teacher('egon','male',18,10,3000)
t2=Teacher('alex','female',38,9,30000)
t3=Teacher('wxx','female',28,10,30000)

print(t1.count)
print(t2.count)
print(t3.count)