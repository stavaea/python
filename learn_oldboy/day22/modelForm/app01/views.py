from django.shortcuts import render,HttpResponse

# Create your views here.

from django.views import View
from django import forms
from .models import Publish,Author,Book


'''
class BookForm(forms.Form):
    title=forms.CharField()
    price=forms.DecimalField()
    publishDate=forms.DateField()

    #state=forms.ChoiceField(choices=[(1,"已出版"),(2,"未出版")])
    publish=forms.ModelChoiceField(queryset=Publish.objects.all())
    authors=forms.ModelMultipleChoiceField(queryset=Author.objects.all())
    
############################################################################################################    
    
model:    
class Book(models.Model):    
    title = models.CharField( max_length=32)
    publishDate=models.DateField()
    price=models.DecimalField(max_digits=5,decimal_places=2)

    # 与Publish建立一对多的关系,外键字段建立在多的一方
    publish=models.ForeignKey(to="Publish",to_field="nid",on_delete=models.CASCADE)
    # 与Author表建立多对多的关系,ManyToManyField可以建在两个模型中的任意一个，自动创建第三张表
    authors=models.ManyToManyField(to='Author',)

####################################
from django.forms import ModelForm


class BookModelForm(ModelForm):
    class Meta:
        model=Book
        fields="__all__"

####################################



class BookForm(forms.Form):
    title=forms.CharField()
    price=forms.DecimalField()
    publishDate=forms.DateField()

    #state=forms.ChoiceField(choices=[(1,"已出版"),(2,"未出版")])
    publish=forms.ModelChoiceField(queryset=Publish.objects.all())
    authors=forms.ModelMultipleChoiceField(queryset=Author.objects.all())
    
####################################


'''

from django.forms import ModelForm


class BookModelForm(ModelForm):
    class Meta:
        model=Book
        fields="__all__"






class AddBookView(View):

    def get(self,request):
        form=BookModelForm()
        return render(request,"addbook.html",locals())



    def post(self,request):
        form=BookModelForm(request.POST)
        if form.is_valid():
            # print("cleaned_data:",form.cleaned_data)
            # form.cleaned_data.pop("authors")
            # Book.objects.create(**form.cleaned_data)

            form.save()

            return HttpResponse("OK")



        else:
            print(form.cleaned_data)
            print(form.errors)
        return HttpResponse("OK")



class EditBookView(View):

    def get(self,request,id):

        edit_book=Book.objects.get(pk=id)
        form = BookModelForm(instance=edit_book)
        return render(request,"editbook.html",locals())



    def post(self,request,id):
        edit_book = Book.objects.get(pk=id)
        form=BookModelForm(request.POST,instance=edit_book)
        if form.is_valid():
            form.save()
            return HttpResponse("OK")

        else:
            print(form.cleaned_data)
            print(form.errors)
        return HttpResponse("OK")