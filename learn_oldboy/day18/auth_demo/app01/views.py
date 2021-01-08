from django.shortcuts import render,redirect

# Create your views here.

from django.contrib import auth

def login(request):
    if request.method=="POST":
        user=request.POST.get("user")
        pwd=request.POST.get("pwd")
        print("before", request.user)
        user=auth.authenticate(username=user,password=pwd)
        if user:

            auth.login(request,user)  # request.user:当前登录对象
            print("after",request.user)

            return redirect("/index/")
        else:
            return redirect("/login/")


    return render(request,"login.html")



def index(request):
    if not request.user.username:
        return redirect("/login/")

    print(request.user)

    name=request.user.username
    return render(request,"index.html",{"name":name})




def logout(request):

    auth.logout(request)

    return redirect("/login/")


def reg(request):
    from django.contrib.auth.models import User

    User.objects.create_user(username="egon",password="egon1234")

    return redirect("/login/")
