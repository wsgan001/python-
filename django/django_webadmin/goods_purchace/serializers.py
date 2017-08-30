from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from basic_data.models import Goods


class PurchaseOrderGoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ('code', 'units', 'sailsmoney', 'suggesstBuysmoney')
