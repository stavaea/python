

from django import forms
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from .models import *

class UserForm(forms.Form):
    user=forms.CharField(min_length=4)
    pwd=forms.CharField()
    repeat_pwd=forms.CharField()
    email=forms.EmailField()


    def clean_user(self):
        val=self.cleaned_data.get("user")
        ret=UserInfo.objects.filter(username=val)
        if not ret:
            return val
        else:
            raise ValidationError("用户已存在！")


    def clean(self):
        pwd=self.cleaned_data.get("pwd")
        r_pwd=self.cleaned_data.get("repeat_pwd")
        if pwd==r_pwd:
            return self.cleaned_data
        else:
            raise ValidationError("两次密码不一致")