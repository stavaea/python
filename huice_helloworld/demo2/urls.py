#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.conf.urls import url

from demo2 import views
urlpatterns = [
    url(r'^home/(?P<id>\d{2})/$', views.home),
]