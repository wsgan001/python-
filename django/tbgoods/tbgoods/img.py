#coding=utf-8
from django.shortcuts import render
from django import forms
from django.http import HttpResponse,HttpResponseRedirect,StreamingHttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def img_qh(request):      
    list=[]
    for i in range(1,117):
        img='static/img/qh/('+str(i)+').gif'    #构造图片路径
        list.append(img)
    paginator = Paginator(list, 10) # 每页25条

    page = request.GET.get('page')
    try:
        img = paginator.page(page) # infos为Page对象！返回在提供的下标处的 Page  对象，下标以1开始。如果提供的页码不存在，抛出 InvalidPage  异常。
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        img = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        img = paginator.page(paginator.num_pages)   #页面总数。

    return render(request, 'img/img_qh.html', {'img': img})   #render()这是一个非常常见的习惯用语，用于加载模板，填充上下文并返回一个含有模板渲染结果的 HttpResponse 对象


def download_qh(request,im):             #下载文件
      def file_iterator(file_name, chunk_size=512):
        with open(file_name,'rb') as f:  #open('','rb')<以二进制读的方式打开，要不然会有问题
            while True:
                c = f.read(chunk_size)   # read([num_bytes=None])读取文件内容。可选的 size 参数是要读的字节数；没有指定的话，文件会一直读到结尾。
                if c:
                    yield c
                else:
                    break


     #!!!!!!!!!!首先将upload_list.html的/d_up{{ uploadfile.id  }}回调给urls的^d_up(\d+)$'，urls将接收到的值回调给视图，即变量nid={{ uploadfile.id  }}
     # im='static/img/qh/('+str(nid)+').gif'
      the_file_name="./"+im
      name = the_file_name.split('/')
      file_name = name[-1]
      response = StreamingHttpResponse(file_iterator(the_file_name))        #含有路径的文件名称
      response['Content-Type'] = 'application/octet-stream'         #通过文件流传输到浏览器，但文件流通常会以乱码形式显示到浏览器中，而非下载到硬盘上，因此，还要在做点优化，让文件流写入硬盘。优化很简单，给StreamingHttpResponse对象的Content-Type和Content-Disposition字段赋下面的值即可
      response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file_name.encode("utf-8"))  #中文显示，文件名，.format格式化函数，{0}表示位置
      return  response