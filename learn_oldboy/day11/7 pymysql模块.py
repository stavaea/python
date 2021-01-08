#1、基本使用
# '''
# create table user(
#     id int primary key auto_increment,
#     username char(16),
#     password char(20)
# );
# insert into user(username,password) values
# ('egon','123'),
# ('alex','456'),
# ('wxx','456');
# '''
#
# import pymysql
#
# user=input('user>>: ').strip()
# pwd=input('password>>: ').strip()
#
# #1、建连接
# conn=pymysql.connect(
#     host='127.0.0.1',
#     port=3306,
#     user='root',
#     password='123',
#     db='db6'
# )
# #2、拿游标
# cursor=conn.cursor()
#
# #3、提交sql
# # sql='select id from user where username="%s" and password="%s"' %(user,pwd)
# # print(sql)
# sql='select id from user where username=%s and password=%s'
# rows=cursor.execute(sql,(user,pwd))
#
# if rows:
#     print('登录成功')
# else:
#     print('用户名或密码错误')
#
# conn.commit()
# #4、回收资源
# cursor.close()
# conn.close()




#2、增删改
# import pymysql
#
# #1、建连接
# conn=pymysql.connect(
#     host='127.0.0.1',
#     port=3306,
#     user='root',
#     password='123',
#     db='db6'
# )
# #2、拿游标
# cursor=conn.cursor()
#
# #3、提交sql
# sql='insert into user(username,password) values(%s,%s)'
# # rows=cursor.execute(sql,('yxx','123'))
# # print(rows)
#
# rows=cursor.executemany(sql,[('yxx1','123'),('yxx2','123'),('yxx3','123')])
# print(rows)
#
#
# conn.commit()
# #4、回收资源
# cursor.close()
# conn.close()


#3、查
import pymysql

#1、建连接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123',
    db='db6'
)
#2、拿游标
cursor=conn.cursor(pymysql.cursors.DictCursor)

#3、提交sql
sql = 'select * from user'
rows = cursor.execute(sql)
# print(rows)

# print(cursor.fetchall())
# print('===>',cursor.fetchall())

print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchmany(3))

cursor.scroll(0, mode='absolute') # 相对绝对位置移动
print(cursor.fetchone())
# cursor.scroll(3,mode='relative') # 相对当前位置移动


#4、回收资源
cursor.close()
conn.close()
