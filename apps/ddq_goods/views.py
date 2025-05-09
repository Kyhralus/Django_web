from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from apps.ddq_goods.models import GoodsType, IndexGoodsBanner, IndexPromotionBanner, IndexTypeGoodsBanner, GoodsSKU
from django_redis import get_redis_connection
from django.core.cache import cache
# Create your views here.

# http://127.0.0.1:8000
class IndexView(View):
    '''首页'''
    def get(self, request):
        '''显示首页'''
        # 尝试从缓存中获取数据
        context = cache.get('index_page_data')

        if context is None:
            types = GoodsType.objects.all() # 获取商品的种类信息
            # 获取首页页面幻灯片中的商品信息，以index字段（展示顺序）进行排序
            goods_banners = IndexGoodsBanner.objects.all().order_by('index')
            # 获取首页促销活动信息，以以index字段（展示顺序）进行排序
            promotion_banners = IndexPromotionBanner.objects.all().order_by('index')
            for type in types:  # GoodsType
                '''
                获取首页中分类商品展示信息（types），遍历商品种类信息，获取每个商品种类（type）为GoodsType对象
                然后在数据库商品分类表（IndexTypeGoodsBanner）中根据type字段（商品类型）以及display_type（展示类型）查询数据，并按照表index字段（展示顺序）进行排序显示
                display_type=1表示图片展示类型，display_type=2表示文字展示类型；
                然后给每个商品种类对象添加image_banners属性以及title_banners属性
                '''
                # 获取type种类首页分类商品的图片展示信息
                image_banners = IndexTypeGoodsBanner.objects.filter(type=type, display_type=1).order_by('index')
                # 获取type种类首页分类商品的文字展示信息
                title_banners = IndexTypeGoodsBanner.objects.filter(type=type, display_type=0).order_by('index')

                # 动态给type增加属性，分别保存首页分类商品的图片展示信息和文字展示信息
                type.image_banners = image_banners
                type.title_banners = title_banners

            context = {'types': types,
                       'goods_banners': goods_banners,
                       'promotion_banners': promotion_banners}
            # 设置缓存
            # key  value timeout
            cache.set('index_page_data', context, 3600)

        # 获取用户购物车中商品的数目
        user = request.user
        cart_count = 0
        if user.is_authenticated:
            # 用户已登录
            conn = get_redis_connection('default')
            cart_key = 'cart_%d' % user.id
            cart_count = conn.hlen(cart_key)

        # 组织模板上下文
        context.update(cart_count=cart_count)

        # 使用模板
        return render(request, 'index.html', context)

# /goods/商品id
class DetailView(View):
    """详情页"""
    def get(self, request, goods_id):
        """显示商品详情页"""
        # 根据商品goods_id, 获取商品信息，如果查询不到则返回首页
        try:
            sku = GoodsSKU.objects.get(id=goods_id)
        except GoodsSKU.DoesNotExist:
            # 此goods_id的商品不存在
            return redirect(reverse("goods:index"))
        return render(request, "detail.html")
        # 获取所有的商品类型
        types = GoodsType.objects.all()
        # 从订单模块中根据查询到的sku对象查询出评论不为空的评论信息
        sku_orders_comment = OrderGoods.objects.filter(sku=sku).exclude(comment='')
        # 根据查询到的商品sku对象获取商品信息按照创建时间进行倒序排序并且只显示最前面两个
        new_skus = GoodsSKU.objects.filter(type=sku.type).order_by('-create_time')[:2]
        # 获取用户购物车中商品的数目
        user = request.user  # 获取user对象
        cart_count = 0  # 默认设置为0
        # 获取商品详情页中的购物车数目信息
        if user.is_authenticated:  # 如果返回True表示用户已登录
            # 用户已登录
            conn = get_redis_connection('default')  # 获取配置中default默认redis连接对象
            cart_key = 'cart_%d' % user.id  # 设置key
            # 通过hlen方法获取购物车商品数目
            cart_count = conn.hlen(cart_key)
        # 定义模板上下问
        content = {"types": types, "sku": sku,
                   "sku_orders_comment": sku_orders_comment,
                   "new_skus": new_skus, "cart_count": cart_count}
        return render(request, "detail.html", content)