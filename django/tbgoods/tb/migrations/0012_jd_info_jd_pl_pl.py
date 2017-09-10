# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-09 05:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tb', '0011_auto_20170907_0915'),
    ]

    operations = [
        migrations.CreateModel(
            name='jd_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=200)),
                ('ids', models.CharField(max_length=200)),
                ('store', models.CharField(max_length=200)),
                ('titles', models.CharField(max_length=500)),
                ('price', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='jd_pl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ids', models.CharField(max_length=200)),
                ('selas', models.CharField(max_length=200)),
                ('user', models.CharField(max_length=200)),
                ('titles', models.CharField(max_length=500)),
                ('sku', models.CharField(max_length=500)),
                ('date', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='pl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemid', models.CharField(max_length=200)),
                ('user', models.CharField(max_length=50)),
                ('sku', models.CharField(max_length=500)),
                ('date', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=5000)),
            ],
        ),
    ]
