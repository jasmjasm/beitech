from rest_framework import serializers, permissions
from app.models import *
from app.renderer import JSONResponseRenderer


class OrderDetailSerializer(serializers.ModelSerializer):
    """
        Order detail serializaer
    """
    # Api publica para efectos de la prueba
    permission_classes = (permissions.AllowAny,)

    class Meta:
        model = OrderDetail
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    """
        Order serializer
    """
    # Api publica para efectos de la prueba
    permission_classes = (permissions.AllowAny,)
    # Metodo custom para obtener el detalle orderdetail asociado a la orden
    orderdetail = serializers.SerializerMethodField()
    # Campo custom que nos permite insertar el orderdetail al momento de crear la orden, con sus respectivas validaciones
    order_detail = serializers.JSONField(write_only=True, required=False)
    customername = serializers.SerializerMethodField()
    products = serializers.SerializerMethodField()

    def create(self, validated_data):
        error = None
        order_detail = validated_data.pop('order_detail', None)
        # Validaciones para el order_detail recibido
        if order_detail:
            for detail in order_detail:
                product_id = detail.get('product', None)
                if not product_id:
                    error = 'No se ha definido un product_id en un item de order_detail'
                    break
                exists = CustomerProduct.objects.filter(
                    customer=validated_data['customer'], product=product_id).exists()
                if not exists:
                    error = 'No existe un product_id ({}) asociado al cliente seleccionado'.format(
                        product_id)
                    break
            if len(order_detail) > 5:
                error = 'No se permiten insertar mas de 5 productos por orden'
        if error:
            raise serializers.ValidationError({"detail": error})
        # Se crea y valida datos recibidos de order
        instance = super(OrderSerializer, self).create(validated_data)
        # Se procede a crear el orderdetail para la orden creada anteriormente
        if order_detail:
            products_list = []
            total = 0
            for detail in order_detail:
                customer_product = CustomerProduct.objects.filter(
                    customer=validated_data['customer'], product=detail['product']).first()
                d = OrderDetail()
                d.order = instance
                # Se asigna el nombre del producto en la product_description de OrderDetail si este no se recibe
                if not 'product_description' in detail:
                    d.product_description = customer_product.product.name
                else:
                    d.product_description = detail['product_description']
                d.quantity = detail['quantity']
                # Se tome el precio del precio definido el CustomerProduct
                d.price = customer_product.price
                total += d.quantity * d.price
                d.product = customer_product.product
                products_list.append(d)
            # Se inserta todo el detalle de una sola vez por temas de optimizacion
            OrderDetail.objects.bulk_create(products_list)
        # Se actualiza el total de la orden basado el en calculo del order detail
        instance.total = total
        # Se actualiza solo el campo total por temas de optimizacion
        instance.save(update_fields=['total'])
        # Se retorna la instancia con toda la informacion
        return instance

    def get_orderdetail(self, instance):
        return OrderDetailSerializer(instance.orderdetail_set.all(), many=True).data

    def get_customername(self, instance):
        return instance.customer.name

    def get_products(self, instance):
        products = ''
        for d in instance.orderdetail_set.all():
            products += "{} x {}</br>".format(d.quantity,
                                              d.product_description)
        return products

    class Meta:
        model = Order
        fields = ('order_id', 'creation_date', 'date', 'customer', 'customername',
                  'delivery_address', 'total', 'orderdetail', 'order_detail', 'products')
