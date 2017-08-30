# coding=utf-8
from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from basic_data.models import GoodsUnit, Warehouse, SupplierCategory, Supplier, GoodsCategory, Goods, GoodsWarehouse


@admin.register(GoodsUnit)
class GoodsUnitAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    exclude = ['creator', 'created_at', 'updated_at', 'deleted_at']


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['code', 'name']
    search_fields = ['code', 'name']
    exclude = ['creator', 'created_at', 'updated_at', 'deleted_at']


@admin.register(SupplierCategory)
class SupplierCategoryAdmin(admin.ModelAdmin):
    list_display = ['code', 'name']
    search_fields = ['code', 'name']
    exclude = ['creator', 'created_at', 'updated_at', 'deleted_at']


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'address',
                    'concat', 'mobile', 'shouldpaymoney',
                    'shouldpaymoneyDate']
    search_fields = ['code', 'name']
    exclude = ['creator', 'created_at', 'updated_at', 'deleted_at']


@admin.register(GoodsCategory)
class GoodsCategoryAdmin(MPTTModelAdmin):
    list_display = ['code', 'name', 'get_parent']
    search_fields = ['code', 'name']
    exclude = ['creator', 'created_at', 'updated_at', 'deleted_at']

    def get_parent(self, obj):
        return obj.parent.name if obj.parent else '-'

    get_parent.short_description = u'上级类别'
    get_parent.admin_order_field = 'parent'


class GoodsInline(admin.TabularInline):
    model = GoodsWarehouse
    exclude = ['creator', 'created_at', 'updated_at', 'deleted_at']
    extra = 0


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'units',
                    'specifications', 'sailsmoney', 'suggesstBuysmoney']
    search_fields = ['code', 'name']
    exclude = ['creator', 'created_at', 'updated_at', 'deleted_at']
    inlines = [GoodsInline]
