# coding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from cmsadmin.forms import LoginForm, AdminAddForm


cms_login_required = login_required(login_url='/admin/login')


@cms_login_required
def admin_index(request):
    return render_to_response('admin/index.html', context_instance=RequestContext(request))


def admin_login(request):
    # 用户如果已经登录就跳转到首页
    if request.user.is_authenticated():
        return HttpResponseRedirect('/admin/index')

    if request.POST:
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            admin_name = data['admin_name']
            admin_pass = data['admin_pass']
            user = auth.authenticate(username=admin_name, password=admin_pass)

            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect('/admin/index')
            else:
                return render_to_response('admin/error-404.html', {'error': '管理员不存在或密码填写错误'})
    else:
        form = LoginForm()
    return render_to_response('admin/login.html', {'form': form}, context_instance=RequestContext(request))


def admin_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/admin/login')


@cms_login_required
def admin_manager(request):
    users = User.objects.all()
    data = {'users': users}

    return render_to_response('admin/admin_manage.html', data, context_instance=RequestContext(request))


@cms_login_required
def admin_add(request):
    if request.POST:
        form = AdminAddForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            data['is_active'] = ','.join(request.REQUEST.getlist('is_active'))
            _create_user(**data)
            return HttpResponseRedirect('/admin/admin_manager')
    else:
        form = AdminAddForm()

    return render_to_response('admin/admin_add.html', {'form': form}, context_instance=RequestContext(request))


@cms_login_required
def admin_hasuser(request):
    username = request.GET['username']

    try:
        User.objects.get(username=username)
        return HttpResponse('exist')
    except User.DoesNotExist, e:
        return HttpResponse('not exist')


def _create_user(*args, **kwargs):
    is_active = kwargs.pop('is_active', None)

    kwargs.pop('notpass')
    user = User.objects.create_user(*args, **kwargs)

    if is_active == 1:
        user.is_active = 1
    else:
        user.is_active = 0

    user.save()

    return True



