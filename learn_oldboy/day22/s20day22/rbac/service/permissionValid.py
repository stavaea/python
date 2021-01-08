
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,render,redirect

class PermissionValid(MiddlewareMixin):

    def process_request(self,request):
        current_path = request.path  # /userinfo/add/

        # 设置白名单
        white_list=["/login/","/admin/*"]

        for per in white_list:
             import re
             ret=re.search(per,current_path)
             if ret:
                return None

        #认证用户是否登录
        user_id=request.session.get("user_id")

        if not user_id:
            return redirect("/login/")

        # 校验权限
        permission_list = request.session["permission_list"]
        import re
        flag = False
        for permission in permission_list:  # "/userinfo/"
            permission = "^%s$" % permission
            ret = re.search(permission, current_path)
            if ret:
                return None

        return HttpResponse("您没有权限访问！")