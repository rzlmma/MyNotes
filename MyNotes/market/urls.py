# -*- coding:utf-8 -*-
# Copyright (c) 2016 MagicStack 

from django.conf.urls import url
from .views import MarketListView


urlpatterns = [
    url(r'offline/order/list/$', MarketListView.as_view(), name='offline_market'),
]