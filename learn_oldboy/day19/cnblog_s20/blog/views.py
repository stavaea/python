from django.shortcuts import render,HttpResponse

# Create your views here.


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

           from django.contrib import auth

           user=auth.authenticate(username=user,password=pwd)
           if user:
               res["user"]=user.username
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


from django import forms
class UserForm(forms.Form):
    user=forms.CharField(min_length=4)
    pwd=forms.CharField()
    repeat_pwd=forms.CharField()
    email=forms.EmailField()


def reg(request):
    if request.method=="POST":
        print(request.POST)
        print(request.FILES)
        form=UserForm(request.POST)
        res={"user":None,"msg":None}
        if form.is_valid():
            pass
        else:
            res["msg"]=form.errors

        return HttpResponse(json.dumps(res))




    return render(request,"reg.html")
