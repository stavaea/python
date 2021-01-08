from django.shortcuts import render,HttpResponse,redirect

# Create your views here.


def index(request):
    ret=request.COOKIES.get("is_login_yuan")

    if not ret:
        return redirect("/login/")
    username = request.COOKIES.get("username")
    return render(request,"index.html",locals())



def send_ajax(request):

    return HttpResponse("s20-django")
from .models import *
def user_valid(request):
    #name=request.GET.get("name")
    name=request.POST.get("name")
    ret=User.objects.filter(name=name)
    res={"state":True,"msg":""}
    if ret:
        res["state"]=False
        res["msg"]="该用户已存在"

    import json
    return HttpResponse(json.dumps(res))


def login(request):
    if request.method=="POST":
        user=request.POST.get("user")
        pwd=request.POST.get("pwd")
        user=UserInfo.objects.filter(user=user,pwd=pwd).first()
        if user:
            obj=HttpResponse("登录成功")
            obj.set_cookie("is_login_yuan",True)
            obj.set_cookie("username",user.user)
            return obj

    return render(request,'login.html')