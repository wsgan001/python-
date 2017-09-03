# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 13:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tb', '0003_auto_20170902_2119'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='\u90ae\u7bb1'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tb.UserType', verbose_name='\u7c7b\u578b'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(max_length=32, verbose_name='\u7528\u6237'),
        ),
    ]
