# coding:utf-8
from django.urls import path,re_path
from .views import IndexView, DetailView, ListView

urlpatterns = [
    path('index', IndexView.as_view(), name='index'), # 首页
    re_path(r'^goods/(?P<goods_id>\d+)$', DetailView.as_view(), name='detail'), # 详情页
    # 未完成
    re_path(r'^list/(?P<type_id>\d+)/(?P<page>\d+)$', ListView.as_view(), name='list'),  # 列表页
    path('', IndexView.as_view(), name='index'),
]

