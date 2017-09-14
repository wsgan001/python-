#coding=utf-8
from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,StreamingHttpResponse
from tb.models import info,UserInfo,pl,jd_info,jd_pl,bj
import csv
from django.views.decorators import csrf
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from forms import UserInfoModelForm,FileUploadForm

#--------------------------------------------------淘宝商品信息----------------------------------------------------------------------------------------------------------------------------
class TbList(ListView):      #引用模板数据库表
    model = info            #对应模板里面info.list.html,路径在模板目录下文件夹tb里面
    context_object_name = 'my_info'
    template_name = 'tb/info_list.html'   #模板文件
    #paginate_by = 20      #一个页面显示的条目


def download_info(request):  #--------------------------------------下载数据库数据为csv
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=tb_info_list.csv'
        writer = csv.writer(response)
        writer.writerow(['id','ids', 's_name', 'titles', 'price', 'selas','url'])  #定义字段名
        infos=info.objects.all()          #获取所需数据
        for infos in infos:    #遍历数据列表
           if infos.id:
             try :
                s_name = Reader.objects.get(id__iexact = infos.id).name
             except:
                s_name = ''
           else :
             s_name = ''
           writer.writerow([infos.id,infos.ids, infos.s_name, infos.titles,infos.price, infos.selas,infos.url])  #获取模型所需的字段
        return response


def search_info(request):       #搜索数据
    q = request.GET.get('q') #对应htmlinput当中name属性 --  #request.GET.get('q') 获取到用户提交的搜索关键词。用户通过表单提交的数据 django 为我们保存在 request.GET 里，这是一个类似于 Python 字典的对象，所以我们使用 get 方法从字典里取出键 q 对应的值，即用户的搜索关键词。这里字典的键之所以叫 q 是因为我们的表单中搜索框 input 的 name 属性的值是 q，如果修改了 name 属性的值，那么这个键的名称也要相应修改。
    error_msg = ''
    if not q:
        error_msg = '请输入关键词'
        return render(request, 'tb/info_list_s.html', {'error_msg': error_msg})
    info_list = info.objects.filter(s_name__icontains=q)   #用户输入了搜索关键词，我们就通过 filter 方法从数据库里过滤出符合条件的所有数据。icontains为模糊匹配，相当于sql的like
    return render(request, 'tb/info_list_s.html', {'error_msg': error_msg, 'info_list':info_list})


def info_page(request):      #数据分页
    info_list = info.objects.all()  # 获取所有info,假设在models.py中已定义了info模型
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

    return render(request, 'tb/info_list_page.html', {'infos': infos})   #render()这是一个非常常见的习惯用语，用于加载模板，填充上下文并返回一个含有模板渲染结果的 HttpResponse 对象




#--------------------------------------------------淘宝评论信息----------------------------------------------------------------------------------------------------------------------------

def download_pl(request):  #--------------------------------------下载数据库数据为csv
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=tb_pl_list.csv'
        writer = csv.writer(response)
        writer.writerow(['id','itemid','user','sku','date','content'])  #定义字段名
        pls=pl.objects.all()          #获取所需数据
        for pls in pls:    #遍历数据列表

           writer.writerow([pls.id,pls.itemid,pls.user,pls.sku,pls.date,pls.content])  #获取模型所需的字段
        return response


def search_pl(request):       #搜索数据
    q = request.GET.get('q') #对应htmlinput当中name属性 --  #request.GET.get('q') 获取到用户提交的搜索关键词。用户通过表单提交的数据 django 为我们保存在 request.GET 里，这是一个类似于 Python 字典的对象，所以我们使用 get 方法从字典里取出键 q 对应的值，即用户的搜索关键词。这里字典的键之所以叫 q 是因为我们的表单中搜索框 input 的 name 属性的值是 q，如果修改了 name 属性的值，那么这个键的名称也要相应修改。
    error_msg = ''
    if not q:
        error_msg = '请输入关键词'
        return render(request, 'tb/pl_list_s.html', {'error_msg': error_msg})
    pl_list = pl.objects.filter(itemid__icontains=q)   #用户输入了搜索关键词，我们就通过 filter 方法从数据库里过滤出符合条件的所有数据。icontains为模糊匹配，相当于sql的like
    return render(request, 'tb/pl_list_s.html', {'error_msg': error_msg, 'pl_list':pl_list})


