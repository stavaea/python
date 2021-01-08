from django.test import TestCase

# Create your tests here.




from bs4 import BeautifulSoup


s="<h1>yuan</h1><a href='xxxx'>click</a>"

bs=BeautifulSoup(s,"html.parser")

print(bs.text)

print(bs.a.get("href"))