__author__ = 'zhufree'
from django.conf.urls import patterns, url
from views import *

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'sample.views.home', name='home'),
    url(r'^$', index),
    url(r'^bind/$', bind),
    url(r'^getsignstatus/$',get_sign_status),
    url(r'^sign/$', sign),

)
