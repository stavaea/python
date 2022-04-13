# -*- coding: UTF-8 -*-
'''
delimiter //
create procedure p1()
BEGIN
    select user,host from mysql.user;
END //
delimiter ;


delimiter //
create procedure p2(
    in n1 int,
    in n2 int,
    out n3 int
)
BEGIN
    select * from emp where id > n1 and id < n2;
    set n3=1;
END //
delimiter ;
'''
import pymysql

#1、建连接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123',
    db='db5'
)
#2、拿游标
cursor = conn.cursor(pymysql.cursors.DictCursor)

#3、提交sql
# cursor.callproc('p1')
# print(cursor.fetchall())

cursor.callproc('p2', (3, 5, 0)) #@_p2_0=3,@_p2_1=5,@_p2_2=0
print(cursor.fetchall())

cursor.execute('select @_p2_2')
print(cursor.fetchone())

#4、回收资源
cursor.close()
conn.close()
