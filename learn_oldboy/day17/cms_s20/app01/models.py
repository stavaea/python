from django.db import models

# Create your models here.


class Book(models.Model):
    title=models.CharField(max_length=32)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    create_time=models.DateField()

    comment_num=models.IntegerField(default=0)
    poll_num=models.IntegerField(default=0)
    read_num=models.IntegerField(default=0)

    memo=models.CharField(max_length=32,default="")

    # book_obj.publish: 与这本书籍关联的出版社对象
    publish=models.ForeignKey(to="Publish",default=1)
    # book_obj.author.all():  与这本书关联的作者对象集合,Queryset []
    author=models.ManyToManyField("Author")

    def __str__(self):
        return self.title

class Publish(models.Model):
    name=models.CharField(max_length=32)
    email=models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Author(models.Model):
    name=models.CharField(max_length=32)

    def __str__(self):return self.name


class AuthorDetail(models.Model):
    tel=models.CharField(max_length=32)
    email=models.EmailField()
    author=models.OneToOneField("Author")
    def __str__(self):return self.email



# class Author2Book(models.Model):
#     book=models.ForeignKey("Book")
#     author=models.ForeignKey("Author")



















