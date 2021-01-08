from django.conf.urls import url

from django.shortcuts import HttpResponse, render,redirect
from django.utils.safestring import mark_safe
from django.urls import reverse

class Show_List(object):
    def __init__(self,config,data_list):
        self.config=config
        self.data_list=data_list

    def get_header(self):
        # 处理表头
        # header_list=["ID","名称","价格"]
        header_list = []
        for field in self.config.new_list_display():
            if isinstance(field, str):
                if field == "__str__":
                    val = self.config.model._meta.model_name.upper()
                else:
                    field_obj = self.config.model._meta.get_field(field)
                    val = field_obj.verbose_name
            else:
                val = field(self.config, is_header=True)
            header_list.append(val)

        return header_list


    def get_body(self):
        # 处理表单数据

        new_data_list = []
        for obj in self.data_list:
            temp = []
            for field in self.config.new_list_display():  # ["nid","title","price","authors",edit]    ['__str__']     ["title","price"]
                if isinstance(field, str):
                    try:
                        from django.db.models.fields.related import ManyToManyField
                        field_obj = self.config.model._meta.get_field(field)
                        if isinstance(field_obj, ManyToManyField):
                            l = []
                            for i in getattr(obj, field).all():
                                l.append(str(i))
                            val = ",".join(l)

                        else:
                            val = getattr(obj, field)
                            print("val", val)
                    except Exception as e:
                        val = getattr(obj, field)

                else:
                    val = field(self.config, obj)
                temp.append(val)

            new_data_list.append(temp)

        '''
        new_data_list=[
           [1 "python",121,"<a href='/stark/app01/book/1/change'>编辑</a>"],

           [2，"go",124，"<a href='/stark/app01/book/2/change'>编辑</a>"],
       ]


       '''

        return new_data_list

    def get_new_actions(self):

        action_list=[]
        for i in self.config.actions: # [patch_init,]
            action_list.append({
                "desc":i.desc,
                "name":i.__name__,
            })

        return action_list

class ModelStark():
    list_display = ["__str__",]
    search_fields=[]

    actions=[]

    def __init__(self, model, site):
        self.model = model
        self.site = site

    def edit(self, obj=None, is_header=False):

        if is_header:
            return "操作"
        return mark_safe("<a href='%s/change'>编辑</a>" % obj.pk)

    def delete(self, obj=None, is_header=False):
        if is_header:
            return "操作"
        return mark_safe("<a href='%s/delete'>删除</a>" % obj.pk)

    def checkbox(self, obj=None, is_header=False):
        if is_header:
            return "选择"
        return mark_safe("<input type='checkbox' name='selected_pk' value=%s>" % obj.pk)



    def get_list_url(self):
        model_name = self.model._meta.model_name
        app_label = self.model._meta.app_label
        _url=reverse("%s_%s_list"%(app_label,model_name))

        return _url







    def new_list_display(self):

        temp=[]
        temp.append(ModelStark.checkbox)
        temp.extend(self.list_display)
        temp.append(ModelStark.edit)
        temp.append(ModelStark.delete)

        return temp

    def get_search_condition(self,request):
        from django.db.models import Q
        search_condition = Q()
        val = request.GET.get("q")
        if val:
            search_condition.connector = "or"

            for field in self.search_fields:
                search_condition.children.append((field + "__contains", val))

        return search_condition

    def list_view(self, request):
        if request.method=="POST":

            action=request.POST.get("action")
            selected_pk=request.POST.getlist("selected_pk")

            action=getattr(self,action)

            action(selected_pk)


        search_condition=self.get_search_condition(request)

        data_list = self.model.objects.all().filter(search_condition)

        print("list_display", self.list_display)  #  ["nid","title","price",edit]

        sl=Show_List(self,data_list)

        return render(request, "list_view.html", locals())

    def get_mdoelForm(self):
        from django.forms import ModelForm
        class DemoModelForm(ModelForm):
            class Meta:
                model = self.model
                fields = "__all__"

        return DemoModelForm

    def add(self, request):



        if request.method=="POST":
            form= self.get_mdoelForm()(request.POST)

            if form.is_valid():
                form.save()

                return redirect(self.get_list_url())
            else:
                return render(request, "add.html", locals())



        form= form= self.get_mdoelForm()()

        return render(request, "add.html", locals())

    def change(self, request, id):

        obj=self.model.objects.filter(pk=id).first()

        if request.method=="POST":
            form = self.get_mdoelForm()(request.POST,instance=obj)

            if form.is_valid():
                form.save()

                return redirect(self.get_list_url())


        form = self.get_mdoelForm()(instance=obj)



        return render(request, "change.html", locals())

    def delete_view(self, request, id):
        if request.method=="POST":
            self.model.objects.get(pk=id).delete()

            return redirect(self.get_list_url())
        url=self.get_list_url()
        return render(request, "delete.html", locals())

    def get_urls2(self):

        model_name=self.model._meta.model_name
        app_label=self.model._meta.app_label

        temp = [
            url("^add/$", self.add,name="%s_%s_add"%(app_label,model_name)),
            url("^$", self.list_view,name="%s_%s_list"%(app_label,model_name)),
            url("^(\d+)/change/$", self.change,name="%s_%s_change"%(app_label,model_name)),
            url("^(\d+)/delete/$", self.delete_view,name="%s_%s_delete"%(app_label,model_name)),
        ]

        return temp

    @property
    def urls2(self):
        return self.get_urls2(), None, None


class StarkSite():
    def __init__(self, ):
        self._registry = {}

    # 一级分发
    def get_urls(self):
        temp = []
        for model, model_class_obj in self._registry.items():  # {Book:ModelAdmin(Book),Publish:ModelAdmn(Publish),....}

            app_name = model._meta.app_label
            model_name = model._meta.model_name
            temp.append(url(r"%s/%s/" % (app_name, model_name), model_class_obj.urls2))

        return temp

    @property
    def urls(self):
        return self.get_urls(), None, None

    def register(self, model, admin_class=None, **options):
        if not admin_class:
            admin_class = ModelStark

        self._registry[model] = admin_class(model, self)


site = StarkSite()

'''
       
        temp.append(url(r"app01/book",ModelAdmin(Book).urls2))
        temp.append(url(r"app01/publish",ModelAdmin(Publish).urls2))


        '''
