from django.shortcuts import render,redirect
from . import models
# Create your views here.


# 主机列表
def host_list(request):
    # 去数据库中取出所有的主机，展示到页面
    host_list = models.Host.objects.all()
    return render(request, "host_list.html", {"host_list": host_list})

# 添加主机
def add_host(requst):
    if requst.method == "POST":
        # 取出提交的数据
        host_name = requst.POST.get("host_name")
        ip = requst.POST.get("ip")
        memo = requst.POST.get("memo")
        group_id = requst.POST.get("group")

        # 创建新的主机记录
        models.Host.objects.create(name=host_name, ip=ip, memo=memo, group_id=group_id)
        # 跳转回主机列表页
        return redirect("/host_list/")

    # 去数据库中把所有的主机组查找出来
    group_list = models.HostGroup.objects.all()
    return render(requst, "add_host.html", {"group_list": group_list})