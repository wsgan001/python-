# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from tb.models import info,UserInfo,uploadfile,pl,jd_info,jd_pl,bj,job_info

class infoAdmin(admin.ModelAdmin):   #定义了一个 ContactAdmin 类，用以说明管理页面的显示格式。
    list_display = ('s_name','ids','titles','price','selas','url','pi_url')        # 页面显示字段
    search_fields = ('ids','s_name')
    list_per_page = 20                  #显示数量，分页


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('username','email','user_type')
    search_fields = ('username',)
    list_per_page = 20

class uploadfileAdmin(admin.ModelAdmin):
    list_display = ('filepath',)
    search_fields = ('filepath',)
    list_per_page = 20

class plAdmin(admin.ModelAdmin):   #定义了一个 ContactAdmin 类，用以说明管理页面的显示格式。
    list_display = ('itemid','user','sku','date','content')        # 页面显示字段
    search_fields = ('itemid','date')        #搜索字段
    list_per_page = 20

class jd_infoAdmin(admin.ModelAdmin):   #定义了一个 ContactAdmin 类，用以说明管理页面的显示格式。
    list_display = ('s_name','ids','store','titles','price','url','pi_url')        # 页面显示字段
    search_fields = ('ids','s_name')        #搜索字段
    list_per_page = 20

class jd_plAdmin(admin.ModelAdmin):   #定义了一个 ContactAdmin 类，用以说明管理页面的显示格式。
    list_display = ('ids','selas','user','titles','sku','date','content')        # 页面显示字段
    search_fields = ('itemid','date')        #搜索字段
    list_per_page = 20

class bjAdmin(admin.ModelAdmin):
    list_display = ('bj_f_rank','bj_name','bj_id','bj_rank_all','bj_follower','bj_swatch','bj_last_time','bj_last_visit','bj_last_up','bj_info_bs','bj_url','img')        # 页面显示字段
    search_fields = ('bj_name','bj_id')        #搜索字段
    list_per_page = 20

class job_infoAdmin(admin.ModelAdmin):
    list_display = ('s_name','time','name','ares','money','company','people','fuli','describes','url')        # 页面显示字段
    search_fields = ('s_name','name','ares')        #搜索字段
    list_per_page = 20

admin.site.register(info,infoAdmin)
admin.site.register(UserInfo,UserInfoAdmin)
admin.site.register(uploadfile,uploadfileAdmin)
admin.site.register(pl,plAdmin)
admin.site.register(jd_info,jd_infoAdmin)
admin.site.register(jd_pl,jd_plAdmin)
admin.site.register(bj,bjAdmin)
admin.site.register(job_info,job_infoAdmin)
