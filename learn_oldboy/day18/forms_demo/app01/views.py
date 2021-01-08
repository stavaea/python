from django.shortcuts import render,HttpResponse

# Create your views here.

from django import forms
from django.forms import widgets

class UserForm(forms.Form):
    user=forms.CharField(label="用户名",
                         min_length=5,
                         error_messages={"required":"不能为空","min_length":"最小长度不能小于5"},
                         widget=widgets.TextInput(attrs={"class":"form-control"})

                         )
    tel=forms.CharField(label="手机号",max_length=8, widget=widgets.TextInput(attrs={"class":"form-control"}))
    email=forms.EmailField(label="邮箱", widget=widgets.TextInput(attrs={"class":"form-control"}))



def reg(request):

    if request.method=="POST":
        #print(request.POST)
        #form=UserForm({"user":"alex999","tel":'123',"email":"111","123":123})
        form=UserForm(request.POST)
        if form.is_valid():
            print("====>",form.cleaned_data)#
            print("====>",form.errors)#
            return HttpResponse("添加成功")
        else:
            # print("---->", form.cleaned_data)  #
            # print("---->", type(form.errors))  # <class 'django.forms.utils.ErrorDict'>
            # print("---->", type(form.errors["user"]))  #
            # print("---->", form.errors["user"][0])  #

            return render(request, 'reg.html',{"form":form})

    form=UserForm()
    return render(request,'reg.html',{"form":form})


'''
form.is_valid():
    # 校验成功的字段
    form.cleaned_data={"user":"alex999","tel":'123'}

    # 校验失败的字段
    form.errors={"email":["..........","......."]}

'''