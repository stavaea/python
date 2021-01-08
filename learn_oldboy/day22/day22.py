
1 CBV
  看源码
  
  url("login",views.LoginView.as_view()) 
  

  views.LoginView.as_view()=view
  一旦用户访问login：  view(request)===dispatch(request)====self.get(request)

  
2 ModleForm:
   
    forms组件：
	        class BookForm(forms.Form):
				title=forms.CharField()
				price=forms.DecimalField()
				publishDate=forms.DateField()

				#state=forms.ChoiceField(choices=[(1,"已出版"),(2,"未出版")])
				publish=forms.ModelChoiceField(queryset=Publish.objects.all())
				authors=forms.ModelMultipleChoiceField(queryset=Author.objects.all())
    
	
	modelForm：
	
	        model:    
			class Book(models.Model):    
				title = models.CharField( max_length=32)
				publishDate=models.DateField()
				price=models.DecimalField(max_digits=5,decimal_places=2)

				# 与Publish建立一对多的关系,外键字段建立在多的一方
				publish=models.ForeignKey(to="Publish",to_field="nid",on_delete=models.CASCADE)
				# 与Author表建立多对多的关系,ManyToManyField可以建在两个模型中的任意一个，自动创建第三张表
				authors=models.ManyToManyField(to='Author',)

			####################################
			from django.forms import ModelForm


			class BookModelForm(ModelForm):
				class Meta:
					model=Book
					fields="__all__"

			####################################



			class BookForm(forms.Form):
				title=forms.CharField()
				price=forms.DecimalField()
				publishDate=forms.DateField()

				#state=forms.ChoiceField(choices=[(1,"已出版"),(2,"未出版")])
				publish=forms.ModelChoiceField(queryset=Publish.objects.all())
				authors=forms.ModelMultipleChoiceField(queryset=Author.objects.all())
				
		####################################
		
		
		
		addBook:
		     def addbook():
			     if get请求：
				    form=BookModelForm()
					return render(request,"addbook.html",locals()) # 标签渲染 {{form.as_p}}
		
		        if post请求：
				
				   form=BookModelForm(request.POST) 
				   if form.is_valid():
				       form.save() # create操作
					   
		editBook：
		    def editbook():
			    if get请求：
				    editbook=Book.objects.get(pk=id)
				    form=BookModelForm(instance=editbook)
					return render(request,"addbook.html",locals()) # 标签渲染 {{form.as_p}}
		
		        if post请求：
				   editbook=Book.objects.get(pk=id)
				   form=BookModelForm(request.POST,instance=editbook) 
				   if form.is_valid():
				       form.save() # update操作
               		
		
		
		
CRM：


1 权限
  
  什么是权限？  一个包含正则表达式的url就是权限
  who         what     how 
  wenzhou    订单表    查看
  
  
  
 
  
  版本一：
  
        UserInfo
		
		id   name  age  
		1    alex1  33
		2    alex2  33
		3    alex3  33
		4    alex4  33
		5    alex5  33
		6    alex6  33
		7    alex7  33
		8    alex8  33
		9    alex9  33
		10   alex10  33
		
		
		
		permission
		
		id   title         url 
		 1  查看订单     /orders/
		 2  添加订单     /orders/add/
		 3  查看客户     /customers/
		 4  添加客户     /customers/add
		
		UserInfo-permission
		
		id    userinfo_id  permission_id
		1         1             1
		2         1             2
		3         1             3
		4         1             4
		
	
		
		
		
    版本二：
	
	    模型：rbac（role-based access control）      
  
  
        UserInfo
		
		id   name  age  
		1    alex1  33
		2    alex2  33
		3    alex3  33
		4    alex4  33
		5    alex5  33
		6    alex6  33
		7    alex7  33
		8    alex8  33
		9    alex9  33
		10   alex10  33
      
	  
	  
	 
       role
	   
	   id   name
	   1   管理员
	   2   CEO
	   3   销售
	   4   讲师
	   
	   
	   UserInfo-role
	   
	   id  userinfo_id   role_id
	   1      1            3   
	   1      2            3   
	   1      3            3   
	   1      4            3   
	   1      5            3   
	   
	   
	   
	   
	   
	   
	   
	   
       permission
		
		id   title         url           
		 1  查看订单     /orders/
		 2  添加订单     /orders/add/
		 3  查看客户     /customers/
		 4  添加客户     /customers/add
		 5  编辑客户     /customers/(\d+)/change


       permission-Role
	   
	      id     role_id    permission_id 
		   1         3            1           
		   2         3            2           
		   3         3            3           
		   4         3            4          
		 
		 
		 
	权限：
        login：
              注册session（查询）
        
        中间件：
              # 白名单校验（正则）
              # 登录校验
			  # 权限校验
		 
		 		 

2 admin组件
    Django后台数据库管理工具（web页面）
    目的：
	    1 使用组件
		2 看源码
		3 自己独立开发一个类似组件
		
    		
    1 使用组件admin
	
	  一旦注册Book：
	     url：
		   查看书籍： http://127.0.0.1:8007/admin/app01/book/
           添加书籍   http://127.0.0.1:8007/admin/app01/book/add/
           编辑书籍： http://127.0.0.1:8007/admin/app01/book/1/change/
           删除书籍： http://127.0.0.1:8007/admin/app01/book/1/delete/
		   
		  
	
今日作业：
    1 权限的菜单栏
	2 单例模式


https://www.cnblogs.com/yuanchenqi/articles/8323452.html
https://www.cnblogs.com/yuanchenqi/articles/8715364.html


3 crm
  ---客户表管理
  ---学生以及学习记录的管理
