

from django import template

from blog.models import *

register=template.Library()

@register.inclusion_tag("menu.html")
def get_query_data(username):
    # 查当前站点的用户对象
    user = UserInfo.objects.filter(username=username).first()

    #  查询当前站点对象
    blog = user.blog

    # 查询每一个分类的名称以及对应的文章数
    from django.db.models import Count
    cate_list = Category.objects.filter(blog=blog).annotate(c=Count("article")).values_list("title", "c")

    # ret=Article.objects.all().values("user").annotate(c=Count("title")).values("user_id","c")
    # print(ret.query)
    # print(ret)
    # 查询每一个标签的名称以及对应的文章数

    tag_list = Tag.objects.filter(blog=blog).annotate(c=Count("article")).values_list("title", "c")
    print(tag_list)

    date_list = Article.objects.filter(user=user).extra(select={"time": "strftime('%%Y-%%m',create_time)"}).values(
        "time").annotate(c=Count("title")).values_list("time", "c")
    print(date_list)

    return {"username": username, "cate_list": cate_list, "tag_list": tag_list, "date_list": date_list, "blog": blog}
