# import subprocess
# import time
#
# subprocess.Popen('tasklist',shell=True)
# print('----->主')
# time.sleep(1)


# import subprocess
import time
#
# obj=subprocess.Popen('tasklist',shell=True,
#                  stdout=subprocess.PIPE,
#                  stderr=subprocess.PIPE,
#                  )
# print(obj)
# print('第1次:',obj.stdout.read())
# print('第2次:',obj.stdout.read())
# print('---->主')

# print(obj.stdout.read().decode('gbk'))



# import subprocess #ls /etc ;pwd;ps aux
# obj=subprocess.Popen('tssssasklist',shell=True,
#                  stdout=subprocess.PIPE,
#                  stderr=subprocess.PIPE,
#                  )

# print(obj.stdout.read())
# print(obj.stderr.read().decode('gbk'))


#了解
import subprocess #tasklist | findstr python
# obj=subprocess.Popen('tasklist | findstr python',shell=True,
#                  stdout=subprocess.PIPE,
#                  stderr=subprocess.PIPE,
#                  )
#
# print(obj.stdout.read())



obj1=subprocess.Popen('tasklist',shell=True,
                 stdout=subprocess.PIPE,
                 stderr=subprocess.PIPE,
                 )

obj2=subprocess.Popen('findstr python',shell=True,
                 stdin=obj1.stdout,
                 stdout=subprocess.PIPE,
                 stderr=subprocess.PIPE,
                 )

print(obj2.stdout.read())