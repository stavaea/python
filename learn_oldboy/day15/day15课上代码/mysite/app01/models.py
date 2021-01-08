from django.db import models

# Create your models here.


# 主机管理系统
class Host(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    ip = models.GenericIPAddressField(unique=True)  # 不能重复
    memo = models.CharField(max_length=128, null=True)  # 备注信息，可以为空
    # 通过外键和HostGroup关联
    group = models.ForeignKey("HostGroup")


# 主机组
class HostGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)




