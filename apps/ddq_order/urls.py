# coding:utf-8
from django.urls import path, re_path
from apps.ddq_order.views import OrderPlaceView, OrderCommitView, CommentView, PayOrderView
urlpatterns = [
    path('place', OrderPlaceView.as_view(), name='place'),  # 提交订单页面显示
    path('commit', OrderCommitView.as_view(), name='commit'),  # 提交创建
    # path('pay', OrderPayView.as_view(), name='pay'),  # 订单支付
    # path('check', CheckPayView.as_view(), name='check'),  # 查询支付订单结果
    re_path(r'comment/(?P<order_id>.+)/$', CommentView.as_view(), name='comment'),  # 订单评论
    path('pay/<int:order_id>/', PayOrderView.as_view(), name='pay_order'),
]