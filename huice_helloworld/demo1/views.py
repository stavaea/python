# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render

from django.contrib import auth
# Create your views here.

# from django.views.decorators.csrf import csrf_protect

import csv, os, json
from demo1.models import *
import pymysql

def index(request):
    username = request.COOKIES.get('username')
    password = request.COOKIES.get('password')
    if username and password:
        return render(request, 'home.html', {'info': u'欢迎登录:%s' % username})
    else:
        return render(request, 'login.html')

# def index(request):
#     Author(name='李清照').save()
#     return HttpResponse('1')

def home(request):
    # return HttpResponse('hello world')
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        if username and pwd:
            return render(request, 'home.html', {'info': u'欢迎登录:%s' % username})
        else:
            return render(request, 'error.html', {'info': u'用户名或密码为空'})
            # return render (request,'home.html',{'info':'success'})
    else:
        return render(request, 'error.html', {'info': u'请求类型无效'})

        # info = 'huice'
        # return render(request, 'home.html', {'info': info})


def bugs(request):
    mouth = request.GET.get('mouth', None)
    if mouth:
        try:
            mouth = int(mouth)
            if mouth in range(1, 10):
                mouth = '2016_0' + str(mouth)
                sum = search_by_mouth(mouth)
                # info = u'%s 月bug总数为 %d' & (mouth, sum)
                dic = {'month': mouth, 'total': sum}
                json.dumps(dic)
                return HttpResponse(content="{'month':'%s','total':%d" % (mouth, sum), content_type='application/json')
            elif mouth in range(10, 13):
                mouth = '2016_' + str(mouth)
                sum = search_by_mouth(mouth)
                # info = u'%s 月bug总数为 %d' & (mouth, sum)
                return HttpResponse(content="{'month':'%s','total':%d" % (mouth, sum), content_type='application/json')
                # return JsonResponse("{'month':'%s','total':%d" % (mouth, sum)")
            else:
                info = u'月份输入无效'
        except:
            info = u'月份输入无效'
            # return render(request, 'home.html', {'info': info})
        else:
            info = u'月份不能为空'

    return HttpResponse(content="{'info':'%s'" % info, content_type='application/json')


    # return render(request, 'home.html', {'info':u'%s 月bug总数是 %s' % (mouth. sum)})


def search_by_mouth(month):
    data = {
        "business_autoFans_J": [{"2016_08": 14}, {"2016_09": 15}, {"2016_10": 9}],
        "autoAX": [{"2016_08": 7}, {"2016_09": 32}, {"2016_10": 0}],
        "autoAX_admin": [{"2016_08": 5}, {"2016_09": 13}, {"2016_10": 2}],
    }
    sum = 0
    for v in data.values():
        for d in v:
            if d.has_key(month):
                sum = sum + d.get(month, 0)
    return sum


def search_user(username, pwd):
    # print(os.path.abspath('.'))
    file_name = './demo1/data.csv'
    flag = False
    try:
        with open(file_name) as f:
            data = csv.reader(f)
            for d in list(data):
                if d[0] == username and d[1] == pwd:
                    flag = True
    except Exception as e:
        print(e.message)
    return flag


# @api_view(['POST', ])
# @requires_rscf_token
def login(request):
    http_response = HttpResponse()
    issave = request.POST.get('isSave')
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if username and password:
            if len(username) > 5:
                # 读取文件
                # search_user(username, password)

                # login_success = search_user(username, password)
                # login_success = auth.authenticate(username=username, password=password)
                try:
                    login_success = User.objects.filter(username=username,password=password)
                except:
                    username = None
                if username:
                # if len(login_success) < 0:
                    if issave:
                        http_response.set_cookie('username', username, max_age=10)
                        http_response.set_signed_cookie('password', password, salt='111')
                    # http_response.set_cookie('password', password)
                    info = u'欢迎登录：%s' % username
                else:
                    info = u'用户名或密码错误'
            else:
                info = u'用户名长度不足5位'
        else:
            # return HttpResponse(content=u'用户名或密码为空', status = 400)
            info = u'用户名或密码为空'
    else:
        info = u'请求类型无效'
    http_response.content = info
    return http_response
    # return render(request, 'home.html', {'info': info})
