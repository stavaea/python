from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def timer(request):

    import time
    ctime=time.time()
    #return HttpResponse(ctime)
    return render(request,"timer.html",{"ctime":ctime})

def book_detail(reqeust,id):

    return HttpResponse(id)

def books_achrive(request,year,month):

    return HttpResponse(year+":"+month)

def books_achrive2(request,month,year):

    return HttpResponse(year+":"+month)

def login(request):

    if request.method=="GET":
        print(request.GET)
        print(request.POST)
        print(request.method)
        print(request.path)
        print(request.path_info)
        print(request.body)
        return render(request, "login.html")

    else:

        print(request.GET)
        print(request.POST)
        print(request.method)
        print(request.path)
        print(request.path_info)
        print(request.body)

        user=request.POST.get("user")
        pwd=request.POST.get("pwd")
        if 1:
            return redirect("/app01/timer/")


def temp_func(request):

    l=[11,222,333]
    dic={"name":"yuan","age":23}

    class Person(object):
        def __init__(self,name,age):
            self.name=name
            self.age=age
        def learning(self):
             return "learning"
    alex=Person("alex",45)
    egon=Person("egon",36)
    person_list=[alex,egon]

    import datetime
    now=datetime.datetime.now()
    print(now)

    file_size=234212123123

    content="hello yuan world egon alex"
    s="<a href='http://www.baidu.com'>hello</a>"
    #return render(request,"temp.html",{"l":l,"dic":dic})
    return render(request,"temp.html",locals())


from .models import *
def add(request):
    # obj=Book.objects.create(title="python",price=123,create_time="2012-12-12")
    # print(obj.title)

    obj=Book(title="php",price=123,create_time="2012-12-12")
    obj.save()
    return HttpResponse("123")


def query(request):
    # # (1) all()    QuerySet: [<Book: Book object>, <Book: Book object>]
    # book_list=Book.objects.all()
    # print(book_list)
    #
    # # (2) filter()   QuerySet
    # book_list=Book.objects.filter(price=123,title="python")
    # print(book_list)
    # book = Book.objects.filter(price=123, title="python")[0]
    # print(book)  # model对象
    #
    # # (3) get()  model对象  有且只有一个查询结果才有意义
    # book=Book.objects.get(price=12345)
    # print(book)

    #(4)  order_by  QuerySet
    # book_list=Book.objects.all().order_by("-id")
    # book_list=Book.objects.all().order_by("price")
    # print(book_list)
    # # (5) count
    # c = Book.objects.all().order_by("price").count()
    # print(c)
    # # (6)first() model对象
    # book=Book.objects.all().first()
    #
    # # (7)exists()
    # ret=Book.objects.all().exists()
    # if ret:
    #     print("Ok")
    # (8)values:QuerySet

    # ret=Book.objects.all().values("title","price")
    # print(ret) # <QuerySet [{'title': 'python'}, {'title': 'php'}]>
    # ret=Book.objects.all().values_list("title","price")
    # print(ret)# <QuerySet [('python', Decimal('123.00')), ('php', Decimal('122.00'))]>
    # (9)distinct
    # ret=Book.objects.all().values("price").distinct()
    # print(ret)

    #######################模糊查询#############################
    book_list=Book.objects.filter(title__startswith="py")
    book_list=Book.objects.filter(price__gt=120)
    return HttpResponse("OK")

'''
   temp=[] 
   for obj in Book.objects.all():
       temp.append({
           "title":obj.title
           "price":obj.price
       })
'''


def books(reqeust):

    book_list=Book.objects.all()

    # 一对多查询
    # book_obj=Book.objects.filter(id=6).first()
    # print(book_obj.publish.name)
    # print(book_obj.publish.email)

    # 多对多的查询
    # book_obj = Book.objects.filter(id=6).first()
    # print(book_obj.author.all())

    return render(reqeust,"books.html",locals())


def addbook(request):

    if request.method=="POST":

        title=request.POST.get("title")
        price=request.POST.get("price")
        date=request.POST.get("date")
        publish_id=request.POST.get("publish_id")
        author_id_list=request.POST.getlist("author_id_list")
        print("author_id_list",author_id_list)
        # 绑定书籍与出版社的一对多的关系
        obj=Book.objects.create(title=title,price=price,create_time=date,publish_id=publish_id)
        # 绑定书籍与作者的多对多的关系
        # 不可行方案
        # for author_id in author_id_list:
        #     A.objects.create(book_id=obj.pk,author_id=author_id)
        # 可行方案
        # obj.author.add(1,2,3)
        # obj.author.remove(1,2)
        # obj.author.clear()
        obj.author.add(*author_id_list)
        return redirect("/books/")





    else:

        publish_list=Publish.objects.all()
        author_list=Author.objects.all()
        return render(request,"addbook.html",locals())


def delbook(request,id):
    Book.objects.filter(id=id).delete()
    return redirect("/books/")