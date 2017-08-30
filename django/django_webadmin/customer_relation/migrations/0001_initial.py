# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import common.constants
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u521b\u5efa\u65f6\u95f4')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='\u5ba2\u6237\u540d\u79f0')),
                ('address', models.CharField(max_length=500, null=True, verbose_name='\u5730\u5740', blank=True)),
                ('concat', models.CharField(max_length=255, null=True, verbose_name='\u8054\u7cfb\u4eba', blank=True)),
                ('mobile', models.CharField(max_length=255, null=True, verbose_name='\u624b\u673a', blank=True)),
                ('phone', models.CharField(max_length=255, null=True, verbose_name='\u56fa\u8bdd', blank=True)),
                ('qq', models.CharField(max_length=255, null=True, verbose_name='QQ', blank=True)),
                ('backconcat', models.CharField(max_length=255, null=True, verbose_name='\u5907\u4efd\u8054\u7cfb\u4eba', blank=True)),
                ('backmobile', models.CharField(max_length=255, null=True, verbose_name='\u5907\u4efd\u8054\u7cfb\u4eba\u624b\u673a', blank=True)),
                ('backphone', models.CharField(max_length=255, null=True, verbose_name='\u5907\u4efd\u8054\u7cfb\u4eba\u56fa\u8bdd', blank=True)),
                ('backqq', models.CharField(max_length=255, null=True, verbose_name='\u5907\u4efd\u8054\u7cfb\u4ebaQQ', blank=True)),
                ('goodaddr', models.CharField(max_length=255, null=True, verbose_name='\u53d1\u8d27\u5730\u5740', blank=True)),
                ('bankaddr', models.CharField(max_length=255, null=True, verbose_name='\u5f00\u6237\u884c', blank=True)),
                ('bankcode', models.CharField(max_length=255, null=True, verbose_name='\u5f00\u6237\u884c\u8d26\u53f7', blank=True)),
                ('taxcode', models.CharField(max_length=255, null=True, verbose_name='\u7a0e\u53f7', blank=True)),
                ('fax', models.CharField(max_length=255, null=True, verbose_name='\u4f20\u771f', blank=True)),
                ('shouldpaymoney', models.DecimalField(null=True, verbose_name='\u5e94\u4ed8\u671f\u521d\u4f59\u989d', max_digits=10, decimal_places=2, blank=True)),
                ('shouldpaymoneyDate', models.DateField(null=True, verbose_name='\u4f59\u989d\u65e5\u671f', blank=True)),
                ('comments', models.CharField(max_length=500, null=True, verbose_name='\u5907\u6ce8', blank=True)),
                ('creator', models.ForeignKey(verbose_name='\u6570\u636e\u521b\u5efa\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': '\u5ba2\u6237\u8d44\u6599',
                'verbose_name_plural': '\u5ba2\u6237\u8d44\u6599',
            },
            bases=(models.Model, common.constants.UsableStatus),
        ),
        migrations.CreateModel(
            name='CustomerCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u521b\u5efa\u65f6\u95f4')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='\u5ba2\u6237\u5206\u7c7b\u540d\u79f0')),
                ('creator', models.ForeignKey(verbose_name='\u6570\u636e\u521b\u5efa\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': '\u5ba2\u6237\u5206\u7c7b',
                'verbose_name_plural': '\u5ba2\u6237\u5206\u7c7b',
            },
            bases=(models.Model, common.constants.UsableStatus),
        ),
        migrations.AddField(
            model_name='customer',
            name='customerCategory',
            field=models.ForeignKey(verbose_name='\u5ba2\u6237\u5206\u7c7b', to='customer_relation.CustomerCategory'),
        ),
    ]