def pl_page(request):      #数据分页
    pl_list = pl.objects.all()  # 获取所有info,假设在models.py中已定义了info模型
    paginator = Paginator(pl_list, 20) # 每页25条

    page = request.GET.get('page')
    try:
        pls = paginator.page(page) # infos为Page对象！返回在提供的下标处的 Page  对象，下标以1开始。如果提供的页码不存在，抛出 InvalidPage  异常。
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        pls = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pls = paginator.page(paginator.num_pages)   #页面总数。

    return render(request, 'tb/pl_list_page.html', {'pls': pls})   #render()这是一个非常常见的习惯用语，用于加载模板，填充上下文并返回一个含有模板渲染结果的 HttpResponse 对象




#--------------------------------------------------京东商品信息----------------------------------------------------------------------------------------------------------------------------


def download_jd_info(request):  #--------------------------------------下载数据库数据为csv
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=jd_info_list.csv'
        writer = csv.writer(response)
        writer.writerow(['id', 's_name','ids','store', 'titles', 'price','url'])  #定义字段名
        jd_infos=jd_info.objects.all()          #获取所需数据
        for jd_infos in jd_infos:    #遍历数据列表
           if jd_infos.id:
             try :
                s_name = Reader.objects.get(id__iexact = jd_infos.id).name
             except:
                s_name = ''
           else :
             s_name = ''
           writer.writerow([jd_infos.id, jd_infos.s_name,jd_infos.ids,jd_infos.store, jd_infos.titles,jd_infos.price, jd_infos.url])  #获取模型所需的字段
        return response


def search_jd_info(request):       #搜索数据
    q = request.GET.get('q') #对应htmlinput当中name属性 --  #request.GET.get('q') 获取到用户提交的搜索关键词。用户通过表单提交的数据 django 为我们保存在 request.GET 里，这是一个类似于 Python 字典的对象，所以我们使用 get 方法从字典里取出键 q 对应的值，即用户的搜索关键词。这里字典的键之所以叫 q 是因为我们的表单中搜索框 input 的 name 属性的值是 q，如果修改了 name 属性的值，那么这个键的名称也要相应修改。
    error_msg = ''
    if not q:
        error_msg = '请输入关键词'
        return render(request, 'tb/jd_info_list_s.html', {'error_msg': error_msg})
    jd_info_list = jd_info.objects.filter(s_name__icontains=q)   #用户输入了搜索关键词，我们就通过 filter 方法从数据库里过滤出符合条件的所有数据。icontains为模糊匹配，相当于sql的like
    return render(request, 'tb/jd_info_list_s.html', {'error_msg': error_msg, 'jd_info_list':jd_info_list})


def jd_info_page(request):      #数据分页
    jd_info_list = jd_info.objects.all()  # 获取所有info,假设在models.py中已定义了info模型
    paginator = Paginator(jd_info_list, 20) # 每页25条

    page = request.GET.get('page')
    try:
        jd_infos = paginator.page(page) # infos为Page对象！返回在提供的下标处的 Page  对象，下标以1开始。如果提供的页码不存在，抛出 InvalidPage  异常。
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        jd_infos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        jd_infos = paginator.page(paginator.num_pages)   #页面总数。

    return render(request, 'tb/jd_info_list_page.html', {'jd_infos': jd_infos})   #render()这是一个非常常见的习惯用语，用于加载模板，填充上下文并返回一个含有模板渲染结果的 HttpResponse 对象




#--------------------------------------------------京东评论信息----------------------------------------------------------------------------------------------------------------------------

def download_jd_pl(request):  #--------------------------------------下载数据库数据为csv
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=jd_pl_list.csv'
        writer = csv.writer(response)
        writer.writerow(['id','ids','selas','user','titles','sku','date','content'])  #定义字段名
        jd_pls=jd_pl.objects.all()          #获取所需数据
        for jd_pls in jd_pls:    #遍历数据列表

           writer.writerow([jd_pls.id,jd_pls.ids,jd_pls.selas,jd_pls.user,jd_pls.sku,jd_pls.date,jd_pls.content])  #获取模型所需的字段
        return response


