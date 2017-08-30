# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import common.constants
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('basic_data', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u521b\u5efa\u65f6\u95f4')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True)),
                ('code', models.CharField(unique=True, max_length=255, verbose_name='\u5355\u53f7')),
                ('purchadate', models.DateField(verbose_name='\u91c7\u8d2d\u65e5\u671f')),
                ('address', models.CharField(max_length=255, null=True, verbose_name='\u4ea4\u8d27\u5730\u5740', blank=True)),
                ('concat', models.CharField(max_length=255, null=True, verbose_name='\u8054\u7cfb\u4eba', blank=True)),
                ('mobile', models.CharField(max_length=255, null=True, verbose_name='\u7535\u8bdd', blank=True)),
                ('fax', models.CharField(max_length=255, null=True, verbose_name='\u4f20\u771f', blank=True)),
                ('payway', models.IntegerField(verbose_name='\u4ed8\u6b3e\u65b9\u5f0f', choices=[(0, '\u8bb0\u5e94\u4ed8\u5e10\u6b3e'), (1, '\u73b0\u91d1\u4ed8\u6b3e'), (2, '\u9884\u4ed8\u6b3e')])),
                ('orderstatus', models.IntegerField(default=0, verbose_name='\u8ba2\u5355\u72b6\u6001', choices=[(0, '\u5f85\u5ba1\u6838'), (1, '\u5ba1\u6838\u901a\u8fc7')])),
                ('creator', models.ForeignKey(verbose_name='\u6570\u636e\u521b\u5efa\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': '\u91c7\u8d2d\u8ba2\u5355',
                'verbose_name_plural': '\u91c7\u8d2d\u8ba2\u5355',
            },
            bases=(models.Model, common.constants.UsableStatus),
        ),
        migrations.CreateModel(
            name='PurchaseOrderGoods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u521b\u5efa\u65f6\u95f4')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True)),
                ('code', models.CharField(default='', max_length=255, verbose_name='\u5546\u54c1\u7f16\u7801')),
                ('name', models.CharField(default='', max_length=255, verbose_name='\u5546\u54c1\u540d\u79f0')),
                ('units', models.CharField(default='', max_length=255, verbose_name='\u8ba1\u91cf\u5355\u4f4d')),
                ('goodscategory', models.CharField(default='', max_length=255, verbose_name='\u5546\u54c1\u5206\u7c7b')),
                ('specifications', models.CharField(default='', max_length=255, verbose_name='\u89c4\u683c\u578b\u53f7')),
                ('barcode', models.CharField(default='', max_length=255, verbose_name='\u6761\u5f62\u7801')),
                ('sailsmoney', models.DecimalField(default=0, verbose_name='\u9500\u552e\u4ef7', max_digits=10, decimal_places=2)),
                ('suggesstBuysmoney', models.DecimalField(default=0, verbose_name='\u5efa\u8bae\u91c7\u8d2d\u4ef7', max_digits=10, decimal_places=2)),
                ('buysmoney', models.DecimalField(default=0, verbose_name='\u91c7\u8d2d\u4ef7', max_digits=10, decimal_places=2)),
                ('comments', models.CharField(default='', max_length=500, verbose_name='\u5907\u6ce8')),
                ('purchaseNumber', models.IntegerField(default=0, verbose_name='\u91c7\u8d2d\u6570\u91cf')),
                ('purchaseTotal', models.DecimalField(default=0, verbose_name='\u91c7\u8d2d\u91d1\u989d', max_digits=10, decimal_places=2)),
                ('creator', models.ForeignKey(verbose_name='\u6570\u636e\u521b\u5efa\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('goods', models.ForeignKey(verbose_name='\u91c7\u8d2d\u5546\u54c1', to='basic_data.Goods')),
                ('purchaseOrder', models.ForeignKey(verbose_name='\u91c7\u8d2d\u5355', to='goods_purchace.PurchaseOrder')),
            ],
            options={
                'verbose_name': '\u91c7\u8d2d\u8ba2\u5355\u8be6\u60c5',
                'verbose_name_plural': '\u91c7\u8d2d\u8ba2\u5355\u8be6\u60c5',
            },
            bases=(models.Model, common.constants.UsableStatus),
        ),
        migrations.CreateModel(
            name='StorageOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u521b\u5efa\u65f6\u95f4')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True)),
                ('code', models.CharField(unique=True, max_length=255, verbose_name='\u5355\u53f7')),
                ('purchadate', models.DateField(verbose_name='\u91c7\u8d2d\u65e5\u671f')),
                ('address', models.CharField(max_length=255, null=True, verbose_name='\u4ea4\u8d27\u5730\u5740', blank=True)),
                ('concat', models.CharField(max_length=255, null=True, verbose_name='\u8054\u7cfb\u4eba', blank=True)),
                ('mobile', models.CharField(max_length=255, null=True, verbose_name='\u7535\u8bdd', blank=True)),
                ('fax', models.CharField(max_length=255, null=True, verbose_name='\u4f20\u771f', blank=True)),
                ('payway', models.IntegerField(verbose_name='\u4ed8\u6b3e\u65b9\u5f0f', choices=[(0, '\u8bb0\u5e94\u4ed8\u5e10\u6b3e'), (1, '\u73b0\u91d1\u4ed8\u6b3e'), (2, '\u9884\u4ed8\u6b3e')])),
                ('orderstatus', models.IntegerField(default=0, verbose_name='\u5165\u5e93\u72b6\u6001', choices=[(0, '\u5f85\u5165\u5e93'), (1, '\u5df2\u5165\u5e93')])),
                ('creator', models.ForeignKey(verbose_name='\u6570\u636e\u521b\u5efa\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': '\u91c7\u8d2d\u5165\u5e93',
                'verbose_name_plural': '\u91c7\u8d2d\u5165\u5e93',
            },
            bases=(models.Model, common.constants.UsableStatus),
        ),
        migrations.CreateModel(
            name='StorageOrderGoods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u521b\u5efa\u65f6\u95f4')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True)),
                ('code', models.CharField(default='', max_length=255, verbose_name='\u5546\u54c1\u7f16\u7801')),
                ('name', models.CharField(default='', max_length=255, verbose_name='\u5546\u54c1\u540d\u79f0')),
                ('units', models.CharField(default='', max_length=255, verbose_name='\u8ba1\u91cf\u5355\u4f4d')),
                ('goodscategory', models.CharField(default='', max_length=255, verbose_name='\u5546\u54c1\u5206\u7c7b')),
                ('specifications', models.CharField(default='', max_length=255, verbose_name='\u89c4\u683c\u578b\u53f7')),
                ('barcode', models.CharField(default='', max_length=255, verbose_name='\u6761\u5f62\u7801')),
                ('sailsmoney', models.DecimalField(default=0, verbose_name='\u9500\u552e\u4ef7', max_digits=10, decimal_places=2)),
                ('suggesstBuysmoney', models.DecimalField(default=0, verbose_name='\u5efa\u8bae\u91c7\u8d2d\u4ef7', max_digits=10, decimal_places=2)),
                ('buysmoney', models.DecimalField(default=0, verbose_name='\u91c7\u8d2d\u4ef7', max_digits=10, decimal_places=2)),
                ('comments', models.CharField(default='', max_length=500, verbose_name='\u5907\u6ce8')),
                ('purchaseNumber', models.IntegerField(default=0, verbose_name='\u91c7\u8d2d\u6570\u91cf')),
                ('purchaseTotal', models.DecimalField(default=0, verbose_name='\u91c7\u8d2d\u91d1\u989d', max_digits=10, decimal_places=2)),
                ('creator', models.ForeignKey(verbose_name='\u6570\u636e\u521b\u5efa\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('goods', models.ForeignKey(verbose_name='\u91c7\u8d2d\u5546\u54c1', to='basic_data.Goods')),
                ('purchaseOrder', models.ForeignKey(verbose_name='\u5165\u5e93\u5355', to='goods_purchace.StorageOrder')),
                ('warehouse', models.ForeignKey(verbose_name='\u5e93\u623f', blank=True, to='basic_data.Warehouse', null=True)),
            ],
            options={
                'verbose_name': '\u91c7\u8d2d\u5165\u5e93\u8be6\u60c5',
                'verbose_name_plural': '\u91c7\u8d2d\u5165\u5e93\u8be6\u60c5',
            },
            bases=(models.Model, common.constants.UsableStatus),
        ),
    ]
