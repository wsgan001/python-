#coding=utf-8
from django.shortcuts import render
from django import forms
from django.http import HttpResponse,HttpResponseRedirect,StreamingHttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def video_1(request):
    num=[]
    for nums in range(1,100):
        num.append(nums)

    paginator = Paginator(num, 5) # 每页25条

    page = request.GET.get('page')
    try:
        nums = paginator.page(page) # infos为Page对象！返回在提供的下标处的 Page  对象，下标以1开始。如果提供的页码不存在，抛出 InvalidPage  异常。
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        nums = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        nums = paginator.page(paginator.num_pages)   #页面总数。
    return render(request, 'video/video_1.html',{'nums':nums})

