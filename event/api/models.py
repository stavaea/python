#coding:utf-8
from django.db import models

# Create your models here.

class Event(models.Model):

    title = models.CharField(max_length=50, unique=True)
    limit = models.IntegerField(default=200)
    choice = ((0, '未开始'), (1, '进行中'), (2, '已结束'))
    status = models.IntegerField(choices=choice, default=0)
    address = models.CharField(max_length=50, null=False)
    time = models.DateField(null=False)

class Guest(models.Model):

    name = models.CharField(max_length=10, null=False)
    phone_number = models.CharField(max_length=11, unique=True, null=False)
    e_mail = models.CharField(max_length=30)
    event = models.ManyToManyField(Event)
