

上节回顾：

	class Book(models.Model):
		title=models.CharField(max_length=32)
		price=models.DecimalField(max_digits=6,decimal_places=2)
		create_time=models.DateField()
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

	class Author(models.Model):
		name=models.CharField(max_length=32)

		def __str__(self):return self.name
		
		
		

添加记录：
    # 方式1:
    book_obj=Book.objects.create(title="python",price=122,create_time="2012-12-12",publish_id=2)
    print(obj.title)
	
	# 方式2:
	publish_obj=Publish.objects.filter(id=2).first()
	book_obj=Book.objects.create(title="python",price=122,create_time="2012-12-12",publish=publish_obj)
    print(obj.title)
	
	
	
	id  book_id    auhtor_id
	 1     1           1
	 2     1           2
	 3     1           3
	
	book_obj.author.add(1,2,3)
	book_obj.author.add(*[1,2,3])
	book_obj.author.remove(*[1,2])
	book_obj.author.clear()
	
	
查询：
    	

	




		
		







day17





