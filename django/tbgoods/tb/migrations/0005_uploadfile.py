# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-05 07:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tb', '0004_auto_20170902_2155'),
    ]

    operations = [
        migrations.CreateModel(
            name='uploadfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='upload/%Y/%m/%d')),
            ],
        ),
    ]
