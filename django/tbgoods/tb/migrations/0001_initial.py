# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 02:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=200)),
                ('itemId', models.CharField(max_length=50)),
                ('titles', models.CharField(max_length=500)),
                ('price', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=500)),
                ('pi_url', models.CharField(max_length=500)),
            ],
        ),
    ]
