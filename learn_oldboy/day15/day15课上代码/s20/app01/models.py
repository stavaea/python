from django.db import models

# Create your models here.

class Book(models.Model):
    # 定义一个自增的ID主键
    id = models.AutoField(primary_key=True)
    # 定义一个最大长度为32的varchar字段
    title = models.CharField(max_length=32)

