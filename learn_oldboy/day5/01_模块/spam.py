#spam.py
# print('from the spam.py')

# __all__=['read1','read2']
# _money=1000

money=1000

def read1():
    print('spam模块：',money)

def read2():
    print('spam模块')
    read1()

def change():
    global money
    money=0

if __name__ == '__main__':
    # print(__name__)
    read1()
    read2()
    change()
    print('调试功能')
