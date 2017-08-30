# coding=utf-8
from django.contrib.auth.models import User, Group, AbstractBaseUser, \
    AbstractUser
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from common.constants import UsableStatus, DICT_NULL_BLANK_TRUE, TRUE_FALSE
from common.models import BaseModel


class GoodsUnit(BaseModel, UsableStatus):
    name = models.CharField(
            u"计量单位", max_length=255, unique=True
    )

    def __unicode__(self):
        return u"%s" % self.name

    class Meta:
        verbose_name_plural = verbose_name = u"商品计量单位"


class Warehouse(BaseModel, UsableStatus):
    code = models.CharField(
            u"仓库编码", max_length=255, unique=True
    )
    name = models.CharField(
            u"仓库名称", max_length=255, unique=True
    )

    def __unicode__(self):
        return u"%s" % self.name

    class Meta:
        verbose_name_plural = verbose_name = u"仓库"


class SupplierCategory(BaseModel, UsableStatus):
    code = models.CharField(
            u"供应商分类编码", max_length=255, unique=True
    )
    name = models.CharField(
            u"供应商分类名称", max_length=255, unique=True
    )

    def __unicode__(self):
        return u"%s" % self.name

    class Meta:
        verbose_name_plural = verbose_name = u"供应商分类"


class Supplier(BaseModel, UsableStatus):
    suppliercategory = models.ManyToManyField(SupplierCategory,
                                              verbose_name=u'供应商分类')
    code = models.CharField(
            u"供应商编码", max_length=255, unique=True
    )
    name = models.CharField(
            u"供应商名称", max_length=255, unique=True
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
        verbose_name_plural = verbose_name = u"供应商"


class GoodsCategory(MPTTModel, BaseModel, UsableStatus):
    code = models.CharField(
            u"商品分类编码", max_length=255, unique=True
    )
    name = models.CharField(
            u"商品分类名称", max_length=255, unique=True
    )
    parent = TreeForeignKey(
            'self', verbose_name=u'上级分类',
            related_name='children', db_index=True,
            **DICT_NULL_BLANK_TRUE
    )

    def __unicode__(self):
        return u"%s" % self.name

    class Meta:
        verbose_name_plural = verbose_name = u"商品分类"

    class MPTTMeta:
        order_insertion_by = ['name']



class Goods(BaseModel, UsableStatus):
    code = models.CharField(
            u"商品编码", max_length=255, unique=True
    )
    name = models.CharField(
            u"商品名称", max_length=255, unique=True
    )
    units = models.ForeignKey(GoodsUnit, verbose_name=u'计量单位', on_delete=models.CASCADE)
    goodscategory = models.ManyToManyField(GoodsCategory, verbose_name=u'商品分类')
    specifications = models.CharField(
            u"规格型号", max_length=255, **DICT_NULL_BLANK_TRUE
    )
    barcode = models.CharField(
            u"条形码", max_length=255, **DICT_NULL_BLANK_TRUE
    )
    sailsmoney = models.DecimalField(
            u"销售价", decimal_places=2, max_digits=10, **DICT_NULL_BLANK_TRUE
    )
    suggesstBuysmoney = models.DecimalField(
            u"建议采购价", decimal_places=2, max_digits=10, **DICT_NULL_BLANK_TRUE
    )
    comments = models.CharField(
            u"备注", max_length=500, **DICT_NULL_BLANK_TRUE
    )

    def __unicode__(self):
        return u"%s" % self.name

    class Meta:
        verbose_name_plural = verbose_name = u"商品"

class GoodsWarehouse(BaseModel, UsableStatus):
    goods = models.ForeignKey(Goods, verbose_name=u'商品')
    warehouse = models.ForeignKey(Warehouse, verbose_name=u'仓库')
    safeNumber = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=u'安全库存')
    goodsNumber = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=u'商品库存')

    class Meta:
        verbose_name_plural = verbose_name = u"商品库存"