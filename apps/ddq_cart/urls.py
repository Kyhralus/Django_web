# coding:utf-8
from django.urls import path,re_path
from .views import *

urlpatterns = [
    path('add', CartAddView.as_view(), name='add'),  # 购物车记录添加
    path('', CartInfoView.as_view(), name='show'),  # 购物车页面显示
    path('update', CartUpdateView.as_view(), name='update'),  # 购物车记录更新
    path('delete', CartDeleteView.as_view(), name='delete'),  # 购物车记录删除
]

'''
在 Django 2.0 之后，推荐使用path()和re_path()代替旧的url()函数，并且不再需要手动添加^（开始）和$（结束）正则表达式符号
'''