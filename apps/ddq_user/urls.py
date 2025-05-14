# coding:utf-8
# apps/ddq_user/urls.py
from django.urls import path, re_path
# from django.contrib.auth.decorators import login_required
from .views import RegisterView, ActiveView, LoginView, LogoutView, UserInfoView, UserHistoryView, UserOrderView, UserAddressView
from .views import UserBalanceView
'''
导入django模块中的login_required方法
验证用户是否是登录状态，也就是获取session的值
如果用户是登录状态，那么则可以访问需要登录成功后所访问的页面
如果用户未登录，直接访问需要登录后才能看到的页面
则login_required方法默认跳转到 http://127.0.0.1:8000/accounts/login/?next=/user/ 页面
'''

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),     # 注册页面
    # re_path(r"register_handle$", views.register_handle, name="register_handle"),  # 注册数据处理,考虑是否需要用正则表达式
    re_path(r"^active/(?P<token>.*)$", ActiveView.as_view(), name="active"),  # 账户激活
    re_path(r"^login$", LoginView.as_view(), name="login"),  # 登录
    re_path(r'^logout$', LogoutView.as_view(), name='logout'), # 退出登陆

    # 封装前 为不美观不统一而封装
    # url(r'^$', login_required(UserInfoView.as_view()), name='user'), # 用户中心-信息页
    # url(r'^order$', login_required(UserOrderView.as_view()), name='order'), # 用户中心-订单页
    # url(r'^address$', login_required(AddressView.as_view()), name='address'), # 用户中心-地址页

    re_path(r'^$', UserInfoView.as_view(), name='user'),  # 用户中心-信息页
    re_path(r"^order/(?P<page>\d+)$", UserOrderView.as_view(), name='order'),  # 用户中心-订单页
    re_path(r'^address$', UserAddressView.as_view(), name='address'),  # 用户中心-地址页
    path("history", UserHistoryView.as_view(), name="history"), # 用户中心-浏览记录
    path('balance', UserBalanceView.as_view(), name='balance'), # 余额充值
]


