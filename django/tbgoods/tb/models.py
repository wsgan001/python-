# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm

#-------------------------------------------------------------------------------------------------------------------------#-------------------------------------------------------------------------------------------------------------------------
class info(models.Model):
     s_name = models.CharField(max_length=200)
     ids = models.CharField(max_length=50)
     titles = models.CharField(max_length=500)
     price= models.CharField(max_length=200)
     selas=models.CharField(max_length=200)
     url = models.CharField(max_length=500)
     pi_url = models.CharField(max_length=500)
     def __str__(self):# 其他属性： __unicode__ on Python 2
        return self.s_name

class pl(models.Model):             #淘宝评论信息
     itemid = models.CharField(max_length=200)
     user = models.CharField(max_length=50)
     sku = models.CharField(max_length=500)
     date= models.CharField(max_length=200)
     content=models.CharField(max_length=5000)

#-------------------------------------------------------------------------------------------------------------------------#-------------------------------------------------------------------------------------------------------------------------



class jd_info(models.Model):
      s_name= models.CharField(max_length=200)
      ids= models.CharField(max_length=200)
      store= models.CharField(max_length=200)
      titles= models.CharField(max_length=500)
      price= models.CharField(max_length=200)
      url= models.CharField(max_length=200)
      pi_url = models.CharField(max_length=500)

class jd_pl(models.Model):
   ids= models.CharField(max_length=200)
   selas= models.CharField(max_length=200)
   user= models.CharField(max_length=200)
   titles= models.CharField(max_length=500)
   sku= models.CharField(max_length=500)
   date= models.CharField(max_length=200)
   content= models.CharField(max_length=5000)

#-------------------------------------------------------------------------------------------------------------------------#-------------------------------------------------------------------------------------------------------------------------



class UserManager(models.Manager):        #此管理器必需放在引用此方法的模型前面，否则出错，（即放在UserInfo(models.Model):前面）
   def get_queryset(self):
           return super(UserManager, self).get_queryset().filter(username='抽')    #调用超类的方法——  super(Blog, self)，get_queryset() 会根据你所需要的属性返回 查询集

class UsersManager(models.Manager):
   def with_counts(self):
     from django.db import connection
     cursor = connection.cursor()
     cursor.execute("""
         SELECT p.id, p.username, p.email, p.user_type_id,COUNT(*)          #COUNT(*)
          FROM tb_UserInfo p
           GROUP BY  p.username, p.email, p.user_type_id       #COUNT(*)可以判断GROUP BY这些字段都相同的重复用户
                         """)
     result_list = []
     for row in cursor.fetchall():
       p = self.model(id=row[0], username=row[1], email=row[2],user_type_id=row[3])   #管理器方法可以访问 self.model来得到它所用到的模型类
       p.num_responses = row[4]          #列表中的每个对象都多了一个名为 num_responses的属性
       result_list.append(p)
     return result_list             #UserInfo.objects.with_counts() 得到所有含有num_responses属性的 OpinionPoll对象

class UserType(models.Model):
    caption = models.CharField(max_length=32)
    def __unicode__(self):  #__unicode__() 方法可以进行任何处理来返回对一个对象的字符串表示。方法未返回一个Unicode对象，而返回比如说一个整型数字，那么Python将抛出一个`` TypeError`` 错误，并提示：”coercing to Unicode: need string or buffer, int found” ，加上去后UserInfo的user_type才能正常显示文字信息，不然会显示UserType.object.
      return  self.caption               #u'%s %s'%(self.captions,self.caption)

class UserInfo(models.Model):
    username = models.CharField(max_length=32, verbose_name='用户')
    email = models.EmailField(verbose_name='邮箱')    #如何定义http上定义的字段呢，自定义写成中文的？之前的用法是在Form里写上label。Model Form定义要用verbose_name
    user_type = models.ForeignKey(to='UserType',to_field='id', verbose_name='类型')  #外键引用表UserType里的id，即该字段实际为user_type_id,页面返回的是return  self.caption 的相应字段
    #objects = models.Manager()
    #objects = UserManager()   #调用管理器，查询相应的条件数据
    objects = UsersManager()

class UserGroup(models.Model):
    name = models.CharField(max_length=32)


#-------------------------------------------------------------------------------------------------------------------------#-------------------------------------------------------------------------------------------------------------------------

class uploadfile(models.Model):
    """
    文件接收 Model
    upload_to：表示文件保存位置
    """
   # file = models.FileField(upload_to="D:/BaiduYunDownload/django/tbgoods/upload/%d")
    file = models.FileField(upload_to="./upload")                       #相对路径./upload/加”.“

#-------------------------------------------------------------------------------------------------------------------------#-------------------------------------------------------------------------------------------------------------------------

class bj(models.Model):
   bj_f_rank= models.CharField(max_length=200)
   bj_name= models.CharField(max_length=200)
   bj_id= models.CharField(max_length=200)
   bj_rank_all= models.CharField(max_length=500)
   bj_follower= models.CharField(max_length=500)
   bj_swatch= models.CharField(max_length=200)
   bj_last_time= models.CharField(max_length=500)
   bj_last_visit= models.CharField(max_length=500)
   bj_last_up= models.CharField(max_length=500)
   bj_info_bs= models.CharField(max_length=5000)
   bj_url= models.CharField(max_length=500)
   img= models.CharField(max_length=500)

#-------------------------------------------------------------------------------------------------------------------------#-------------------------------------------------------------------------------------------------------------------------


