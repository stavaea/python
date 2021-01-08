import settings
import hashlib
import time

class MySQL:
    def __init__(self,host,port):
        self.host=host
        self.port=port

    def func(self):
        print('%s 说：你好啊我的天' %self.name)

    @classmethod
    def from_conf(cls):
        return cls(settings.HOST,settings.PORT)

    @staticmethod
    def create_id(n):
        m=hashlib.md5()
        m.update(str(time.clock()+n).encode('utf-8'))
        return m.hexdigest()

# conn=MySQL('127.0.0.1',3306)

#绑定方法：绑定给谁就应该由谁来调用，谁来调用就会把谁当做第一个参数自动传入

conn=MySQL.from_conf()
# print(conn.host,conn.port)


print(MySQL.create_id(1))
print(conn.create_id(2))
