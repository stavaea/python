from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=20)

class User(models.Model):
    name = models.CharField(max_length=20, null=False, unique=True)
    password = models.CharField(max_length=32, null=False)
    email = models.EmailField()