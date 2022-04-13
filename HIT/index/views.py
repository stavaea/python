# coding:utf-8
from django.shortcuts import render
from django.http import JsonResponse,HttpResponseRedirect,HttpResponse
from models import *
import json
from django.contrib import auth
# Create your views here.


def signup(request):
    return render(request, 'signup.html')


def login(request):
    return render(request, 'login.html')


def index(request):
    return render(request, 'home.html')

def task_list(request):
    kw = request.GET.get('kw')
    data = {'data': []}
    if not kw:
        tasks = Task.objects.all()
    else:
        tasks = Task.objects.filter(name__contains=kw)
    for task in tasks:
        data['data'].append(task)
    return render(request, 'task_list.html', data)

def task_search(request):
    kw = request.GET.get('kw')
    if kw:
        tasks = Task.objects.filter(name__contains=kw)
    else:
        tasks = Task.objects.all()
    list = []
    if tasks.exists():
        for task in tasks:
            dic = {}
            dic['id'] = task.id
            dic['name'] = task.name
            list.append(dic)
    return HttpResponse(content_type="application/json", content=json.dumps({'tasks': list}, ensure_ascii=False))

def check_user(request):
    name = request.POST.get('username')
    if name:
        if User.objects.filter(name=name).exists():
            return JsonResponse({'valid': False})
    return JsonResponse({'valid': True})


'''接收用户注册信息，入库。
成功之后跳转登录页，注册失败--提示信息，
'''
def signup_submit(request):
    username = request.POST.get('username')
    email = request.POST.get('email', None)
    password = request.POST.get('password')
    if username and password:
        if not User.objects.filter(name=username).exists():
            try:
                User.objects.create(name=username, email=email, password=password)
                message = u'注册成功'
                flag = 0
                url = '/login/'
            except Exception as e:
                message = u'新增用户失败'
                flag = 1
                url = '/signup/'
                print e
        else:
            message = u'用户名已存在'
            flag = 1
            url = '/signup/'
    else:
        message = u'缺少必填参数'
        flag = 1
        url = '/signup/'

    return render(request, 'alert.html', {'data':json.dumps({'message':message,'flag':flag, 'url':url}, ensure_ascii=False)})

def login_submit(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username and password:
        if User.objects.filter(name=username, password=password).exists():
            try:
                return HttpResponseRedirect('/home/')
            except Exception as e:
                message = u'登录失败'
                flag = 1
                url = '/login/'
                print e
        else:
            message = u'用户名或密码错误'
            flag = 1
            url = '/login/'
    else:
        message = u'缺少必填参数'
        flag = 1
        url = '/login/'

    return render(request, 'alert.html', {'data':json.dumps({'message':message,'flag':flag, 'url':url}, ensure_ascii=False)})

def task_delete(request):
    id = request.GET.get('id')
    if id:
        if Task.objects.filter(id=id).exists():
            try:
                Task.objects.filter(id=id).delete()
                message = u'任务已删除'
                flag = 0
                url = '/task/list/'
            except:
                message = u'删除任务失败'
                flag = 1
                url = '/task/list/'
        else:
            message = u'测试任务不存在'
            flag = 1
            url = '/task/list/'
    else:
        message = u'缺少必填参数'
        flag = 1
        url = '/task/list/'

    return render(request, 'alert.html', {'data':json.dumps({'message':message,'flag':flag, 'url':url}, ensure_ascii=False)})