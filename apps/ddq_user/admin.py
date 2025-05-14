from django.contrib import admin
from apps.ddq_user.models import User, Address, Balance

# 注册商品类型模型类
admin.site.register(User)
admin.site.register(Address)
# admin.site.register(AddressManager)
admin.site.register(Balance)
# Register your models here.
