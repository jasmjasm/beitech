from rest_framework import viewsets
from app.models import Order
from app.api.serializers import *


class OrderViewSet(viewsets.ModelViewSet):
    """
        Order viewset
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailViewSet(viewsets.ModelViewSet):
    """
        Order detail viewset
    """
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer
