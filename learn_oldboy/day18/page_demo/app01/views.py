from django.shortcuts import render,HttpResponse

# Create your views here.

from .models import Book
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    '''
    批量插入数据
     book_list=[]
    for i in range(100):
        book_obj=Book(title="Book_%s"%i,price=i*i)
        book_list.append(book_obj)

    Book.objects.bulk_create(book_list)


    :param request:
    :return:
    '''

    try:
        book_list = Book.objects.all()
        paginator = Paginator(book_list, 2)
        print("count:", paginator.count)  # 数据总数
        print("num_pages", paginator.num_pages)  # 总页数
        print("page_range", paginator.page_range)  # 页码的列表

        c_page = request.GET.get("page", 1)
        page = paginator.page(c_page)
    except EmptyPage:
        page = paginator.page(1)

    # print(page.has_next())
    # print(page.next_page_number())
    # print(page.has_previous())
    # print(page.previous_page_number())
    # print(page.object_list)




    return render(request,"index.html",{"page":page,"paginator":paginator,"c_page":int(c_page)})





