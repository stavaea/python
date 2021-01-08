from django.contrib import admin

# Register your models here.

from app02 import models

admin.site.register(models.Food)
print("=======>",admin.site._registry)

'''
{
<class 'django.contrib.auth.models.Group'>: <django.contrib.auth.admin.GroupAdmin object at 0x000000000423F550>, 
<class 'django.contrib.auth.models.User'>: <django.contrib.auth.admin.UserAdmin object at 0x0000000004268F98>,

<class 'app01.models.Book'>: <django.contrib.admin.options.ModelAdmin object at 0x0000000004274048>,
<class 'app01.models.Publish'>: <django.contrib.admin.options.ModelAdmin object at 0x000000000427BA90>,
<class 'app01.models.Author'>: <django.contrib.admin.options.ModelAdmin object at 0x000000000427BBA8>, 
<class 'app02.models.Food'>: <django.contrib.admin.options.ModelAdmin object at 0x000000000427BBE0>}



'''