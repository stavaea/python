

from stark.service.sites import site,ModelStark

from app01.models import Book
from app01.models import Publish
from app01.models import Author




class BookConfig(ModelStark):


    def display_authors(self, obj=None,is_header=False):

        if is_header:
            return "作者"
        s=[]
        for author in obj.authors.all():
            s.append(author.name)

        return " ".join(s)

    list_display = ["nid","title","price","publish","authors",]

    search_fields=["title","price"]

    def patch_init(self,selected_pk):
        print("selected_pk",selected_pk)
        ret=self.model.objects.filter(pk__in=selected_pk).update(price=0)
        print("====>",ret)

    patch_init.desc="批量初始化"


    def patch_delete(self,selected_pk):
        print("selected_pk",selected_pk)
        ret=self.model.objects.filter(pk__in=selected_pk).delete()
        print("====>",ret)

    patch_delete.desc="批量删除"


    actions=[patch_init,patch_delete]


site.register(Book,BookConfig)



site.register(Publish)
site.register(Author)


print(site._registry)