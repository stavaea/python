from django.shortcuts import render,HttpResponse

# Create your views here.


from rbac.models import UserInfo
from  django.views import View

class LoginView(View):

    def get(self,request):
        return render(request,"login.html")

    def post(self,request):


        user=request.POST.get("user")
        pwd=request.POST.get("pwd")

        user=UserInfo.objects.filter(name=user,pwd=pwd).first()
        if user:

            request.session["user_id"]=user.pk

            # 将当前登录用户的权限列表注册到session中
            permission_list=[]
            # for role in user.roles.all():
            #     for permission in role.permissions.all():
            #         permission_list.append(permission.url)

            permission_list = []
            permissions=user.roles.all().values("permissions__url").distinct()
            for per in permissions:
                permission_list.append(per.get("permissions__url"))

            print("permission_list:  ",permission_list)

            request.session["permission_list"]=permission_list


        return HttpResponse("OK")



class UserView(View):


    def get(self,request):


        user_list=UserInfo.objects.all()
        permission_list=request.session["permission_list"]
        return render(request,"user_list.html",locals())



def adduser(request):


    return HttpResponse('adduser')



def change(request,id):


    return HttpResponse('change....')
