class Foo:
    def f2(self):
        print('====?>')

    def f1(self):
        print('Foo.f1')
        # super().f2()
        Foo.f2(123)
class Bar:
    def f2(self):
        print('Bar f2')

class Sub(Foo,Bar):
    pass

s=Sub()
# print(Sub.mro())
# [<class '__main__.Sub'>,
# <class '__main__.Foo'>,
# <class '__main__.Bar'>,
#  <class 'object'>]

s.f1()


