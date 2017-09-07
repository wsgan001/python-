#coding=utf-8
from django.conf.urls import include, url
from django.contrib import admin
from tb.views import  TbList ,downloadfile,search_info,info_page ,user_list, user_edit ,upload_file,download_file ,uploadlist           #引用的模板
from django.conf import settings
from view import user_lists
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tblist$', TbList.as_view()),                                 #---------------------class需要加.as_view()，def不用
    url(r'^download/$', downloadfile, name = "tb_downloadfile"),   #def
    url(r'^tblist_s$', search_info),     #关键搜索
    url(r'^tblist_page$', info_page),   #数据分页
    url(r'^user_lists$', user_lists),
    url(r'^user_list$', user_list),
    url(r'^edit-(\d+)$', user_edit),  #\d+为每个用户的编辑页面
    url(r'^upload$', upload_file),
    url(r'^uplist$', uploadlist.as_view()),
  #  url(r'^d_up$', download_file),
    url(r'^d_up(\d+)$', download_file),     #一个括号代表一个模式，首先将upload_list.html的/d_up{{ uploadfile.id  }}回调给urls的^d_up(\d+)$'，urls将接收到的值回调给视图，即变量nid={{ uploadfile.id  }}

]
