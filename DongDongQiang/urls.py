"""
URL configuration for DongDongQiang project.

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
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),    # ，二级路由。指引到admin.site.urls文件的url
    path('user/', include(('ddq_user.urls', 'user'))),  # 用户模块
    path('cart/', include(('ddq_cart.urls', 'cart'))),  # 购物车模块
    path('order/', include(('ddq_order.urls', 'order'))),  # 订单模块
    path('', include(('ddq_goods.urls', 'goods'))),  # 商品模块
    path('tinymce/', include('tinymce.urls')),
    path(r'search', include('haystack.urls')),  # 全文检索框架
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)