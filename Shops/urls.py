from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include(('ddq_user.urls', 'user'))),  # 用户模块
    path('cart/', include(('ddq_cart.urls', 'cart'))),  # 购物车模块
    path('order/', include(('ddq_order.urls', 'order'))),  # 订单模块
    path('', include(('ddq_goods.urls', 'goods'))),  # 商品模块（首页）
]