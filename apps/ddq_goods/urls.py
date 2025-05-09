# coding:utf-8
from django.urls import path,re_path
from .views import IndexView, DetailView

urlpatterns = [
    # re_path(r"^$", views.index, name="index"), # 首页
    re_path(r"^$", IndexView.as_view(), name="index"),
    re_path(r"^goods/(?P<goods_id>\d+)$", DetailView.as_view(), name="detail"),  # 详情页
]

