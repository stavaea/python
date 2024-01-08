# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2024/1/8 14:48
# @Author : waxberry
# @File : edit_cgi.py
# @Software : PyCharm

print ('Content-type: text/html\n')
from os.path import join, abspath
import cgi,sys

BASE_DIR = abspath('data')
form = cgi.FieldStorage()
filename = form.getvalue('filename')
if not filename:
    print ('Please enter a file name')
    sys .exit()
try:
    text = open(join(BASE_DIR,filename)).read()
except Exception,data:
    print(str(data))
print ('''
<html>
    <head>
        <title>Editing...</title>
    </head>
    <body>
        <form action='/test/cgi-bin/save.cgi' method='POST'>
        <b>File:</b>%s<br/>
        <input type="hidden' value='%s name='filename'/>
        <b>Password:</b><br/>
        <input name='password' type= 'password' /><br/>
        <b>Text :</b><br/>
        <textarea name='text! cols='4'rows='20'>%s</textarea><br/>
        <input type='submit'value='Save">
        </form>
    </body>
</html>
''')% (filename, filename, text)