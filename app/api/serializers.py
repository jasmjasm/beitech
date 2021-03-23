from rest_framework import serializers, permissions
from app.models import *


class OrderDetailSerializer(serializers.ModelSerializer):
    # Api publica para efectos de la prueba
    permission_classes = (permissions.AllowAny,)

    class Meta:
        model = OrderDetail
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    # Api publica para efectos de la prueba
    permission_classes = (permissions.AllowAny,)
    orderdetail = serializers.SerializerMethodField()

    def get_orderdetail(self, instance):
        return OrderDetailSerializer(instance.orderdetail_set.all(), many=True).data

    class Meta:
        model = Order
        fields = ('order_id', 'creation_date', 'date', 'customer',
                  'delivery_address', 'total', 'orderdetail')
