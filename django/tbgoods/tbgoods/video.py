#coding=utf-8
from django.shortcuts import render
from django import forms
from django.http import HttpResponse,HttpResponseRedirect,StreamingHttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def video_1(request):
    return render(request, 'video/video_1.html')

