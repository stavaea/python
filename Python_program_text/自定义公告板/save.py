# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2024/1/8 15:31
# @Author : waxberry
# @File : save.py
# @Software : PyCharm


print('Content-type:text/html\n')
import cgitb;cgitb.enable()
def quote(string):
    if string:
        return string.replace("'","\\'")
    else:
        return string
import MySQLdb
conn = MySQLdb.connect(db='usernet',host='127.0.0.1',user=' root',passwd='root')
curs = conn.cursor()
import cgi,sys
form = cgi.FieldStorage()
sender = quote(form.getvalue("sender" ))
subject = quote(form.getvalue('subject'))
text = quote(form.getvalue("text"))
reply_to = form.getvalue( 'reply to')
if not (sender and subject and text):
    print ('please supply sender, subject,text')
    sys.exit()
if reply_to is not None:
    query = '''INSERI INTO message(reply_to, sender, subject,text)
    VALUES('%d'，'%s', '%s', '%s')''' % (int(reply_to),sender, subject,text)
else:
    query = '''INSERI INTO message(reply_to, sender, subject,text)
        VALUES('%d'，'%s', '%s', '%s')''' % (int(reply_to), sender, subject, text)
curs.execute(query)
conn.commit()
print('''
<html>
    <head>
        <title>Message Save</title>
    </head>
    <body>
        <h1>Message Saved</h1>
        <hr/>
        <a href='main.cgi'>Back to the main page</a>
    </body>
</html>
''')

