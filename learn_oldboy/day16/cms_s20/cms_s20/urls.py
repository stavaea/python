"""cms_s20 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.shortcuts import HttpResponse

from app01.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^timer/$', timer), # timer(request)
    # url(r'^books_achrive/(\d+)/$', book_detail), # book_detail(request,3)
    # #url(r'^books_achrive/(\d+)/(\d+)/$', books_achrive), # books_achrive(request,2012,12)
    # url(r'^books_achrive/(?P<year>\d+)/(?P<month>\d+)/$', books_achrive2), # books_achrive(request,year=2012,month=12)
    url(r'^login/', login,name="xxx"),
    url(r'^app01/', include('app01.urls'),),
    url(r'^template/', temp_func,),
    url(r'^add/', add,),
    url(r'^query/', query,),
    url(r'^books/', books,),
    url(r'^addbook/', addbook,),
    url(r'^del/(\d+)', delbook,),

]


#  url的路径：/books/3与正则匹配 /book/\d+

# import re
#
# re.findall("^books_achrive/(\d+)/$","books_achrive/2012/12/")
