#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response,RequestContext,redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import os
import csv
import json
from django.core.urlresolvers import reverse
from django.contrib import auth

# Create your views here.

# @api_view(['POST'])
# def home(request):
#     if request.method == 'GET':
#         return render(request, 'home.html', {'info': '欢迎访问'})
#     else:
#         return render(request, 'error.html', {'info': '请求类型无效'})

def home(request):
    user = request.GET.get('user', '')
    # user = request.session.get('username', '')
    return render(request, 'home.html', {'info': u'欢迎访问,%s' % user})

def error(request):
    info = request.GET.get('info', '')
    return render(request, 'error.html', {'info':info})

def index(request):
    return render(request, 'login.html')

    #cookie机制
    # user = request.COOKIES.get('user', None)
    # pwd = request.COOKIES.get('pwd', None)
    # if user and pwd:
    #     return render(request, 'home.html', {'info':u'欢迎光临 %s' % user})
    # else:
    #     return render(request, 'login.html')

# bugs1
def bugs(request):
    if request.method == 'GET':
        month = request.GET.get('month', None)
        if month:
            bug_info = search_by_month(month)
            if bug_info == '月份参数无效':
                return render(request, 'error.html', {'info': bug_info})
            else:
                return render(request, 'home.html', {'info': u'%s月，bug总数为：%s' %(month, bug_info)})
        else:
            return render(request, 'error.html', {'info': u'缺少参数month'})
    else:
        return render(request, 'error.html', {'info': u'请求类型无效'})

# bugs2
# def bugs(request):
#     result = {}
#     if request.method == 'GET':
#         month = request.GET.get('month', None)
#         if month:
#             bug_info = search_by_month(month)
#             if bug_info == '月份参数无效':
#                 result['info'] = bug_info
#             else:
#                 result['month'] = month
#                 result['total'] = bug_info
#         else:
#             result['info'] = u'缺少参数month'
#     else:
#         result['info'] = u'请求方法类型无效'
#     return HttpResponse(content=json.dumps(result, ensure_ascii=False), content_type='application/json')
#     # return JsonResponse(data=result, charset='utf-8')

def search_by_month(month):
    data = {
    "business_autoFans_J": [{"2017_08": 14}, {"2017_09": 15}, {"2017_10": 9}],
    "autoAX": [{"2017_08": 7}, {"2017_09": 32}, {"2017_10": 0}],
    "autoAX_admin": [{"2017_08": 5}, {"2017_09": 13}, {"2017_10": 2}],
    }
    try:
        month = int(month)
        total = 0
        if month in range(1, 10):
            for l in data.values():
                for d in l:
                    if d.has_key('2017_0%d' % month):
                        total += d.get('2017_0%d' % month, 0)
        elif month in range(10, 13):
            for l in data.values():
                for d in l:
                    if d.has_key('2017_%d' % month):
                        total += d.get('2017_%d' % month, 0)
        else:
            total = '月份参数无效'
    except:
        total = '月份参数无效'
    return total

#login1
# def login(request):
#     if request.method =='POST':
#         username = request.POST.get('username', None)
#         password = request.POST.get('password', None)
#         if username and password:
#             if len(username) >= 5:
#                 if search_user(username, password):
#                     response = u'欢迎光临 %s' % username
#                 else:
#                     response = u'用户名或密码错误'
#             else:
#                 response = u'username必须大于5位'
#         else:
#             response = u'缺少必要参数：username、password'
#     else:
#         response = u'该接口只支持POST请求'
#
#     return render(request, 'home.html', {'info': response})

#login2
# def login(request):
#     response = ''
#     if request.method =='POST':
#         username = request.POST.get('username', None)
#         password = request.POST.get('password', None)
#         if username and password:
#             if len(username) >= 5:
#                 if search_user(username, password):
#                     response = u'欢迎光临 %s' % username
#                 else:
#                     response = u'用户名或密码错误'
#             else:
#                 response = u'username必须大于5位'
#         else:
#             response = u'缺少必要参数：username、password'
#             return HttpResponse(content=response, status=400)
#     else:
#         response = u'该接口只支持POST请求'
#     return render(request, 'home.html', {'info': response})

# login3
# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username', None)
#         password = request.POST.get('password', None)
#         if username and password:
#             if len(username) >= 5:
#                 if search_user(username, password):
#                     response = u'欢迎光临 %s' % username
#                     http_response = render(request, 'home.html', {'info': response})
#                     if request.POST.get('isSave', '0') == '1':
#                         http_response.set_cookie('user', username, max_age=30)
#                         http_response.set_signed_cookie('pwd', password, salt="jkkll", max_age=30)
#                     return http_response
#                 else:
#                     response = u'用户名或密码错误'
#             else:
#                 response = u'username必须大于5位'
#         else:
#             response = u'缺少必要参数：username、password'
#     else:
#         response = u'该接口只支持POST请求'
#     return render(request, 'home.html', {'info': response})

# login4
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if username and password:
            if len(username) >= 5:
                if search_user(username, password):
                    http_response = HttpResponseRedirect('/demo/home/?user=%s' %username)

                    #利用session重定向，传递数据
                    # request.session['username'] = username
                    # request.session.set_expiry(0)
                    # http_response = HttpResponseRedirect('/demo/home/')

                    if request.POST.get('isSave', '0') == '1':
                        http_response.set_cookie('user', username, max_age=30)
                        http_response.set_signed_cookie('pwd', password, salt="jkkll", max_age=30)
                    return http_response
                else:
                    response = u'用户名或密码错误'
            else:
                response = u'username必须大于5位'
        else:
            response = u'缺少必要参数：username、password'
    else:
        response = u'该接口只支持POST请求'
    return HttpResponseRedirect('/demo/error/?info=%s' % response)

#login5
# def login(request):
#     if request.method =='POST':
#         username = request.POST.get('username', None)
#         password = request.POST.get('password', None)
#         if username and password:
#             if len(username) >= 5:
#                 user = auth.authenticate(username=username, password=password)
#                 if user:
#                     auth.login(request, user)
#                     response = u'欢迎光临 %s' % username
#                 else:
#                     response = u'用户名或密码错误'
#             else:
#                 response = u'username必须大于5位'
#         else:
#             response = u'缺少必要参数：username、password'
#     else:
#         response = u'该接口只支持POST请求'
#
#     return render(request, 'home.html', {'info': response})

def search_user(username, password):
    try:
        with open(os.path.abspath('.'+'\\login.csv')) as f:
            reader = csv.reader(f)
            for line in reader:
                u = line[0]
                p = line[1]
                if u == username and p == password:
                    return True
    except:
        return False
    return False