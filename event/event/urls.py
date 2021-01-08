"""event URL Configuration

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
    url(r'^register/', 'api.views.register'),
    url(r'^add_event/', 'api.views.add_event'),
    url(r'^get_eventlist/', 'api.views.get_eventlist'),
    url(r'^add_guest/', 'api.views.add_guest'),
    url(r'^get_guestlist/', 'api.views.get_guestlist'),
    url(r'^sign/', 'api.views.sign'),
]
