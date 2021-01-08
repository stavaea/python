from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from django.contrib import auth

import json

def login(reqeust):
    if reqeust.is_ajax():

       res={"user":None,"msg":None}
       user=reqeust.POST.get("user")
       pwd=reqeust.POST.get("pwd")
       valid=reqeust.POST.get("valid")
       print(reqeust.POST)
       random_str=reqeust.session.get("random_str")
       if valid.upper()==random_str.upper():



           user=auth.authenticate(username=user,password=pwd)
           if user:
               res["user"]=user.username  # request.user
               auth.login(reqeust,user)
           else:
               res["msg"]="用户名或者密码错误"
       else:
           res["msg"]="验证码失败"

       return HttpResponse(json.dumps(res))



    return render(reqeust,"login.html")


def valid_img(request):

    # 方式1：
    # with open("egon.jpg","rb") as f:
    #     data=f.read()

    # 方式2：
    import random
    def get_random_color():
        return (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    # from PIL import Image
    # image=Image.new("RGB",(250,36),color=get_random_color())
    # f=open("validcode.png","wb")
    # image.save(f,"png")
    #
    # with open("validcode.png","rb") as f:
    #     data=f.read()

    # 方式3：
    # from PIL import Image
    # from io import BytesIO
    # image=Image.new("RGB",(250,36),color=get_random_color())
    # f=BytesIO()
    # image.save(f,"png")
    # data=f.getvalue()

    # 方式4：
    from PIL import Image

    from PIL import ImageDraw,ImageFont
    from io import BytesIO
    image=Image.new("RGB",(250,36),color=get_random_color())

    draw=ImageDraw.Draw(image)
    font = ImageFont.truetype("blog/static/font/kumo.ttf", size=32)


    random_str=""
    for i in range(5):
        random_num=str(random.randint(0,9))
        random_low_alpha=chr(random.randint(97,122))
        random_up_alpha=chr(random.randint(65,90))
        random_char=random.choice([random_num,random_low_alpha,random_up_alpha])
        draw.text((20+i*40,0),random_char,get_random_color(),font=font)
        random_str+=random_char

    print(random_str)



    request.session["random_str"]=random_str







    # 噪点噪线
    # width=250
    # height=36
    # for i in range(10):
    #     x1=random.randint(0,width)
    #     x2=random.randint(0,width)
    #     y1=random.randint(0,height)
    #     y2=random.randint(0,height)
    #     draw.line((x1,y1,x2,y2),fill=get_random_color())
    #
    # for i in range(100):
    #     draw.point([random.randint(0, width), random.randint(0, height)], fill=get_random_color())
    #     x = random.randint(0, width)
    #     y = random.randint(0, height)
    #     draw.arc((x, y, x + 4, y + 4), 0, 90, fill=get_random_color())
    f=BytesIO()
    image.save(f,"png")
    data=f.getvalue()
    return HttpResponse(data)



from blog.forms import *

def reg(request):
    if request.method=="POST":
        print(request.POST)
        print(request.FILES)
        form=UserForm(request.POST)
        res={"user":None,"msg":None}
        if form.is_valid():
            user=form.cleaned_data.get("user")
            pwd=form.cleaned_data.get("pwd")
            email=form.cleaned_data.get("email")
            avatar=request.FILES.get("avatar_img")
            blog= Blog.objects.create(title=user+"的个人博客",site=user,theme=user)
            UserInfo.objects.create_user(username=user,password=pwd,email=email,avatar=avatar,blog=blog)

            res["user"]=user



        else:
            res["msg"]=form.errors
        return HttpResponse(json.dumps(res))




    return render(request,"reg.html")


def logout(request):
    auth.logout(request)

    return redirect("/index/")




def index(request):

    article_list=Article.objects.all()
    return render(request,"index.html",locals())





def homesite(request,username,**kwargs):
    print("kwargs",kwargs)
    print(username)# 查当前站点的用户名称
    # 查当前站点的用户对象
    user=UserInfo.objects.filter(username=username).first()

    #  查询当前站点对象
    blog=user.blog

    # 查询当前站点的所有文章
    if kwargs:
        condition=kwargs.get("condition")
        params=kwargs.get("params")

        if condition=="cate":
            article_list=Article.objects.filter(user=user).filter(category__title=params)
        elif condition=="tag":
            article_list=Article.objects.filter(user=user).filter(tags__title=params)
        else:
            year,month=params.split("-")
            article_list=Article.objects.filter(user=user).filter(create_time__year=year,create_time__month=month)
    else:
         article_list=Article.objects.filter(user=user)



    return render(request,"homesite.html",locals())



def article_detail(request,username,article_id):

    print(username)  # 查当前站点的用户名称
    # 查当前站点的用户对象
    user = UserInfo.objects.filter(username=username).first()

    #  查询当前站点对象
    blog = user.blog

    article_obj=Article.objects.filter(pk=article_id).first()
    return render(request,"article_detail.html",locals())