from django.shortcuts import render, HttpResponse


# Create your views here.


# 视图函数
# def login(request):
#
#
#     if request.method=="POST":
#         user=request.POST.get("user")
#
#         return HttpResponse("OK")
#
#
#     return render(request,"login.html")


#视图类

from django.views import View
class LoginView(View):

    def dispatch(self, request, *args, **kwargs):
        print("OK123")

        ret=super().dispatch(request, *args, **kwargs)
        return ret

    def get(self,request):

        return render(request, "login.html")

    def post(self,request):

        user=request.POST.get("user")
        return HttpResponse(user)










