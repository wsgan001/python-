#coding=utf-8
from django.conf.urls import include, url
from django.contrib import admin
from tb.views import  TbList ,download_info,search_info,info_page,download_pl,search_pl,pl_page,download_jd_info,search_jd_info,jd_info_page,download_jd_pl,search_jd_pl,jd_pl_page ,download_bj,search_bj,bj_page ,download_job_info, search_job_info,job_info_page                                         #引用的模板
from tb.view import  user_list, user_edit ,upload_file,download_file ,uploadlist           #引用的模板
from django.conf import settings
from view import user_lists
from img import img_qh,download_qh
from video import video_1
from chatroom.views import index,post
from tb.ajax import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
   # url(r'^$', admin.site.urls),
    #------------------------------------
    url(r'^tblist$', TbList.as_view()),                                 #---------------------class需要加.as_view()，def不用
    url(r'^download_info/$', download_info),   #def
    url(r'^tblist_s$', search_info),     #关键搜索
    url(r'^tblist_page$', info_page),   #数据分页
    url(r'^download_pl/$', download_pl),   #def
    url(r'^pllist_s$', search_pl),     #关键搜索
    url(r'^pllist_page$', pl_page),   #数据分页
 #---------------------------------------------                               #---------------------class需要加.as_view()，def不用
    url(r'^download_jd_info/$', download_jd_info),   #def
    url(r'^jdlist_s$', search_jd_info),     #关键搜索
    url(r'^jdlist_page$', jd_info_page),   #数据分页
    url(r'^download_jd_pl/$', download_jd_pl),   #def
    url(r'^jd_pllist_s$', search_jd_pl),     #关键搜索
    url(r'^jd_pllist_page$', jd_pl_page),   #数据分页
 #---------------------------------------------
    url(r'^download_bj/$', download_bj),   #def
    url(r'^bjlist_s$', search_bj),     #关键搜索
    url(r'^bjlist_page$',bj_page),   #数据分页
 #---------------------------------------------
    url(r'^download_job_info/$', download_job_info),   #def
    url(r'^joblist_s$', search_job_info),     #关键搜索
    url(r'^joblist_page$', job_info_page),   #数据分页
  #---------------------------------------------
    url(r'^user_lists$', user_lists),
    url(r'^user_list$', user_list),
    url(r'^edit-(\d+)$', user_edit),  #正则表达式（\d+）为每个用户的编辑页面,----数字
    url(r'^upload$', upload_file),
    url(r'^uplist$', uploadlist.as_view(),name = "uplist"), #name值为设置在模板href中引用当前url，好处是只需在修改此url，模板url会自动改变，模式为href="{% url 'name' url其他后缀  %}">
    url(r'^d_up(\d+)$', download_file,name = "d_ups"),         #一个括号代表一个模式，首先将upload_list.html的/d_up{{ uploadfile.id  }}回调给urls的^d_up(\d+)$'，urls将接收到的值回调给视图，即变量nid={{ uploadfile.id  }}
    url(r'^img_qh$', img_qh),
    url(r'^d_qh(\S+)$', download_qh,name = "d_qh"),   #\S+，非空字符
     url(r'^v_1$', video_1),
 #---------------------------------------------
    url(r'^c_index$', index),
    # url(r'^p/(?P<id>\d+)/$', single_post),
    # url(r'^topic/(?P<id>\d+)/$', show_topic),
    url(r'^post/$', post),
 #---------------------------------------------
     url(r'^login/$', home),

]
