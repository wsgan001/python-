from decimal import Decimal
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from basic_data.models import Goods, GoodsWarehouse, Warehouse
from goods_purchace.models import PurchaseOrder, StorageOrder, StorageOrderGoods, PurchaseOrderGoods
from goods_purchace.serializers import PurchaseOrderGoodsSerializer
from rest_framework import generics
import simplejson as json


class PurchaseOrderGoodsDetailViewSet(viewsets.ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = PurchaseOrderGoodsSerializer


@csrf_exempt
def ApproveStorageOrder(request, code, status):
    try:
        entity = StorageOrder.objects.get(code=code)
        if status == u'0':
            purchaseOrder = PurchaseOrder.objects.get(code=code)
            purchaseOrder.orderstatus = 0
            entity.delete()

        if status == u'1':
            entity.orderstatus = 1
            entity.save()

            jsonEntities = json.loads(request.POST.get('data'))
            for i in range(len(jsonEntities) - 1):
                goods = Goods.objects.get(code=jsonEntities[i].get('code'))
                goodsWarehouseEntity = GoodsWarehouse.objects.filter(goods=goods.id,
                                                                     warehouse=jsonEntities[i].get('warehouse')).get()

                storage = StorageOrderGoods.objects.get(code=jsonEntities[i].get('code'),
                                                        purchaseOrder=StorageOrder.objects.get(code=code).id)
                warehouse = Warehouse.objects.get(id=jsonEntities[i].get('warehouse'))
                storage.warehouse = warehouse
                storage.save()

                goodsWarehouseEntity.goodsNumber += Decimal(jsonEntities[i].get('purchaseNumber'))
                goodsWarehouseEntity.save()

        return HttpResponse("")
    except Exception as e:
        print e


def ApprovePurchageOrder(request, code, status):
    entity = PurchaseOrder.objects.select_related().get(code=code)
    entity.orderstatus = status
    entity.save()

    if status == u'1':
        storageOrder = StorageOrder.objects.create(
                code=entity.code,
                purchadate=entity.purchadate,
                address=entity.address,
                concat=entity.concat,
                mobile=entity.mobile,
                fax=entity.fax,
                payway=entity.payway,
                orderstatus=0
        )

        goodOrders = PurchaseOrderGoods.objects.filter(purchaseOrder=entity.id).all()
        for obj in goodOrders:
            StorageOrderGoods.objects.create(
                    goods=obj.goods,
                    code=obj.code,
                    name=obj.name,
                    units=obj.units,
                    goodscategory=obj.goodscategory,
                    specifications=obj.specifications,
                    barcode=obj.barcode,
                    sailsmoney=obj.sailsmoney,
                    suggesstBuysmoney=obj.suggesstBuysmoney,
                    buysmoney=obj.buysmoney,
                    comments=obj.comments,
                    purchaseNumber=obj.purchaseNumber,
                    purchaseTotal=obj.purchaseTotal,
                    purchaseOrder=storageOrder
            )

    if status == u'0':
        StorageOrder.objects.get(code=code).delete()

    return HttpResponse("")
