class A(object):
    # def test(self):
    #     print('from A')
    pass

class B(A):
    # def test(self):
    #     print('from B')
    pass

class C(A):
    # def test(self):
    #     print('from C')
    pass
class D(B):
    # def test(self):
    #     print('from D')
    pass

class E(C):
    # def test(self):
    #     print('from E')
    pass
class F(D,E):
    # def test(self):
    #     print('from F')
    pass

f1=F()
print(F.mro())
# f1.test()
