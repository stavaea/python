from django.shortcuts import render

# Create your views here.


from django.shortcuts import HttpResponse, render, redirect
from app01 import models

def index(request):
    # 所有和请求相关的数据都封装到了这个request参数中
    # return HttpResponse("This is index page!")
    return redirect("http://www.luffycity.com")

def home(request):
    # 所有和请求相关的数据都封装到了这个request参数中
    # return HttpResponse("This is home page!")
    return render(request, "home.html")


def login(request):
    error_msg = ""
    # 如果是POST请求，表示页面上给我提交数据了
    if request.method == "POST":
        # 我要从提交的数据中 取到email和pwd
        email = request.POST.get("email2")
        pwd = request.POST.get("pwd")
        print(email, pwd)
        if email == "alex@1.com" and pwd == "alexdsb":
            # 登录成功
            return redirect("http://www.luffycity.com")
        else:
            error_msg = "邮箱或密码错误！"


    # 相当于执行了
    # with open("login.html", "rb") as f:
    # ret = f.read()
    # rerturn ret
    return render(request, "login.html", {"error": error_msg})


# 展示书列表的函数
def book_list(request):
    # 找到所有的书
    books = models.Book.objects.all()
    return render(request, "book_list.html", {"book_list": books})


# 添加新书
def add_book(request):
    # 如果请求方法是post，表示前端页面填完了正在提交新书的信息
    if request.method == "POST":
        new_book_name = request.POST.get("book_name")
        # 去数据库里面创建新的一本书
        models.Book.objects.create(title=new_book_name)
        # 跳转回之前展示书籍列表的页面
        return redirect("/book_list/")
    # 返回一个页面让用户填写新书的相关信息
    return render(request, "add_book.html")

# 删除书
def delete_class(request):
    # 取到要删除的书的ID，如何从GET(URL)请求中获取数据
    delete_id = request.GET.get("id")
    # g根据ID值 去数据库中取对应的数据
    models.Book.objects.get(id=delete_id).delete()  # 找到并删除
    return redirect("/book_list/")


# 编辑书
def edit_book(request):
    # 如果是post请求，就表明前端页面编辑完了，把新的书信息发过来
    if request.method == "POST":
        # 取到正在编辑的书的ID
        book_id = request.POST.get("book_id")
        # 取到编辑之后的书的名字
        new_book_title = request.POST.get("book_name")
        # 更新书的title
        book_obj = models.Book.objects.get(id=book_id)
        book_obj.title = new_book_title
        # 保存
        book_obj.save()
        # 跳转回书列表页
        return redirect("/book_list/")

    # 返回页面让用户编辑书
    # 先取到当前编辑的书的ID值
    edit_id = request.GET.get("id")
    # 根据ID值取出具体的书对象
    book = models.Book.objects.get(id=edit_id)
    return render(request, "edit_book.html", {"book": book })
