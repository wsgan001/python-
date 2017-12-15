# -*- coding:utf-8 -*-
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True, null=False)
    count = models.IntegerField(default=0)

    def __unicode__(self):
        return u'%s' % self.name


class Photo(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    link = models.URLField(unique=True, blank=False,null=False)
    description = models.TextField(null=True)
    up_loader = models.ForeignKey(User, related_name='user_has_photos')
    time = models.DateTimeField(auto_now_add=True, default=timezone.now)
    tags = models.ManyToManyField(Tag, related_name='tag_has_photos')
    like_count = models.IntegerField(default=0)

    def __unicode__(self):
        return u'%s' % self.name


class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, related_name='use_has_comments')
    photo = models.ForeignKey(Photo, null=True, related_name='photo_has_comments')
    time = models.DateTimeField(auto_now_add=True, null=True)
    def __unicode__(self):
        return u'%s' % self.content


admin.site.register(Tag)
admin.site.register(Photo)
admin.site.register(Comment)
