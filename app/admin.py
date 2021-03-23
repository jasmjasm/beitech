from django.contrib import admin
from .models import *


class CustomerAdmin(admin.ModelAdmin):
    """
        Customer admin
    """
    list_display = ('customer_id', 'name', 'email',)
    list_display_links = ('name',)
    search_fields = ('name', 'email',)


class ProductAdmin(admin.ModelAdmin):
    """
        Product admin
    """
    list_display = ('product_id', 'name', 'description', 'price')
    list_display_links = ('name',)
    search_fields = ('name', 'description',)


class CustomerProductAdmin(admin.ModelAdmin):
    """
        Customer product admin
    """
    list_display = ('id', 'customer', 'product',)
    list_display_links = ('id',)
    search_fields = ('customer__name', 'product__name',)


class OrderDetailInLine(admin.TabularInline):
    model = OrderDetail
    fields = ('product', 'product_description', 'price', 'quantity',)


class OrderAdmin(admin.ModelAdmin):
    """
        Order admin
    """
    list_display = ('order_id', 'customer', 'creation_date',
                    'delivery_address', 'total',)
    list_display_links = ('order_id',)
    list_filter = ('customer',)
    search_fields = ('customer__name', 'delivery_address',)
    inlines = [
        OrderDetailInLine
    ]


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(CustomerProduct, CustomerProductAdmin)
admin.site.register(Order, OrderAdmin)
