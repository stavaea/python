"""HIT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('^home/', 'index.views.index'),
    url('^signup/$', 'index.views.signup'),
    url('^signup/submit', 'index.views.signup_submit'),
    url('^login/$', 'index.views.login'),
    url('^login/submit', 'index.views.login_submit'),
    url('^task/list/', 'index.views.task_list'),
    url('^task/search/', 'index.views.task_search'),
    url('^task/delete/', 'index.views.task_delete'),
    url('^checkuser/', 'index.views.check_user')
]
