# coding:utf-8
# apps/ddq_user/urls.py
from django.urls import path, re_path
from . import views # 导入views模块

urlpatterns = [
    path("register/", views.register, name="register"),     # 注册页面
    re_path(r"register_handle$", views.register_handle, name="register_handle"),  # 注册数据处理,考虑是否需要用正则表达式

]

