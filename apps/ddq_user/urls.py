# coding:utf-8
# apps/ddq_user/urls.py
from django.urls import path, re_path
from .views import RegisterView,ActiveView,LoginView # 导入views模块

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),     # 注册页面
    # re_path(r"register_handle$", views.register_handle, name="register_handle"),  # 注册数据处理,考虑是否需要用正则表达式
    re_path(r"^active/(?P<token>.*)$", ActiveView.as_view(), name="active"),  # 账户激活
    re_path(r"^login$", LoginView.as_view(), name="login"),  # 登录
]


