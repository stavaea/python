from django.test import TestCase

# Create your tests here.



class A(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return self.name+str(self.age)
alex=A("alex",23)
print(alex)