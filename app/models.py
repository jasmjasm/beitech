from django.db import models


class Customer(models.Model):
    """
        Customer model
    """
    customer_id = models.AutoField(verbose_name='Id', primary_key=True)
    name = models.CharField(verbose_name='Name', max_length=191)
    email = models.EmailField(verbose_name='Email',
                              max_length=191, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'customers'


class Product(models.Model):
    """
        Product model
    """
    product_id = models.AutoField(verbose_name='Id', primary_key=True)
    name = models.CharField(verbose_name='Name', max_length=191)
    description = models.CharField(verbose_name='Description', max_length=191)
    price = models.DecimalField(
        verbose_name='Price', max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'products'


class CustomerProduct(models.Model):
    """
        Customer products model
    """
    customer = models.ForeignKey(
        Customer, verbose_name='Customer', on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, verbose_name='Product', on_delete=models.CASCADE)

    def __str__(self):
        return "{} | {}".format(self.customer, self.product)

    class Meta:
        verbose_name = 'customer product'
        verbose_name_plural = 'customer products'
        unique_together = (('customer', 'product',),)


class Order(models.Model):
    """
        Order model
    """
    order_id = models.AutoField(verbose_name='Id', primary_key=True)
    customer = models.ForeignKey(
        Customer, verbose_name='Customer', on_delete=models.CASCADE)
    creation_date = models.DateField(auto_now_add=True)
    delivery_address = models.CharField(
        verbose_name='Delivery address', max_length=191)
    total = models.DecimalField(
        verbose_name='Total', max_digits=14, decimal_places=2)

    def __str__(self):
        return "{} | {}".format(self.order_id, self.customer)

    class Meta:
        verbose_name_plural = 'orders'


class OrderDetail(models.Model):
    """
        Order detail model
    """
    order_detail_id = models.AutoField(verbose_name='Id', primary_key=True)
    order = models.ForeignKey(
        Order, verbose_name='Order', on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, verbose_name='Product', on_delete=models.CASCADE)
    product_description = models.CharField(
        verbose_name='Product description', max_length=191)
    price = models.DecimalField(
        verbose_name='Price', max_digits=10, decimal_places=2)
    quantity = models.BigIntegerField(verbose_name='Quantity')

    def __str__(self):
        return "{} | {} | {}".format(self.order_detail_id, self.order, self.product)

    class Meta:
        verbose_name = 'product detail'
        verbose_name_plural = 'product details'
