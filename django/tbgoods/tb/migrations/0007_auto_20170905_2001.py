# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 12:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tb', '0006_auto_20170905_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='file',
            field=models.FileField(upload_to=b''),
        ),
    ]
