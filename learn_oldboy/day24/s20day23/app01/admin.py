from django.contrib import admin

# Register your models here.
from app01 import models

admin.site.register(models.Book)
print(admin.site._registry)

admin.site.register(models.Publish)
print(admin.site._registry)

admin.site.register(models.Author)
print(admin.site._registry)
