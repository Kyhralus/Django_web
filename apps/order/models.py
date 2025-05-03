# # order/models.py
# from django.db import models
# from django.conf import settings
# from DjangoWebApps.goods.models import Product
#
# class Order(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField()
#     address = models.TextField()
#     postal_code = models.CharField(max_length=20)
#     city = models.CharField(max_length=100)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     paid = models.BooleanField(default=False)
#
#     class Meta:
#         ordering = ['-created']
#
#     def __str__(self):
#         return f'Order {self.id}'
#
#     def get_total_cost(self):
#         return sum(item.get_cost() for item in self.items.all())
#
# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     quantity = models.IntegerField(default=1)
#
#     def __str__(self):
#         return str(self.id)
#
#     def get_cost(self):
#         return self.price * self.quantity

# -*- coding: utf-8 -*-
from django.db import models
from db.base_model import BaseModel
# Create your models here.


class OrderInfo(BaseModel):
    '''订单模型类'''
    PAY_METHOD_CHOICES = (
        (1, '货到付款'),
        (2, '微信支付'),
        (3, '支付宝'),
        (4, '银联支付')
    )

    ORDER_STATUS_CHOICES = (
        (1, '待支付'),
        (2, '待发货'),
        (3, '待收货'),
        (4, '待评价'),
        (5, '已完成')
    )

    order_id = models.CharField(max_length=128, primary_key=True, verbose_name='订单id')
    user = models.ForeignKey('user.User', verbose_name='用户', on_delete=models.CASCADE)
    addr = models.ForeignKey('user.Address', verbose_name='地址', on_delete=models.CASCADE)
    pay_method = models.SmallIntegerField(choices=PAY_METHOD_CHOICES, default=3, verbose_name='支付方式')
    total_count = models.IntegerField(default=1, verbose_name='商品数量')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='商品总价')
    transit_price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='订单运费')
    order_status = models.SmallIntegerField(choices=ORDER_STATUS_CHOICES, default=1, verbose_name='订单状态')
    trade_no = models.CharField(max_length=128, verbose_name='支付编号')

    class Meta:
        db_table = 'order_info'
        verbose_name = '订单'
        verbose_name_plural = verbose_name


class OrderGoods(BaseModel):
    '''订单商品模型类'''
    order = models.ForeignKey('OrderInfo', verbose_name='订单', on_delete=models.CASCADE)
    sku = models.ForeignKey('goods.GoodsSKU', verbose_name='商品SKU', on_delete=models.CASCADE)
    count = models.IntegerField(default=1, verbose_name='商品数目')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='商品价格')
    comment = models.CharField(max_length=256, verbose_name='评论')

    class Meta:
        db_table = 'order_goods'
        verbose_name = '订单商品'
        verbose_name_plural = verbose_name