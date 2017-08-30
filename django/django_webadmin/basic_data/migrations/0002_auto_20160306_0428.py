# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import common.constants


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basic_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsWarehouse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u521b\u5efa\u65f6\u95f4')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True)),
                ('safeNumber', models.DecimalField(verbose_name='\u5b89\u5168\u5e93\u5b58', max_digits=8, decimal_places=2)),
                ('goodsNumber', models.DecimalField(verbose_name='\u5546\u54c1\u5e93\u5b58', max_digits=8, decimal_places=2)),
                ('creator', models.ForeignKey(verbose_name='\u6570\u636e\u521b\u5efa\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': '\u5546\u54c1\u5e93\u5b58',
                'verbose_name_plural': '\u5546\u54c1\u5e93\u5b58',
            },
            bases=(models.Model, common.constants.UsableStatus),
        ),
        migrations.RemoveField(
            model_name='goods',
            name='warehouse',
        ),
        migrations.AddField(
            model_name='goodswarehouse',
            name='goods',
            field=models.ForeignKey(verbose_name='\u5546\u54c1', to='basic_data.Goods'),
        ),
        migrations.AddField(
            model_name='goodswarehouse',
            name='warehouse',
            field=models.ForeignKey(verbose_name='\u4ed3\u5e93', to='basic_data.Warehouse'),
        ),
    ]
