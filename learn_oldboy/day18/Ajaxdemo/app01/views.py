from django.shortcuts import render,HttpResponse,redirect

# Create your views here.


def index(request):
    if not request.session.get("user_id"):
        return redirect("/login/")



    '''
        
        1 request.COOKIE.get("sessionid"):vwerascxh24asdasdasdsd
        
        2 在django-sesion表查询一条记录:session-key=vwerascxh24asdasdasdsd
    
        3 session-data({"user_id":1,"username":"alex"}).get("user_id")
    

    '''

    name=request.session.get("username")

    return render(request,"index.html",locals())



def send_ajax(request):

    return HttpResponse("s20-django")
from .models import *





def login(request):
    if request.method=="POST":
        user=request.POST.get("user")
        pwd=request.POST.get("pwd")
        user=UserInfo.objects.filter(user=user,pwd=pwd).first()
        if user:
            request.session["user_id"]=user.pk
            request.session["username"]=user.user



            return HttpResponse("登录成功")

    return render(request,'login.html')


'''
                 
               if request.COOKIE.get("sessionid"):
                      更新
                      
               else:                           
               
                       {"user_id":1,"username":"alex"}
        
        
                       第一步: 生成随机字符串: vwerascxh24asdasdasdsd
                       第二步: 在django-sesion表生成一条记录:
                            session-key                    session-data
                       vwerascxh24asdasdasdsd       {"user_id":1,"username":"alex"}
                       第三步:
                             
                             obj.set_cookie("sessionid",vwerascxh24asdasdasdsd) 

 '''


def logout(request):

    request.session.flush()


    return redirect("/login/")