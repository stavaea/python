"""s20day23 URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

# from django.shortcuts import  HttpResponse
# def index(request):
#     return HttpResponse("首页")
#
# def test01(request):
#     return HttpResponse("test01")
# def test02(request):
#     return HttpResponse("test02")
# def test03(request):
#     return HttpResponse("test03")
#
# ########################################################
# def add(request):
#     return HttpResponse("add")
# def list_view(request):
#     return HttpResponse("list_view")
# def change(request,id):
#     return HttpResponse("change")
# def delete(request,id):
#     return HttpResponse("delete")
#
# def get_urls2():
#
#     temp=[
#         url("^add/$",add),
#         url("^$",list_view),
#         url("^(\d+)/change/$",change),
#         url("^(\d+)/delete/$",delete),
#     ]
#
#     return temp
#
#
# def get_urls():
#     temp=[]
#
#     for model,model_class_obj in admin.site._registry.items(): # {Book:ModelAdmin(Book),Publish:ModelAdmn(Publish),....}
#
#           app_name=model._meta.app_label
#           model_name=model._meta.model_name
#           temp.append(url(r"%s/%s/"%(app_name,model_name),(get_urls2(),None,None)))
#
#     return  temp
#

from stark.service.sites import site

urlpatterns = [
    url(r'^admin/', admin.site.urls),
   # url(r"^stark",(get_urls(),None,None))

    url(r'^stark/', site.urls),

]
