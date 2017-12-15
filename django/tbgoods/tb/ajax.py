#coding=utf-8
import json
from django.shortcuts import render

def home(request):
    List = ['自强学堂', '渲染Json到模板']
    Dict = {'site': '自强学堂', 'author': '涂伟忠'}
    return render(request, 'ajax/login.html', {
            'List': json.dumps(List),
            'Dict': json.dumps(Dict)
        })
