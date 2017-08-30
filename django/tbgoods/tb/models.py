# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class info(models.Model):
     s_name = models.CharField(max_length=200)
     ids = models.CharField(max_length=50)
     titles = models.CharField(max_length=500)
     price= models.CharField(max_length=200)
     selas=models.CharField(max_length=200)
     url = models.CharField(max_length=500)
     pi_url = models.CharField(max_length=500)
