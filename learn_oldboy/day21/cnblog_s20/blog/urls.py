
from django.conf.urls import url, include
from django.contrib import admin

from blog import views
from django.views.static import serve
from cnblog_s20 import settings


from blog import views
urlpatterns = [
    url(r"digg/",views.digg),
    url(r"comment/",views.comment),
    url(r"comment_tree/(\d+)",views.comment_tree),
    url(r"add_article",views.add_article),
    url(r'^(?P<username>\w+)/$',views.homesite),
    url(r'^(?P<username>\w+)/(?P<condition>tag|cate|achrive)/(?P<params>.*)',views.homesite),
    url(r'^(?P<username>\w+)/articels/(?P<article_id>\d+)',views.article_detail),

]
