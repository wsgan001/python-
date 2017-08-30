# coding=utf-8
from django.contrib.auth.models import User, Group, AbstractBaseUser, \
    AbstractUser
from django.core.urlresolvers import reverse

from django.db import models
from django.utils import timezone
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from .constants import UsableStatus, DICT_NULL_BLANK_TRUE


# Create your models here.
class BaseModel(models.Model):
    creator = models.ForeignKey(
            User,
            verbose_name=u"数据创建人",
            **DICT_NULL_BLANK_TRUE
    )
    created_at = models.DateTimeField(
            verbose_name=u"数据创建时间",
            default=timezone.now
    )
    updated_at = models.DateTimeField(
            verbose_name=u"数据更新时间",
            default=timezone.now
    )
    deleted_at = models.DateTimeField(
            verbose_name=u"数据删除时间",
            **DICT_NULL_BLANK_TRUE
    )

    class Meta:
        abstract = True
