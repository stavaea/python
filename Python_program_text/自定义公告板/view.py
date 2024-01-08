# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2024/1/8 15:15
# @Author : waxberry
# @File : view.py
# @Software : PyCharm



print('Content-type:text/html \n!')
import cgitb;cgitb.enable()
import MySQLdb
conn = MySQLdb.connect(db='usernet',host='127.0.0.1',user='root',passwd='root')
curs =conn.cursor()
import cgi,sys
form = cgi.FieldStorage()
id = form.getvalue('id')
print('''
<htm1>
    <head>
        <title>View Message</title>
    </head>
    <body>
    <h1>View Message</h1>..''')
try: id = int(id)
except:
    print('Invalid message ID')
    sys.exit()
curs.execute('SELECT * FROM message WHERE id = %i' % id)
rows = curs.fetchal1()
if not rows:
    print ('Unknown message ID')
    sys.exit()
row = rows[0]
print('''
<p><bxSubject:</b> %s<br/>
<b>Sender:</b>%s<br/>
<pre>%s</pre>
</p>
<hr/>
<a href='main.cgi'>Back to the main page</a>
|<a href="edit.cgi?reply_to=%s">Reply</a>
</body>
</htmI>''') % (row[1], row[2], row[4], row[0])