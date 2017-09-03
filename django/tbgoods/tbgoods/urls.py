#coding=utf-8
from django.conf.urls import url
from django.contrib import admin
from tb.views import  TbList ,downloadfile,search_info,info_page ,user_list, user_edit              #引用的模板

from view import user_lists
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tblist$', TbList.as_view()),   #class
    url(r'^download/$', downloadfile, name = "tb_downloadfile"),   #def
    url(r'^tblist_s$', search_info),     #关键搜索
    url(r'^tblist_page$', info_page),   #数据分页
    url(r'^user_lists$', user_lists),
    url(r'^user_list$', user_list),
    url(r'^edit-(\d+)$', user_edit),  #\d+为每个用户的编辑页面
]
