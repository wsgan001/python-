# coding=utf-8
from django.contrib.auth.models import User, Group, AbstractBaseUser, \
    AbstractUser
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from basic_data.models import Goods, Warehouse
from common.constants import UsableStatus, DICT_NULL_BLANK_TRUE, TRUE_FALSE, PAYWAY, GOODS_ORDER_STATUS, \
    GOODS_STORAGE_STATUS
from common.models import BaseModel


class PurchaseOrder(BaseModel, UsableStatus):
    code = models.CharField(
            u"单号", max_length=255, unique=True
    )
    purchadate = models.DateField(
            u"采购日期"
    )
    address = models.CharField(
            u"交货地址", max_length=255, **DICT_NULL_BLANK_TRUE
    )
    concat = models.CharField(
            u"联系人", max_length=255, **DICT_NULL_BLANK_TRUE
    )
    mobile = models.CharField(
            u"电话", max_length=255, **DICT_NULL_BLANK_TRUE
    )
    fax = models.CharField(
            u"传真", max_length=255, **DICT_NULL_BLANK_TRUE
    )
    # purchaceUser = models.ForeignKey(User, verbose_name=u'业务员')
    payway = models.IntegerField(choices=PAYWAY, verbose_name=u'付款方式')
    orderstatus = models.IntegerField(choices=GOODS_ORDER_STATUS, verbose_name=u'订单状态', default=0)

    def __unicode__(self):
        return u"%s" % self.code

    class Meta:
        verbose_name_plural = verbose_name = u"采购订单"


class PurchaseOrderGoods(BaseModel, UsableStatus):
    goods = models.ForeignKey(Goods, verbose_name=u'采购商品', )
    code = models.CharField(
            u"商品编码", max_length=255, default=u""
    )
    name = models.CharField(
            u"商品名称", max_length=255, default=u""
    )
    units = models.CharField(max_length=255, verbose_name=u'计量单位', default=u"")
    goodscategory = models.CharField(max_length=255, verbose_name=u'商品分类', default=u"")
    specifications = models.CharField(
            u"规格型号", max_length=255, default=u""
    )
    barcode = models.CharField(
            u"条形码", max_length=255, default=u""
    )
    sailsmoney = models.DecimalField(
            u"销售价", decimal_places=2, max_digits=10, default=0
    )
    suggesstBuysmoney = models.DecimalField(
            u"建议采购价", decimal_places=2, max_digits=10, default=0
    )
    buysmoney = models.DecimalField(
            u"采购价", decimal_places=2, max_digits=10, default=0
    )
    comments = models.CharField(
            u"备注", max_length=500, default=u""
    )
    purchaseNumber = models.IntegerField(verbose_name=u'采购数量', default=0)
    purchaseTotal = models.DecimalField(verbose_name=u'采购金额', max_digits=10, decimal_places=2,
                                        default=0)
    purchaseOrder = models.ForeignKey(PurchaseOrder, verbose_name=u'采购单')

    class Meta:
        verbose_name_plural = verbose_name = u"采购订单详情"


class StorageOrder(BaseModel, UsableStatus):
    code = models.CharField(
            u"单号", max_length=255, unique=True
    )
    purchadate = models.DateField(
            u"采购日期"
    )
    address = models.CharField(
            u"交货地址", max_length=255, **DICT_NULL_BLANK_TRUE
    )
    concat = models.CharField(
            u"联系人", max_length=255, **DICT_NULL_BLANK_TRUE
    )
    mobile = models.CharField(
            u"电话", max_length=255, **DICT_NULL_BLANK_TRUE
    )
    fax = models.CharField(
            u"传真", max_length=255, **DICT_NULL_BLANK_TRUE
    )
    # purchaceUser = models.ForeignKey(User, verbose_name=u'业务员')
    payway = models.IntegerField(choices=PAYWAY, verbose_name=u'付款方式')
    orderstatus = models.IntegerField(choices=GOODS_STORAGE_STATUS, verbose_name=u'入库状态', default=0)

    def __unicode__(self):
        return u"%s" % self.code

    class Meta:
        verbose_name_plural = verbose_name = u"采购入库"


class StorageOrderGoods(BaseModel, UsableStatus):
    warehouse = models.ForeignKey(Warehouse, verbose_name=u'库房', **DICT_NULL_BLANK_TRUE)
    goods = models.ForeignKey(Goods, verbose_name=u'采购商品', )
    code = models.CharField(
            u"商品编码", max_length=255, default=u""
    )
    name = models.CharField(
            u"商品名称", max_length=255, default=u""
    )
    units = models.CharField(max_length=255, verbose_name=u'计量单位', default=u"")
    goodscategory = models.CharField(max_length=255, verbose_name=u'商品分类', default=u"")
    specifications = models.CharField(
            u"规格型号", max_length=255, default=u""
    )
    barcode = models.CharField(
            u"条形码", max_length=255, default=u""
    )
    sailsmoney = models.DecimalField(
            u"销售价", decimal_places=2, max_digits=10, default=0
    )
    suggesstBuysmoney = models.DecimalField(
            u"建议采购价", decimal_places=2, max_digits=10, default=0
    )
    buysmoney = models.DecimalField(
            u"采购价", decimal_places=2, max_digits=10, default=0
    )
    comments = models.CharField(
            u"备注", max_length=500, default=u""
    )
    purchaseNumber = models.IntegerField(verbose_name=u'采购数量', default=0)
    purchaseTotal = models.DecimalField(verbose_name=u'采购金额', max_digits=10, decimal_places=2,
                                        default=0)
    purchaseOrder = models.ForeignKey(StorageOrder, verbose_name=u'入库单')

    class Meta:
        verbose_name_plural = verbose_name = u"采购入库详情"
