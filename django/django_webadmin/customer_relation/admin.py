from django.contrib import admin

# Register your models here.
from customer_relation.models import CustomerCategory, Customer


@admin.register(CustomerCategory)
class CustomerCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    exclude = ['creator', 'created_at', 'updated_at', 'deleted_at']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'customerCategory', 'address',
                    'concat', 'mobile', 'shouldpaymoney',
                    'shouldpaymoneyDate']
    search_fields = ['name']
    exclude = ['creator', 'created_at', 'updated_at', 'deleted_at']
