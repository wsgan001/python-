#coding=utf-8
from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,StreamingHttpResponse
from tb.models import UserInfo,uploadfile
import csv
from django.views.decorators import csrf
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from forms import UserInfoModelForm,FileUploadForm



def user_list(request):               #数据库表单操作
    li = UserInfo.objects.all().select_related('user_type')  # 这里只能是外键，多对多字段也不可以
    lis= UserInfo.objects.with_counts()
    return render(request,'tb/user_list.html',{'li': li,'lis': lis})

def user_edit(request, nid):             #数据库表单操作，添加修改用户
    # 获取当前id对象的用户信息
    # 显示用户已经存在数据
    if request.method == "GET":
        user_obj = UserInfo.objects.filter(id=nid).first()    #查找id=nid的一行
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

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def upload_file(request):         #上传文件
    """
    文件接收 view
    :param request: 请求
    :return:
    """
    if request.method == 'POST':        #POST和GET是HTTP协议定义的与服务器交互的方法。GET一般用于获取/查询 资源信息，而POST一般用于更新 资源信息。GET提交，请求的数据会附在URL之后（就是把数据放置在HTTP协议头中），以?分割URL和传输数据，多个参数用&连接；POST提交：把提交的数据放置在是HTTP包的包体中。GET提交的数据会在地址栏中显示出来，而POST提交，地址栏不会改变
        my_form = FileUploadForm(request.POST, request.FILES) #文件上传的时候，文件数据被保存在 request. FILES
        if my_form.is_valid():
          #  f = my_form.cleaned_data['my_file']
          #  handle_uploaded_file(f)
            file_model = uploadfile()                 #保存记录到数据库
            file_model.file = my_form.cleaned_data['my_file']  #不管表单提交的是什么数据，一旦通过调用 is_valid() 成功验证（ is_valid() 返回 True ），验证后的表单数据将位于 form.cleaned_data字典中。这些数据已经为你转换好为Python 的类型。
            file_model.save()
        return HttpResponse('Upload Success')
    else:
        my_form = FileUploadForm()
    return render(request, 'tb/upload.html', {'form': my_form})   #根据html的请求，视图将返回特定的html模板以及字典参数数据
"""
def handle_uploaded_file(f):      #保存上传文件
    file_name = f.name    #图片名称
    path="E:\\tae\django\\tbgoods\\upload"
    file_path='%s/%s'%(path,file_name)
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)"""


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class uploadlist(ListView):
    model = uploadfile          #对应模板里面info.list.html,路径在模板目录下文件夹tb里面
    context_object_name = 'my_uploadfile'
    template_name = 'tb/upload_list.html'   #模板文件
    #paginate_by = 20      #一个页面显示的条目


def download_file(request,nid):             #下载文件
      def file_iterator(file_name, chunk_size=512):
        with open(file_name,'rb') as f:  #open('','rb')<以二进制读的方式打开，要不然会有问题
            while True:
                c = f.read(chunk_size)   # read([num_bytes=None])读取文件内容。可选的 size 参数是要读的字节数；没有指定的话，文件会一直读到结尾。
                if c:
                    yield c
                else:
                    break

      f=uploadfile.objects.values('file')  #获取某个字段的所有值：[{字段：值}]
      page=int(nid)-int(1)                    #!!!!!!!!!!首先将upload_list.html的/d_up{{ uploadfile.id  }}回调给urls的^d_up(\d+)$'，urls将接收到的值回调给视图，即变量nid={{ uploadfile.id  }}
      uploadfiles=f[page]['file']   #  page根据字段id值nid与数组所要返回的位置差值确定
      the_file_name="./"+uploadfiles
   #   the_file_name =  "./upload/1.zip"
      name = the_file_name.split('/')
      file_name = name[-1]
      response = StreamingHttpResponse(file_iterator(the_file_name))        #含有路径的文件名称
      response['Content-Type'] = 'application/octet-stream'         #通过文件流传输到浏览器，但文件流通常会以乱码形式显示到浏览器中，而非下载到硬盘上，因此，还要在做点优化，让文件流写入硬盘。优化很简单，给StreamingHttpResponse对象的Content-Type和Content-Disposition字段赋下面的值即可
      response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file_name.encode("utf-8"))  #中文显示，文件名，.format格式化函数，{0}表示位置
      return  response

"""
下面是URLconf 解析器使用的算法，针对正则表达式中的命名组和非命名组：
1. 如果有命名参数，则使用这些命名参数，忽略非命名参数。
2. 否则，它将以位置参数传递所有的非命名参数。"""

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------