def search_jd_pl(request):       #搜索数据
    q = request.GET.get('q') #对应htmlinput当中name属性 --  #request.GET.get('q') 获取到用户提交的搜索关键词。用户通过表单提交的数据 django 为我们保存在 request.GET 里，这是一个类似于 Python 字典的对象，所以我们使用 get 方法从字典里取出键 q 对应的值，即用户的搜索关键词。这里字典的键之所以叫 q 是因为我们的表单中搜索框 input 的 name 属性的值是 q，如果修改了 name 属性的值，那么这个键的名称也要相应修改。
    error_msg = ''
    if not q:
        error_msg = '请输入关键词'
        return render(request, 'tb/jd_pl_list_s.html', {'error_msg': error_msg})
    jd_pl_list = jd_pl.objects.filter(ids__icontains=q)   #用户输入了搜索关键词，我们就通过 filter 方法从数据库里过滤出符合条件的所有数据。icontains为模糊匹配，相当于sql的like
    return render(request, 'tb/jd_pl_list_s.html', {'error_msg': error_msg, 'jd_pl_list':jd_pl_list})


def jd_pl_page(request):      #数据分页
    jd_pl_list = jd_pl.objects.all()  # 获取所有info,假设在models.py中已定义了info模型
    paginator = Paginator(jd_pl_list, 20) # 每页25条

    page = request.GET.get('page')
    try:
        jd_pls = paginator.page(page) # infos为Page对象！返回在提供的下标处的 Page  对象，下标以1开始。如果提供的页码不存在，抛出 InvalidPage  异常。
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        jd_pls = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        jd_pls = paginator.page(paginator.num_pages)   #页面总数。

    return render(request, 'tb/jd_pl_list_page.html', {'jd_pls': jd_pls})   #render()这是一个非常常见的习惯用语，用于加载模板，填充上下文并返回一个含有模板渲染结果的 HttpResponse 对象



#--------------------------------------------------bj信息----------------------------------------------------------------------------------------------------------------------------



def download_bj(request):  #--------------------------------------下载数据库数据为csv
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=bj_list.csv'
        writer = csv.writer(response)
        writer.writerow(['bj_f_rank','bj_name','bj_id','bj_rank_all','bj_follower','bj_swatch','bj_last_time','bj_last_visit','bj_last_up','bj_info_bs','img'])  #定义字段名
        bjs=bj.objects.all()          #获取所需数据
        for bjs in bjs:    #遍历数据列表
           writer.writerow([bjs.bj_f_rank,bjs.bj_name.encode("utf-8"),bjs.bj_id, bjs.bj_rank_all.encode("utf-8"),bjs.bj_follower,bjs.bj_swatch,bjs.bj_last_time,bjs.bj_last_visit,bjs.bj_last_up,bjs.bj_info_bs.encode("utf-8"),bjs.img])  #获取模型所需的字段
        return response

def search_bj(request):       #搜索数据
    q = request.GET.get('q') #对应htmlinput当中name属性 --  #request.GET.get('q') 获取到用户提交的搜索关键词。用户通过表单提交的数据 django 为我们保存在 request.GET 里，这是一个类似于 Python 字典的对象，所以我们使用 get 方法从字典里取出键 q 对应的值，即用户的搜索关键词。这里字典的键之所以叫 q 是因为我们的表单中搜索框 input 的 name 属性的值是 q，如果修改了 name 属性的值，那么这个键的名称也要相应修改。
    error_msg = ''
    if not q:
        error_msg = '请输入关键词'
        return render(request, 'tb/info_list_s.html', {'error_msg': error_msg})
    bj_list = bj.objects.filter(bj_id__icontains=q)   #用户输入了搜索关键词，我们就通过 filter 方法从数据库里过滤出符合条件的所有数据。icontains为模糊匹配，相当于sql的like
    return render(request, 'tb/bj_list_s.html', {'error_msg': error_msg, 'bj_list':bj_list})

def bj_page(request):      #数据分页
    bj_list =bj.objects.all()  # 获取所有info,假设在models.py中已定义了info模型
    paginator = Paginator(bj_list, 20) # 每页25条

    page = request.GET.get('page')
    try:
        bjs = paginator.page(page) # infos为Page对象！返回在提供的下标处的 Page  对象，下标以1开始。如果提供的页码不存在，抛出 InvalidPage  异常。
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        bjs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        bjs = paginator.page(paginator.num_pages)   #页面总数。

    return render(request, 'tb/bj_list_page.html', {'bjs': bjs})   #render()这是一个非常常见的习惯用语，用于加载模板，填充上下文并返回一个含有模板渲染结果的 HttpResponse 对象

