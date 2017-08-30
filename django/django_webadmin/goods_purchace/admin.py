# coding=utf-8
from django.contrib import admin
from django.contrib.admin.forms import forms

from basic_data.models import Goods, GoodsUnit
from goods_purchace.models import PurchaseOrder, PurchaseOrderGoods, StorageOrder, StorageOrderGoods


class PurchaseOrderGoodsInline(admin.TabularInline):
    model = PurchaseOrderGoods
    fields = ['goods', 'sailsmoney',
              'suggesstBuysmoney', 'purchaseNumber',
              'buysmoney', 'purchaseTotal']
    readonly_fields = ['sailsmoney',
                       'suggesstBuysmoney',
                       'purchaseTotal']
    exclude = ['creator', 'created_at', 'updated_at', 'deleted_at']
    extra = 0
    verbose_name = "订单明细"
    verbose_name_plural = "订单明细"

    class Media:
        js = ('/static/js/PurchaseOrderGoodsInline.js',)


@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ['code', 'address',
                    'concat', 'mobile', 'fax', 'orderstatus']
    readonly_fields = ['orderstatus']
    search_fields = ['code']
    exclude = ['creator', 'created_at', 'updated_at', 'deleted_at']
    inlines = [PurchaseOrderGoodsInline]
    list_filter = ['orderstatus']

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        i = 0

        for instance in instances:
            goodsid = instance.goods_id
            buysmoney = instance.buysmoney
            purchaseNumber = instance.purchaseNumber

            goods = Goods.objects.get(id=goodsid)
            instance.goods = goods
            instance.code = goods.code
            instance.name = goods.name
            instance.units = goods.units.name
            instance.goodscategory = goods.goodscategory
            instance.specifications = goods.specifications
            instance.barcode = goods.barcode
            instance.sailsmoney = goods.sailsmoney
            instance.suggesstBuysmoney = goods.suggesstBuysmoney
            instance.comments = goods.comments
            instance.purchaseTotal = instance.purchaseNumber * instance.buysmoney
            instance.buysmoney = buysmoney
            instance.purchaseNumber = purchaseNumber
            instance.save()
            i += 1

        formset.save_m2m()


class StorageOrderGoodsInline(admin.TabularInline):
    model = StorageOrderGoods
    fields = ['code','goods', 'sailsmoney',
              'suggesstBuysmoney', 'purchaseNumber',
              'buysmoney', 'purchaseTotal', 'warehouse']
    readonly_fields = ['code','sailsmoney',
                       'suggesstBuysmoney', 'goods', 'purchaseNumber', 'buysmoney',
                       'purchaseTotal']
    exclude = ['creator', 'created_at', 'updated_at', 'deleted_at']
    extra = 0
    verbose_name = "入库订单明细"
    verbose_name_plural = "入库订单明细"

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    class Media:
        js = ('/static/js/StorageOrderGoodsInline.js',)


@admin.register(StorageOrder)
class StorageOrderAdmin(admin.ModelAdmin):
    list_display = ['code', 'address',
                    'concat', 'mobile', 'fax', 'orderstatus']
    search_fields = ['code']
    readonly_fields = ['code', 'address',
                       'concat', 'mobile', 'fax', 'orderstatus', 'purchadate', 'payway']
    exclude = ['creator', 'created_at', 'updated_at', 'deleted_at', 'orderstatus']
    inlines = [StorageOrderGoodsInline]
    list_filter = ['orderstatus']

    def has_add_permission(self, request):
        return False

    def has_edit_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
