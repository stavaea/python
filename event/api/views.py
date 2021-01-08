#coding:utf-8
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
# Create your views here.
from django.contrib import auth
from rest_framework.decorators import api_view
import base64
from rest_framework.authtoken.models import Token
import hashlib
from models import *
from django.contrib.auth.models import *
from django.db import connection
'''为DB中已有的用户生成token
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
for user in User.objects.all():
    Token.objects.create(user=user)'''

'''设置每次生成新用户时，自动为用户生成token的signals
from rest_framework.authtoken.models import Token
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
'''

def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# def check_sign(dic_headers, paras_dic):
#     flag = False
#     user_token = dic_headers.get('HTTP_TOKEN', None)
#     username = paras_dic.get('username')
#     User.objects.filter(username=username).first()
#     # user = auth.authenticate(username=username)
#     token = Token.objects.get(user=user).key
#     random = dic_headers.get('HTTP_RANDOM', None)
#     if token == user_token and random:
#         keys = sorted(paras_dic.keys())
#         list = []
#         for key in keys:
#             if key not in ['username', 'sign']:
#                 list.append(key + '=' + paras_dic[key])
#         paras = '&'.join(list)
#         md5_str = token + 'para=' + paras + random
#         md5 = hashlib.md5()
#         md5.update(md5_str)
#         if paras_dic.get('sign') == md5.hexdigest:
#             flag = True
#     return flag
def check_sign(dic_headers, paras_dic):
    flag = False
    token = dic_headers.get('HTTP_TOKEN', None)
    random = dic_headers.get('HTTP_RANDOM', None)
    if token and random:
        keys = sorted(paras_dic.keys())
        list = []
        for key in keys:
            if key not in ['username', 'sign']:
                list.append(key + '=' + paras_dic[key])
        paras = '&'.join(list)
        md5_str = token + 'para=' + paras + random
        md5 = hashlib.md5()
        md5.update(md5_str)
        if paras_dic.get('sign') == md5.hexdigest:
            flag = True
    return flag

@api_view(['POST',])
def register(request):

    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    result = {}

    if username and password:
        password = base64.decodestring(password)[3:]
        user = auth.authenticate(username=username, password=password)
        if user:
            # token = Token.objects.get(user=request.user).key
            token = Token.objects.get(user=user).key
            error_code = 0
            result['token'] = token
        else:
            error_code = 10000
    else:
        error_code = 10001

    result['error_code'] = error_code
    return JsonResponse(result)

@api_view(['POST',])
def add_event(request):

    result = {}
    title = request.POST.get('title')
    username = request.POST.get('username')
    address = request.POST.get('address')
    time = request.POST.get('time')
    sign = request.POST.get('sign')
    limit = request.POST.get('limit', 200)
    status = request.POST.get('status', 0)
    if title and username and address and sign and time:
        # data = {}
        if check_sign(request.META, request.POST):
            if not Event.objects.filter(title=title).exists():
                Event.objects.create(title=title, address=address,
                                     time=time, limit=limit, status=status)
                error_code = 0
                # data['event_id'] = Event.id
                # data['status'] = Event.status
            else:
                error_code = 10002

        else:
            error_code = 10011
    else:
        error_code = 10001

    result['error_code'] = error_code
    # return JsonResponse(result(data))
    return JsonResponse(result)

@api_view(['POST',])
def get_eventlist(request):

    title = request.POST.get('title', None)
    result = {}
    if check_sign(request.META, request.POST):
        # event_list = []
        if title:
            # search_result = {}
            Event.objects.filter(title=title)
            result['title'] = title
            # search_result['id'] = Event.id
            # search_result['title'] = title
            # search_result['status'] = Event.status
            error_code = 0

        else:
            error_code = 10004
        # event_list['search_result'] = search_result
    else:
        error_code = 10011

    # result['event_list'] = event_list
    result['error_code'] = error_code
    return JsonResponse(result)

@api_view(['POST',])
def add_guest(request):

    result = {}
    evnet_id = request.POST.get('id')
    name = request.POST.get('name')
    phone_number = request.POST.get('phone_number')
    e_mail = request.POST.get('e_mail')

    if evnet_id and name and phone_number and e_mail:
        data = {}
        if check_sign(request.META, request.POST):
            if Event.objects.filter(title=Event.title).exists():
                if Guest.objects.filter(name=name).exists():
                    if Event.limit < Event.limit:
                        Guest.objects.create(name=name, phone_number=phone_number, e_mail=e_mail)
                        error_code = 0
                        data['event_id'] = evnet_id
                        data['guest_id'] = Guest.id
                    else:
                        error_code = 10006
                else:
                    error_code = 10005
            else:
                error_code = 10004
        else:
            error_code = 10011

    else:
        error_code = 10001
    result['data'] = data
    result['error_code'] = error_code
    return JsonResponse(result)

def get_guestlist(request):

    event_id = request.POST.get('event_id')
    phone_number = request.POST.get('phone_number')
    result = {}
    if event_id:
        if check_sign(request.META, request.POST):
            # guest_list = []
            if not Guest.objects.filter(phone_number=phone_number).exists():
                # search_result = {}
                if phone_number:
                    Guest.objects.filter(id=Guest.id, name=Guest.name,
                                         phone_number=Guest.phone_number,
                                         e_mail=Guest.e_mail)
                    # search_result['guest_id'] = Guest.id
                    # search_result['guest_name'] = Guest.name
                    # search_result['phone_number'] = Guest.phone_number
                    # search_result['e_mail'] = Guest.e_mail
                    error_code = 0
                else:
                    cursor = connection.cursor()
                    sql = "select * from api_guest"
                    cursor.execute(sql)
                    error_code = 0
                    # search_result = {}

            else:
                error_code = 10007
            # guest_list['search_result'] = search_result
        else:
            error_code = 10011
    else:
        error_code = 10004
    result['error_code'] = error_code
    # result['guest_list'] = guest_list
    return JsonResponse(result)

@api_view(['POST',])
def sign(request):

    event_id = request.POST.get('event_id')
    phone_number = request.POST.get('phone_number')
    result = {}

    if event_id and phone_number:
        if check_sign(request.META, request.POST):
            pass
            if Event.status != 2:
                error_code = 0
            else:
                error_code = 10010
        else:
            error_code = 10011
    else:
        error_code = 10001
    result['error_code'] = error_code
    return JsonResponse(result)