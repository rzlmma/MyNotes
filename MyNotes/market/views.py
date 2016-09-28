from django.views.generic.list import ListView
from .models import OffLineMarket


class MarketListView(ListView):
    model = OffLineMarket

