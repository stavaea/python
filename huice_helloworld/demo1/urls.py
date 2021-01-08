#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.conf.urls import url,include


urlpatterns = [
    url(r'^home/', 'demo1.views.home'),
    url(r'^bugs/', 'demo1.views.bugs'),
    url(r'^login/', 'demo1.views.login'),
    url(r'^index/', 'demo1.views.index'),
]

# urlpatterns = [
#     url(r'^home/', include('views.home')),
#     url(r'^bugs/', include('views.bugs')),
#     url(r'^login/', include('views.login')),
#     url(r'^index/', include('views.index')),
# ]