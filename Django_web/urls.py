"""
URL configuration for Django_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

# urlpatterns = [                                # 双层路由
#     path("admin/", admin.site.urls),            # 看到"admin/"这个请求，就将请求转向admin.site.urls路由
#     path("user/", include("DjangoWebApps.user.urls", namespace='user')),        # 用户模块
#     # path("goods/", include("DjangoWebApps.dw_goods.urls", namespace='goods')),      # 商品模块
#     path("cart/", include("DjangoWebApps.cart.urls", namespace='cart')),        # 购物车模块
#     path("order/", include("DjangoWebApps.order.urls", namespace='order')),      # 订单模块
#     path("", include("DjangoWebApps.goods.urls", namespace='goods')),      # 商品模块
#
# ]
# Django_web/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # 用户模块 - 修改这里
    path("user/", include(("apps.user.urls", "user"), namespace="user")),
    # 其他模块保持不变
    path("cart/", include(("apps.cart.urls", "cart"), namespace="cart")),
    # path("goods/", include(("DjangoWebApps.goods.urls", "goods"), namespace="goods")),
    path("order/", include(("apps.order.urls", "order"), namespace="order")),
    path("goods/", include(("apps.goods.urls", "goods"), namespace="goods")),
    # 富文本编辑器
    path("tinymce/", include(("tinymce.urls", "tinymce"))),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
