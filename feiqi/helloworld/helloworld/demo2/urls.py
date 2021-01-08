from django.conf.urls import include, url

urlpatterns = [
    url(r'^home/(?P<id>\d{2})/$', 'demo2.views.home'),
]