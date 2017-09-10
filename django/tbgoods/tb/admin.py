# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from tb.models import info,UserInfo,uploadfile,pl,jd_info,jd_pl

class infoAdmin(admin.ModelAdmin):   #定义了一个 ContactAdmin 类，用以说明管理页面的显示格式。
    list_display = ('s_name','ids','titles','price','selas','url','pi_url')        # 页面显示字段
    search_fields = ('ids','s_name')        #搜索字段
    list_per_page = 20           #显示数量，分页


class UserInfoAdmin(admin.ModelAdmin):   #定义了一个 ContactAdmin 类，用以说明管理页面的显示格式。
    list_display = ('username','email','user_type_id')        # 页面显示字段
    search_fields = ('username',)        #搜索字段
    list_per_page = 20           #显示数量，分页

class uploadfileAdmin(admin.ModelAdmin):   #定义了一个 ContactAdmin 类，用以说明管理页面的显示格式。
    list_display = ('file',)        # 页面显示字段
    search_fields = ('file',)        #搜索字段
    list_per_page = 20           #显示数量，分页

class plAdmin(admin.ModelAdmin):   #定义了一个 ContactAdmin 类，用以说明管理页面的显示格式。
    list_display = ('itemid','user','sku','date','content')        # 页面显示字段
    search_fields = ('itemid','date')        #搜索字段
    list_per_page = 20

class jd_infoAdmin(admin.ModelAdmin):   #定义了一个 ContactAdmin 类，用以说明管理页面的显示格式。
    list_display = ('s_name','ids','store','titles','price','url')        # 页面显示字段
    search_fields = ('ids','s_name')        #搜索字段
    list_per_page = 20

class jd_plAdmin(admin.ModelAdmin):   #定义了一个 ContactAdmin 类，用以说明管理页面的显示格式。
    list_display = ('ids','selas','user','titles','sku','date','content')        # 页面显示字段
    search_fields = ('itemid','date')        #搜索字段
    list_per_page = 20

admin.site.register(info,infoAdmin)
admin.site.register(UserInfo,UserInfoAdmin)
admin.site.register(uploadfile,uploadfileAdmin)
admin.site.register(pl,plAdmin)
admin.site.register(jd_info,jd_infoAdmin)
admin.site.register(jd_pl,jd_plAdmin)