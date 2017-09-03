#coding=utf-8
from django.shortcuts import render
from django import forms

class UserInfo(forms.Form):
     email = forms.EmailField(required=True)   #required是否可以为空,如果为False说明可以为空
     host = forms.CharField()    #如果required不写默认为Ture
     port = forms.CharField()
     mobile = forms.CharField()

def user_lists(request):
    obj = UserInfo()   #创建了这个对象
    if request.method == 'POST':
        #获取用户输入一句话就搞定
        user_input_obj = UserInfo(request.POST)
        '''
        咱们把post过来的数据当参数传给UserInfo咱们定义的这个类,UserInfo会自动会去你提交的数据
              email/host/port/mobile 自动的封装到user_input_obj里,封装到这个对象里我们就可以判断输入是否合法
        '''
        if user_input_obj.is_valid():       #判断用户输入是否合法
             data = user_input_obj.clean()   #获取用户输入
             print data
        else:
            #如果发生错误,捕捉错误。
            error_msg = user_input_obj.errors
            print error_msg    #打印一下然后看下他的类型
            '''
            <ul class="errorlist">
            <li>mobile<ul class="errorlist"><li>This field is required.
            </li></ul></li>
            <li>host<ul class="errorlist"><li>This field is required.</li></ul></li>
            <li>port<ul class="errorlist"><li>This field is required.</li></ul></li>
            </ul>
            '''
            #然后把错误信息返回
            return render(request,'user_list.html',{'obj':obj,'errors':error_msg,})  #然后把对象传给html,在把错误信息传递过去
    return render(request,'user_lists.html',{'obj':obj,})   #然后把对象传给html
