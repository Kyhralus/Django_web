from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.db import transaction
from django.contrib import messages
from django.urls import reverse  # 修改导入路径
from django.conf import settings
from django.views.generic import View

from apps.ddq_user.models import Address, User, Balance
from apps.ddq_goods.models import GoodsSKU
from apps.ddq_order.models import OrderInfo, OrderGoods

from django_redis import get_redis_connection
from utils.mixin import LoginRequiredMixin
from datetime import datetime

import logging

import os
# Create your views here.
# /order/place
class OrderPlaceView(LoginRequiredMixin, View):
    """提交订单页面显示"""
    def post(self, request):
        """提交订单页面显示"""
        # 获取我们的登录用户
        user = request.user
        # 获取参数sku_ids
        sku_ids = request.POST.getlist('sku_ids')

        # 校验参数
        if not sku_ids:
            # cart page
            return redirect(reverse('cart:show'))

        conn = get_redis_connection('default')
        cart_key = 'cart_%d' % user.id

        skus = []
        # 保存商品的总家属和总价
        total_count = 0
        total_price = 0
        # 便利sku_ids获取用户要购买的商品的信息
        for sku_id in sku_ids:
            # 根据商品的id获取商品的信息
            sku = GoodsSKU.objects.get(id=sku_id)
            # 获取用户要购买的商品的数量
            count = int(conn.hget(cart_key, sku_id))
            # 计算商品的小计
            amount = sku.price * int(count)
            # 动态给sku增加属性count,保存购买商品的数量
            sku.count = count
            # 动态给sku添加属性amount,保存购买商品的小计
            sku.amount = amount
            # 追加
            skus.append(sku)
            # 累加计算商品的总价和总剑术
            total_count += int(count)
            total_price += amount

        # 云飞： 世纪开发的时候，属于一个子系统
        transit_price = 10 # 写思

        # 是付款
        total_pay = total_price + transit_price

        # 获取用户的首见地址
        addrs = Address.objects.filter(user=user)

        # 组织上下文
        sku_ids = ','.join(sku_ids) # [1, 25]->1, 25
        context = {'skus':skus,
                   'total_count': total_count,
                   'total_price': total_price,
                   'transit_price': transit_price,
                   'total_pay': total_pay,
                   'addrs': addrs,
                   'sku_ids': sku_ids}

        # 使用模板
        return render(request, 'place_order.html', context)


class OrderCommitView(View):
    """创建订单"""
    def post(self, request):
        user = request.user
        if not user.is_authenticated:
            return JsonResponse({"res": 0, "error_msg": "请先登录"})
        # 获取参数
        addr_id = request.POST.get("addr_id")
        pay_method = request.POST.get("pay_method")
        sku_ids = request.POST.get("sku_ids")
        # 校验参数
        if not all([addr_id, pay_method, sku_ids]):
            return JsonResponse({"res": 1, "error_msg": "参数不完整"})
        # 判断前端传递过来的支付方式是否存在
        if pay_method not in OrderInfo.PAY_METHODS:
            return JsonResponse({"res": 2, "error_msg": "非法的支付方式"})

        # 判断前端传递过来的收货地址是否存在
        try:
            addr = Address.objects.get(id=addr_id)
        except Address.DoesNotExist:
            return JsonResponse({"res": 3, "error_msg": "非法的收货地址"})
        # 1 自定义order_id 20190408174330+用户id（作为唯一标识）
        order_id = datetime.now().strftime("%Y%m%d%H%M%S") + str(user.id)
        # 2 总件数和总金额初始设置为0
        total_count = 0
        total_price = 0
        # 3 运费
        transit_price = 10

        # 向ddq_order_info表中插入记录
        order = OrderInfo.objects.create(
            order_id=order_id, user=user,
            addr=addr, pay_method=pay_method,
            total_count=total_count, total_price=total_price,
            transit_price=transit_price)
        conn = get_redis_connection("default")
        cart_key = "cart_%d" % user.id
        sku_ids = sku_ids.split(',')
        for sku_id in sku_ids:
            # 获取商品信息
            try:
                sku = GoodsSKU.objects.get(id=sku_id)
            except GoodsSKU.DoesNotExist:
                return JsonResponse({"res": 4, "error_msg": "商品不存在"})
            # 从redis数据库中获取用户购买商品的数量
            count = conn.hget(cart_key, sku_id)

            # 向ddq_order_goods表中添加记录
            OrderGoods.objects.create(
                order=order, sku=sku,
                count=count, price=sku.price)

            # 更新商品的库存和销量
            sku.stock -= int(count)
            sku.sales += int(count)
            sku.save()

            # 累加计算订单商品的总数量和总价格
            amount = sku.price * int(count)
            total_count += int(count)
            total_price += amount

        order.total_count = total_count
        order.total_price = total_price
        order.save()
        conn.hdel(cart_key, *sku_ids)  # *sku_ids ---> [1,2,3]变成1,2,3
        # 返回正确响应
        return JsonResponse({'res': 5, 'error_message': '订单创建成功'})

