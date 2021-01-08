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

def editbook(request,id):

    if request.method=="POST":
        title=request.POST.get("title")
        price=request.POST.get("price")
        date=request.POST.get("date")
        publish_id=request.POST.get("publish_id")
        author_id_list=request.POST.getlist("author_id_list")

        Book.objects.filter(id=id).update(title=title,price=price,create_time=date,publish_id=publish_id)
        Book.objects.filter(id=id).update(**request.POST)
        book=Book.objects.filter(id=id).first()
        # book.author.clear()
        # book.author.add(*author_id_list)
        book.author.set(author_id_list)

        return redirect("/books/")



    publish_list = Publish.objects.all()
    author_list = Author.objects.all()
    edit_obj=Book.objects.filter(id=id).first()
    return render(request,"editbook.html",locals())

def delbook(request,id):
    Book.objects.filter(id=id).delete()
    return redirect("/books/")

def multi_query(request):
    ######################基于对象的跨表查询#########################
    #--------一对多：

    # 查询id=9的书籍的出版社的名称
    book_obj=Book.objects.filter(id=9).first()
    print(book_obj.publish.name)

    # # 查询苹果出版社出版过的书籍名称
    # publish_obj=Publish.objects.filter(name="苹果出版社").first()
    # print(publish_obj.book_set.all()) # <QuerySet [<Book: java123>, <Book: 历险记>]>
    # for book in publish_obj.book_set.all():
    #     print(book.title)
    # # --------多对多：
    # # 查询java123所有作者的名字
    # obj=Book.objects.filter(title="java123").first()
    # for i in obj.author.all():
    #     print(i.name)
    #
    # # 查询alex出版过的所有书籍名称
    # obj=Author.objects.filter(name="alex").first()
    # print(obj.book_set.all().values("title")) # <QuerySet [{'title': '历险记'}, {'title': 'php'}]>
    #
    # # 一对一
    # # 查询alex的手机号
    # obj=Author.objects.filter(name="alex").first()
    # print(obj.authordetail.tel)
    # # 查询手机号为456的作者的名字
    # ad=AuthorDetail.objects.filter(tel="456").first()
    # print(ad.author.name)
    ######################基于queryset的跨表查询#########################

    #一对多：
    #正向查询
    # 查询价格等于100的书籍的的出版社的名称
    # book_list=Book.objects.filter(price=100)
    # for book in book_list:
    #     print(book.publish.name)

    # ret=Book.objects.filter(price=100).values("title","publish__name")
    # print(ret)# [{},{},{}]
    #
    # '''
    # values:
    #
    # temp=[]
    # for book in Book.objects.filter(price=100):
    #
    #      temp.append({
    #          "title":book.title,
    #          "publish__name":book.publish.name,
    #      })
    #
    # '''
    # #反向查询
    # # 查询苹果出版社出版过的书籍名称
    #
    # ret=Publish.objects.filter(name="苹果出版社").values("book__title")
    # print(ret)
    # '''
    # publish_obj=Publish.objects.filter(name="苹果出版社").first()
    # temp=[]
    # for book in publish_obj.book_set.all()
    #      book.append({
    #         "book__title":book.title
    #      })
    # '''
    # # 多对多：
    # # 正向查询
    # # 查询java123所有作者的名字
    # ret=Book.objects.filter(title="java123").values("author__name").distinct()
    # print(ret)

    # 查询alex出版过的所有书籍名称
    ret=Author.objects.filter(name="alex").values("book__title")
    print(ret)

    # 一对一：
    # 反向查询
    # 查询alex的手机号
    # ret=Author.objects.filter(name="alex").values("authordetail__tel")
    # print(ret)
    # 查询手机号为456的作者的名字
    # ret=AuthorDetail.objects.filter(tel="456").values("author__name")
    # print(ret)

    # 查询手机号以1开头的作者出版过的所有书籍名称以及出版社名称
    # ret=AuthorDetail.objects.filter(tel__startswith="1").values("author__book__title","author__book__publish__name")
    # print(ret)

    #############################聚合与分组##########################################
    # 聚合
    # 统计所有书籍的平均价格
    from django.db.models import Avg,Count,Max,Min
    # ret=Book.objects.all().aggregate(c=Avg("price"))
    # print(ret)

    #查询每一个出版社出版的书籍个数

    # ret=Publish.objects.all().annotate(c=Count("book")).values("name","c")
    # print(ret)


    # 查询每一个作者出版的书籍的平均价格
    ret=Author.objects.all().annotate(price_avg=Avg("book__price")).values("name","price_avg")
    print(ret)

    #查询每一本书籍名称以及作者的个数

    ret=Book.objects.all().annotate(c=Count("author")).values("title","c")
    print(ret)

    # 查询价格大于200的每一本书籍名称以及作者的个数
    ret = Book.objects.filter(price__gt=200).annotate(c=Count("author")).values("title", "c")
    print(ret)

    #####################F与Q#######################################
    # F
    from django.db.models import F,Q
    ret=Book.objects.filter(comment_num__gt=F("poll_num"))
    print(ret)
    ret=Book.objects.filter(comment_num__gt=F("read_num")*10)
    print(ret)
    Book.objects.all().update(price=F("price")+100)

    # Q
    ret=Book.objects.filter(title__startswith="java",price__gt=200)
    print(ret)
    ret = Book.objects.filter(Q(title__startswith="java")|~Q(price__lt=200))
    print(ret)
    ret = Book.objects.filter(Q(title__startswith="java")|Q(price__lt=200),create_time__year=2017,)
    print(ret)

    return HttpResponse("OK")




