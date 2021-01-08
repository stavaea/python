
from django.conf.urls import url,include
from app01.views import *

urlpatterns = [

    url(r'^timer/$', timer), # timer(request)
    url(r'^books_achrive/(\d+)/$', book_detail), # book_detail(request,3)
    #url(r'^books_achrive/(\d+)/(\d+)/$', books_achrive), # books_achrive(request,2012,12)
    url(r'^books_achrive/(?P<year>\d+)/(?P<month>\d+)/$', books_achrive2), # books_achrive(request,year=2012,month=12)

]


