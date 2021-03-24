from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from app.models import Order
from app.api.serializers import *


class OrderViewSet(viewsets.ModelViewSet):
    """
        Order viewset
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filterset_fields = {
        'date':  ['range'],
        'customer': ['exact']
    }


class CustomOrderViewSet(OrderViewSet):
    """
        Custom order viewset
    """
    renderer_classes = [JSONResponseRenderer]


class OrderDetailViewSet(viewsets.ModelViewSet):
    """
        Order detail viewset
    """
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer
