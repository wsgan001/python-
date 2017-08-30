#coding=utf-8
from django.views.generic import ListView
from tb.models import info

class TbList(ListView):      #引用模板数据库表
    model = info            #对应模板里面info.list.html,路径在模板目录下文件夹tb里面
    context_object_name = 'my_favorite_info'
