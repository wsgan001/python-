#coding=utf-8
from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from tb.models import info,UserInfo
import csv
from django.views.decorators import csrf
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from forms import UserInfoModelForm

class TbList(ListView):      #引用模板数据库表
    model = info            #对应模板里面info.list.html,路径在模板目录下文件夹tb里面
    context_object_name = 'my_info'
    template_name = 'tb/info_list.html'   #模板文件
    #paginate_by = 20      #一个页面显示的条目

def downloadfile(request):  #--------------------------------------下载csv
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=tb_info_list.csv'
        writer = csv.writer(response)
        writer.writerow(['id', 's_name', 'titles', 'price', 'selas','url'])  #定义字段名
        infos=info.objects.all()          #获取所需数据
        for infos in infos:    #遍历数据列表
           if infos.id:
             try :
                s_name = Reader.objects.get(id__iexact = infos.id).name
             except:
                s_name = ''
           else :
             s_name = ''
           writer.writerow([infos.id, infos.s_name, infos.titles,infos.price, infos.selas,infos.url])  #获取模型所需的字段
        return response



def search_info(request):       #搜索数据
    q = request.GET.get('q') #对应htmlinput当中name属性 --  #request.GET.get('q') 获取到用户提交的搜索关键词。用户通过表单提交的数据 django 为我们保存在 request.GET 里，这是一个类似于 Python 字典的对象，所以我们使用 get 方法从字典里取出键 q 对应的值，即用户的搜索关键词。这里字典的键之所以叫 q 是因为我们的表单中搜索框 input 的 name 属性的值是 q，如果修改了 name 属性的值，那么这个键的名称也要相应修改。
    error_msg = ''
    if not q:
        error_msg = '请输入关键词'
        return render(request, 'tb/info_list_s.html', {'error_msg': error_msg})
    info_list = info.objects.filter(s_name__icontains=q)   #用户输入了搜索关键词，我们就通过 filter 方法从数据库里过滤出符合条件的所有数据。这里的过滤条件是 title__icontains=q
    return render(request, 'tb/info_list_s.html', {'error_msg': error_msg, 'info_list':info_list})


def info_page(request):      #数据分页
    info_list = info.objects.all()  # 获取所有contacts,假设在models.py中已定义了Contacts模型
    paginator = Paginator(info_list, 20) # 每页25条

    page = request.GET.get('page')
    try:
        infos = paginator.page(page) # infos为Page对象！返回在提供的下标处的 Page  对象，下标以1开始。如果提供的页码不存在，抛出 InvalidPage  异常。
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        infos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        infos = paginator.page(paginator.num_pages)   #页面总数。

    return render(request, 'tb/info_list_page.html', {'infos': infos})




def user_list(request):               #数据库表单操作
    li = UserInfo.objects.all().select_related('user_type')  # 这里只能是外键，多对多字段也不可以
    return render(request,'tb/user_list.html',{'li': li})

def user_edit(request, nid):             #数据库表单操作
    # 获取当前id对象的用户信息
    # 显示用户已经存在数据
    if request.method == "GET":
        user_obj = UserInfo.objects.filter(id=nid).first()
        mf = UserInfoModelForm(instance=user_obj)   # 把默认数据传递进去 ，instance  属性，表示与它绑定的模型实例
        return render(request,'tb/user_edit.html',{'mf': mf, 'nid': nid})
    elif request.method == 'POST':
        # 数据修改的信息，给数据库的哪一行做修改？
        user_obj = UserInfo.objects.filter(id=nid).first()
        mf = UserInfoModelForm(request.POST,instance=user_obj)  # 指定给谁做修改
        if mf.is_valid():    #模型表单的验证在调用
            mf.save()             #根据表单绑定的数据创建并保存数据库对
        else:
            print mf.errors.as_json()          #实例而带有 as_  前缀的方法可以渲染它们
        return render(request,'tb/user_edit.html',{'mf': mf, 'nid': nid})
"""
save源码里：
def save(self, commit=True):
    """"""
    if commit:
        self.instance.save()    # 指的当前model对象
        self._save_m2m()        # 指：保存m2m对象
    else:
        self.save_m2m = self._save_m2m
    return self.instance    # model 类的对象

所以instance = obj.save(False)时，什么都不会操作。

if obj.is_valid():
    instance = obj.save(False)
    instance.save()     # 当前对象表数据创建
    obj.save_m2m()      # 多对多表数据创建
    # 上面这三句完成的是和上面 obj.save 一样的操作。拆开就可以自定制操作了"""