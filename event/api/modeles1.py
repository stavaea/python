#coding:utf-8
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Event(models.Model):
    title = models.CharField(max_length=30, unique=True)
    limit = models.IntegerField(default=200)
    status_list = ((0, '未开始'), (1, '进行中'), (2, '已结束'))
    status = models.IntegerField(choices=status_list)
    address = models.CharField(max_length=50, null=False)
    time = models.DateTimeField(null=False)

    def __unicode__(self):
        return self.title

    class META():
        verbose_name = '会议表'
        verbose_name_plural = verbose_name

class Guest(models.Model):
    event = models.ManyToManyField
    name = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=11, unique=True, null=False)
    e_mail = models.CharField(max_length=30, null=False)

    def __unicode__(self):
        return self.name

    class META:
        verbose_name = '嘉宾表'
        verbose_name_plural = verbose_name