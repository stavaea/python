# coding:utf-8
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from models import *
from django.db import connection
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
import hashlib,time,base64
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# def check_sign(header_dic, query_dic):
#     flag = False
#     sign = query_dic.get('sign', None)
#     username = query_dic.get('username', None)
#     token = header_dic.get('HTTP_TPKEN', None)
#     random = header_dic.get('HTTP_RANDOM', None)
#     md5 = hashlib.md5
#     user = User.objects.filter(username=username)
#     if user.exists():
#         if token and len(random) == 5:
#             para_str = ''
#             if query_dic:
#                 list = []
#                 for k, v in query_dic.items():
#                     if k !='sign' and k !='username':
#                         list.append(k + '=' + v)
#                 list.sort()
#                 para_str = '&'.join(list)
#             sign_str = "%spara=%s%s" % (token, para_str, random)
#             md5.update(sign_str.encode(encoding="utf-8"))
#             server_sign = md5.hexdigest()
#             if server_sign == sign:
#                 flag = True
#     # return flag

# @api_view(['POST',])
def signup(request):
    username = request.POST.get('username')
    pwd = request.POST.get('password')
    email = request.POST.get('email', None)
    if username and pwd:
        name = User.objects.filter(name=username)
        if not name.exists():
        # if check_user():
            if username > 6 and username < 20:
                if len(pwd) != 0:
                    if email:
                        user = User(name=username, password=pwd, email=email)
                        user.save()
                    else:
                        user = User(name=username, password=pwd)
                        user.save()
                else:
                    msg = u'密码不能为空'
            else:
                msg = u'用户名长度应大于6位小于20位'
        else:
            msg = u'用户已存在'
    else:
        msg = u'缺少必填参数'
    return render(request, 'signup.html', msg)

# @api_view(['POST',])
def login(request):
    username = request.POST.get('username')
    pwd = request.POST.get('password')
    if username and pwd:
        # pwd = base64.decodestring(pwd)[3:]
        # pwd = base64.decodestring(pwd)[3:]
        user = auth.authenticate(username=username, pwd=pwd)
        if user:
            token_str = Token.objects.get(user=user).key
            return token_str
        else:
            msg = u'用户名不存在'
    else:
        msg = u'用户名或密码为空'
    return render(request, 'login.html', msg)

def home(request):
    return render(request, 'home.html')

def task_list(request):
    kw = request.GET.get('kw')
    data = {'data': []}
    if kw:
        tasks = Task.objects.filter(name__contains=kw)
    else:
        tasks = Task.objects.all()
    for task in tasks:
        data['data'].append(task)
    return render(request, 'task_list.html', data)

def check_user(request):
    name = request.POST.get('username')
    if name:
        if User.objects.filter(name=name).exists():
            return JsonResponse({'valid': False})
    return JsonResponse({'valid': True})