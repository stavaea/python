from django.conf.urls import include, url

urlpatterns = [
    url(r'^home/', 'demo.views.home'),
    url(r'^index/', 'demo.views.index'),
    url(r'^bugs/', 'demo.views.bugs'),
    url(r'^error/', 'demo.views.error'),
    url(r'^login/', 'demo.views.login'),
]