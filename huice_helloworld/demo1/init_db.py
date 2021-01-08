#coding:utf-8
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "huice_helloworld.settings")
django.setup()
from demo1.models import *
from xlrd import xldate_as_datetime
import xlrd


book = xlrd.open_workbook(u'./图书信息表.xls')
table = book.sheet_by_name(u'作者信息')

for i in range(1, table.nrows):
    values = table.row_values(i)
    name = values[0]
    sex = values[1]
    age = values[2]
    email = values[3]
    phone = values[4]
    if sex == u'男':
        sex = 0
    else:
        sex = 1
    author = Author.objects.create(name=name)
    AuthorDetails.objects.create(
        sex = sex,
        age = age,
        email = email,
        phone = int(phone),
        author = author
    )

table2 = book.sheet_by_name(u'出版社信息')
for i in range(1, table2.nrows):
    values = table2.row_values(i)
    name = values[0]
    address = values[1]
    city = values[2]
    website = values[3]
    Publisher.objects.create(name=name, address=address,city=city,
                             website=website)

table3 = book.sheet_by_name(u'图书信息')
for i in range(1, table3.nrows):
    values = table3.row_values(i)
    title = values[0]
    author_name = values[1].split(',')
    publication_name = values[2]
    publication_date = xldate_as_datetime(values[3], 0)
    price = values[4]
    try:
        publisher = Publisher.objects.get(name=publication_name)
        book = Book.objects.create(title=title, pulisher=publisher, price=price, publication_date=publication_date)
        for a_name in author_name:
            author = Author.objects.get(name=a_name)
            book.authors.add(author)

    except Exception as e:
        print e

