#coding:utf-8
from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=18)

class Author(models.Model):
    name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '作者表'
        verbose_name_plural = verbose_name
        # ordering = []

class AuthorDetails(models.Model):
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    sex = models.IntegerField(choices=((0, '男'), (1, '女')))
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    author = models.OneToOneField(Author) # author = Author.id


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    website = models.URLField()

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    price = models.FloatField(max_length=20)
    def __unicode__(self):
        return self.title

