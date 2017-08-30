# coding=utf-8
from django.contrib.auth.models import User, Group, AbstractBaseUser, \
    AbstractUser
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from common.constants import UsableStatus, DICT_NULL_BLANK_TRUE, TRUE_FALSE
from common.models import BaseModel


class CustomerCategory(BaseModel, UsableStatus):
    name = models.CharField(
            u"客户分类名称", max_length=255, unique=True
    )

    def __unicode__(self):
        return u"%s" % self.name

    class Meta:
        verbose_name_plural = verbose_name = u"客户分类"


class Customer(BaseModel, UsableStatus):
    customerCategory = models.ForeignKey(
            CustomerCategory, verbose_name=u'客户分类'
    )
    name = models.CharField(
            u"客户名称", max_length=255, unique=True
    )
    address = models.CharField(
            u"地址", max_length=500, **DICT_NULL_BLANK_TRUE
    )
    concat = models.CharField(
            u"联系人", max_length=255, **DICT_NULL_BLANK_TRUE
    )
    mobile = models.CharField(
            u"手机", max_length=255, **DICT_NULL_BLANK_TRUE
    )
    phone = models.CharField(
            u"固话", max_length=255, **DICT_NULL_BLANK_TRUE
    )
    qq = models.CharField(
            u"QQ", max_length=255, **DICT_NULL_BLANK_TRUE
    )
    backconcat = models.CharField(
            u"备份联系人", max_length=255, **DICT_NULL_BLANK_TRUE
    )
    backmobile = models.CharField(
            u"备份联系人手机", max_length=255, **DICT_NULL_BLANK_TRUE
    )
    backphone = models.CharField(
            u"备份联系人固话", max_length=255, **DICT_NULL_BLANK_TRUE
    )
    backqq = models.CharField(
            u"备份联系人QQ", max_length=255, **DICT_NULL_BLANK_TRUE
    )
    goodaddr = models.CharField(
            u"发货地址", max_length=255, **DICT_NULL_BLANK_TRUE
    )
    bankaddr = models.CharField(
            u"开户行", max_length=255, **DICT_NULL_BLANK_TRUE
    )
    bankcode = models.CharField(
            u"开户行账号", max_length=255, **DICT_NULL_BLANK_TRUE
    )
    taxcode = models.CharField(
            u"税号", max_length=255, **DICT_NULL_BLANK_TRUE
    )
    fax = models.CharField(
            u"传真", max_length=255, **DICT_NULL_BLANK_TRUE
    )
    shouldpaymoney = models.DecimalField(
            u"应付期初余额", decimal_places=2, max_digits=10, **DICT_NULL_BLANK_TRUE
    )
    shouldpaymoneyDate = models.DateField(
            u"余额日期", **DICT_NULL_BLANK_TRUE
    )
    comments = models.CharField(
            u"备注", max_length=500, **DICT_NULL_BLANK_TRUE
    )

    def __unicode__(self):
        return u"%s" % self.name

    class Meta:
        verbose_name_plural = verbose_name = u"客户资料"
