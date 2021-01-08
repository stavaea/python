#coding:utf-8
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from api.models import *
from rest_framework.authtoken.models import Token
import hashlib
import base64
from django.contrib.auth.models import User
from django.contrib import auth
import json
import time
from django.db import connection

def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

def check_sign(header_dic, query_dic):
    flag = False
    sign = query_dic.get('sign', None)
    username = query_dic.get('username', None)
    token = header_dic.get('HTTP_TPKEN', None)
    random = header_dic.get('HTTP_RANDOM', None)
    md5 = hashlib.md5
    user = User.objects.filter(username=username)
    if user.exists():
        if token and len(random) == 5:
            para_str = ''
            if query_dic:
                list = []
                for k, v in query_dic.items():
                    if k !='sign' and k !='username':
                        list.append(k + '=' + v)
                list.sort()
                para_str = '&'.join(list)
            sign_str = "%spara=%s%s" % (token, para_str, random)
            md5.update(sign_str.encode(encoding="utf-8"))
            server_sign = md5.hexdigest()
            if server_sign == sign:
                flag = True
    return flag

@api_view(['POST',])
def register(request):
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    if username and password:
        password = base64.decodestring(password)[3:]
        user = auth.authenticate(username=username, password=password)
        if user:
            token_str = Token.objects.get(user=user).key
            result = {'error_code': 0, 'token': token_str}
        else:
            result = {'error_code': 10000}
    else:
        result = {'error_code': 10001}
    return JsonResponse(result)

@api_view(['POST',])
def add_event(request):
    username = request.POST.get('username', None)
    title = request.POST.get('title', None)
    address = request.POST.get('address', None)
    time = request.POST.get('time', None)
    limit = request.POST.get('limit',None)
    status = request.POST.get('status', 0)
    result = {}
    if title and address and time and username:
        if check_sign(result.META, request.POST):
            event = Event.objects.filter(title=title)
            if not event:
                if status in ('0', '1', '2'):
                    Event.objects.create(title=title, address=address,
                                         time=time, limit=limit, status=status)
                    id = Event.objects.get(title=title).id
                    result = {'error_code': 0,
                              "data":
                                  {"event_id": id,
                                   "status": status}
                              }
                else:
                    result = {'error_code': 10003}
            else:
                result = {'error_code': 10002}
        else:
            result = {'error_code': 10011}
    else:
        result = {'error_code': 10001}
    return JsonResponse(result)

@api_view(['GET',])
def get_eventlist(request):
    title = request.GET.get('title', None)
    username = request.GET.get('username', None)
    result = {}
    if username:
        if check_sign(request.META, request.GET):
            if not title:
                events = Event.objects.all()
            else:
                events = Event.objects.filter(title__contains=title)
            if events.count() > 0:
                event_list = []
                for event in events:
                    id = event.id
                    title = event.title
                    status = event.status
                    event_list.append({'id': id, 'title': title, 'status': status})
                result = {'error_code': 0, 'event_list': event_list}
            else:
                result = {'error_code': 10004}
        else:
            result = {'error_code': 10011}
    else:
        result = {'error_code': 10001}
    return HttpResponse(json.dumps(result, ensure_ascii=False))

@api_view(['POST',])
def get_eventdetail(request):
    id = request.GET.get('id', None)
    username = request.GET.get('username', None)
    if id and username:
        if check_sign(request.META, request.GET):
            try:
                event = Event.objects.get(id=id)
                detail = {}
                detail['id'] = event.id
                detail['title'] = event.title
                detail['status'] = event.status
                detail['limit'] = event.limit
                detail['address'] = event.address
                detail['start_time'] = event.time.strftime('%Y-%m-%d %H:%M:%S')
                result = {'error_code': 0, 'event_detail': detail}
            except:
                result = {'error_code': 10004}
        else:
            result = {'error_code': 10011}
    else:
        result = {'error_code': 10001}
    return HttpResponse(json.dumps(result, ensure_ascii=False))

@api_view(['POST',])
def set_status(request):
    id = request.POST.get('id', None)
    status = request.POST.get('status', None)
    username = request.POST.get('username', None)
    if id and status and username:
        if check_sign(request.META, request.POST):
            try:
                event = Event.objects.get(id=id)
                if status in ('0', '1', '2'):
                    event.status = status
                    event.save()
                    result = {'error_code': 0}
                else:
                    result = {'error_code': 10003}
            except:
                result = {'error_code': 10004}
        else:
            result = {'error_code': 10011}
    else:
        result = {'error_code': 10001}
    return JsonResponse(result)