# ajax　post
# 前端传递的参数： 订单id(order_id)
# /order/pay
logger = logging.getLogger(__name__)
from django.shortcuts import redirect, render


class PayOrderView(View):
    def post(self, request, order_id):
        try:
            user = request.user
            order = OrderInfo.objects.get(order_id=order_id, user=user)
        except OrderInfo.DoesNotExist:
            messages.error(request, "订单不存在")
            return redirect(reverse('user:order'))

        try:
            balance, created = Balance.objects.get_or_create(user=user)
        except Exception as e:
            messages.error(request, "系统错误，请稍后重试")
            return redirect(reverse('user:order'))

        if balance.amount >= order.total_price:
            try:
                with transaction.atomic():
                    balance.amount -= order.total_price
                    balance.save()
                    order.order_status = 4
                    # order.order_status = OrderInfo.ORDER_STATUS_ENUM["UNSEND"]
                    order.save()
                    messages.success(request, "支付成功")
                    # 提供 page 参数，假设默认是第一页
                    return redirect(reverse('user:order', kwargs={'page': 1}))
            except Exception as e:
                messages.error(request, "支付处理失败，请稍后重试")
                # 提供 page 参数，假设默认是第一页
                return redirect(reverse('user:order', kwargs={'page': 1}))
        else:
            messages.error(request, "余额不足，请先充值")
            return redirect(reverse('user:order', kwargs={'page': 1}))


class CommentView(LoginRequiredMixin, View):
    """订单评论"""
    def get(self, request, order_id):
        """提供评论页面"""
        user = request.user
        # 校验数据
        if not order_id:
            return redirect(reverse('user:order'))

        try:
            order = OrderInfo.objects.get(order_id=order_id, user=user)
        except OrderInfo.DoesNotExist:
            return redirect(reverse("user:order"))

        # 根据订单的状态获取订单的状态标题
        order.status_name = OrderInfo.ORDER_STATUS[order.order_status]

        # 获取订单商品信息
        order_skus = OrderGoods.objects.filter(order_id=order_id)
        for order_sku in order_skus:
            # 计算商品的小计
            amount = order_sku.count*order_sku.price
            # 动态给order_sku增加属性amount,保存商品小计
            order_sku.amount = amount
        # 动态给order增加属性order_skus, 保存订单商品信息
        order.order_skus = order_skus

        # 使用模板
        return render(request, "order_comment.html", {"order": order})

    def post(self, request, order_id):
        """处理评论内容"""
        user = request.user
        # 校验数据
        if not order_id:
            return redirect(reverse('user:order'))

        try:
            order = OrderInfo.objects.get(order_id=order_id, user=user)
        except OrderInfo.DoesNotExist:
            return redirect(reverse("user:order"))

        # 获取评论条数
        total_count = request.POST.get("total_count")
        print("comment total_count:",total_count)
        total_count = int(total_count)

        # 循环获取订单中商品的评论内容
        for i in range(1, total_count + 1):
            # 获取评论的商品的id
            sku_id = request.POST.get("sku_%d" % i) # sku_1 sku_2
            # 获取评论的商品的内容
            content = request.POST.get('content_%d' % i, '') # cotent_1 content_2 content_3
            print("comment sku_id:",sku_id,"content:",content)
            try:
                order_goods = OrderGoods.objects.get(order=order_id, sku_id=sku_id)
            except OrderGoods.DoesNotExist:
                print("OrderGoods.DoesNotExist")
                continue
            print("comment are:",content)
            order_goods.comment = content
            order_goods.save()

        order.order_status = 5  # 已完成
        order.save()
        # 提供 page 参数，假设默认是第一页
        return redirect(reverse("user:order", kwargs={"page": 1}))