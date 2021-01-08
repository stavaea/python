class Foo:
    def __init__(self,name):
        self.name=name

    def f1(self):
        print('===>f1')

obj=Foo('egon')
# obj.name #obj.__dict__['name']


# hasattr
# print(hasattr(obj,'name')) #obj.name
# print(hasattr(obj,'f1'))#obj.f1

# getattr
# if hasattr(obj,'f1'):
#     f=getattr(obj,'f1') #f=obj.f1
#     f()
# print(getattr(obj,'xxx',None))

# setattr
# obj.x=1
# setattr(obj,'x',1)
# print(obj.__dict__)

# delattr
# del obj.name
# delattr(obj,'name')
# print(obj.__dict__)

class FtpClient:
    def __init__(self,host,port):
        self.host=host
        self.port=port
        self.conn='xxx'

    def interactie(self):
        while True:
            cmd=input('>>: ').strip()
            if not cmd:continue
            cmd_l=cmd.split()
            print(cmd_l)
            if hasattr(self,cmd_l[0]):
                func=getattr(self,cmd_l[0])
                func(cmd_l)

    def get(self,cmd_l):
        print('geting...',cmd_l)

    def put(self,cmd_l):
        print('putting....',cmd_l)

client=FtpClient('1.1.1.1',23)
client.interactie()