@api_view(['POST',])
def add_guest(request):
    id = request.POST.get('id', None)
    name = request.POST.get('name', None)
    phone_number = request.POST.get('phone_number', None)
    e_mail = request.POST.get('e-mail', None)
    username = request.POST.get('username', None)
    if id and name and phone_number and username:
        if check_sign(request.META, request.POST):
            event = Event.objects.filter(id=id)
            if event.exists():
                count = Guest.objects.filter(event=event.first()).count()
                guest = Guest.objects.first(phone_number=phone_number)
                if not guest.exists():
                    if count < event.first().limit:
                        g = Guest(name=name, phone_number=phone_number,
                                  e_mail=e_mail)
                        g.save()
                        g.event.add(event.first())
                        result = {'error_code': 0,
                                  "data":
                                      {
                                      "event_id": id,
                                      "guest_id": g.id
                                      }
                                  }
                    else:
                        result = {'error_code': 10006}
                else:
                    events_id = guest.first().event.all().values_list('id')
                    if (int(id),) not in events_id:
                        if count < event.first().limit:
                            Guest.objects.get(phone_number=phone_number).event.add(event.first())
                            result = {'error_code': 0,
                                      "data":
                                          {
                                          "event_id": id,
                                          "guest_id": guest.first().id
                                          }
                                      }
                        else:
                            result = {'error_code': 10006}
                    else:
                        result = {'error_code': 10005}
            else:
                result = {'error_code': 10004}
        else:
            result = {'error_code': 10011}
    else:
        result = {'error_code': 10001}
    return JsonResponse(result)

@api_view(['GET',])
def get_guestlist(request):
    event_id = request.GET.get('event_id', None)
    phone_number = request.GET.get('phone_number', None)
    username = request.GET.get('username', None)
    if event_id and username:
        if check_sign(request.META, request.GET):
            event = Event.objects.filter(id=event_id)
            if event.exists():
                if phone_number:
                    guests = Guest.objects.filter(event=event.first(), phone_number=phone_number)
                else:
                    guests = Guest.objects.filter(event=event.first())
                if guests.exists():
                    guest_list = []
                    for guest in guests:
                        guest_info = {}
                        guest_info['guest_id'] = guest.id
                        guest_info['name'] = guest.name
                        guest_info['phone_number'] = guest.phone_number
                        guest_info['e-mail'] = guest.e_mail
                        guest_list.append(guest_info)
                    result = {'error_code': 0, 'guest_list': guest_list}
                else:
                    result = {'error_code': 10007}
            else:
                result = {'error_code': 10004}
        else:
            result = {'error_code': 10011}
    else:
        result = {'error_code': 10001}
    return HttpResponse(json.dumps(result, ensure_ascii=False))

@api_view(['POST',])
def sign(request):
    event_id = request.POST.get('id', None)
    phone_number = request.POST.get('phone_number', None)
    username = request.POST.get('username', None)
    if event_id and phone_number and username:
        if check_sign(request.META, request.POST):
            event = Event.objects.filter(id=event_id)
            if event.exists():
                n_time = time.time()
                e_time = time.mktime(event.first().time.timetuple())
                if event.first().status != '2' and n_time < e_time:
                    guest = Guest.objects.filter(phone_number=phone_number, event=event.first())
                    if guest.exists():
                        sql = "SELECT sign FROM api_guest_event WHERE guest_id=%s AND event_id=%s" % (guest.first().id, event_id)
                        cursor = connection.cursor()
                        cursor.execute(sql)
                        is_sign = cursor.fetchone()[0]
                        if is_sign == 0:
                            sql = "UPDATE api_guest_event SET sign=1 WHERE guest_id=%s AND event_id=%s" % (guest.first().id, event_id)
                            cursor.execute(sql)
                            result = {'error_code': 0}
                        else:
                            result = {'error_code': 10009}
                    else:
                        result = {'error_code': 10008}
                else:
                    result = {'error_code': 10010}
            else:
                result = {'error_code': 10004}
        else:
            result = {'error_code': 10011}
    else:
        result = {'error_code': 10001}
    return JsonResponse(result)