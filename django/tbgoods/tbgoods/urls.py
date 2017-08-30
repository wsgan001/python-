#coding=utf-8
from django.conf.urls import url
from django.contrib import admin
from tb.views import  TbList   #引用的模板

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tblist$', TbList.as_view()),
]
