# -*- coding:utf-8 -*-
"""
定义线下实体店的购买清单
"""
from django.db import models


class Fruits(models.Model):
    name = models.CharField(max_length=100, help_text=u"水果的名字")
    number = models.IntegerField(null=True, blank=True, help_text=u"水果的件数")
    price = models.FloatField(null=True, blank=True, help_text=u"水果的单价")
    total = models.FloatField(null=True, blank=True, help_text=u"水果的总价")
    market = models.ForeignKey(OffLineMarket, help_text=u"购买水果的超市")


class OffLineMarket(models.Model):
    """
    超市小票
    """
    name = models.CharField(max_length=200, help_text=u"超市的名字")
    order_time = models.DateTimeField(null=True, blank=True, help_text=u"超市小票生成的时间")
    address = models.CharField(max_length=200, blank=True, null=True, help_text=u"超市所在的位置")
    create_time = models.DateTimeField(auto_now_add=True, help_text=u"订单记录创建的时间")
    modify_time = models.DateTimeField(auto_now=True, help_text=u"订单记录修改时间")
    delete_time = models.DateTimeField(auto_now=True, help_text=u"订单记录删除的时间")

    class Meta:
        ordering = ["-create_time"]