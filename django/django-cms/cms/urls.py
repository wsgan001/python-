from django.conf.urls import patterns, include, url
import os

urlpatterns = patterns('',
                       url(r'^admin/login/', 'cmsadmin.views.admin_login'),
                       url(r'^admin/index/', 'cmsadmin.views.admin_index'),
                       url(r'^admin/logout/', 'cmsadmin.views.admin_logout'),
                       url(r'^admin/admin_manager/', 'cmsadmin.views.admin_manager'),
                       url(r'^admin/admin_add', 'cmsadmin.views.admin_add'),
                       url(r'^admin/admin_hasuser/.*', 'cmsadmin.views.admin_hasuser'),
                       url('^css/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resource/css')}),
                       url('^avatars/(?P<path>.*)$', 'django.views.static.serve', {
                           'document_root': os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resource/avatars')}),
                       url('^js/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resource/js')}),
                       url('^images/(?P<path>.*)$', 'django.views.static.serve', {
                           'document_root': os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resource/images')}),
                       url('^font/(?P<path>.*)$', 'django.views.static.serve', {
                           'document_root': os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resource/font')}),
                       )
