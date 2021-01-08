from django.contrib import admin

# Register your models here.
from .models import *




class BookConfig(admin.ModelAdmin):
    list_display = ["nid","title","price","publishDate","publish"]

    list_display_links=["title","price"]

    list_filter=["title","publish"]
    search_fields=["title"]


    def patch_init(self,request,queryset):
        queryset.update(price=100)

    patch_init.short_description = "批量初始化"


    actions = [patch_init]

    #change_list_template="list.html"

    ordering=("price","nid",)



admin.site.register(Book,BookConfig)




admin.site.register(Publish)
admin.site.register(Author)
admin.site.register(AuthorDetail)
