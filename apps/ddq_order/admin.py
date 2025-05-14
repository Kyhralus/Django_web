from django.contrib import admin
from apps.ddq_order.models import OrderInfo, OrderGoods


admin.site.register(OrderInfo)

admin.site.register(OrderGoods)
