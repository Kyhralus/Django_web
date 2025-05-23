# -*- coding: utf-8 -*-
from django.db import models
from db.base_model import BaseModel
from tinymce.models import HTMLField

class GoodsType(BaseModel):
    """商品类型模型类"""
    name = models.CharField(max_length=20, verbose_name='种类名称')
    logo = models.CharField(max_length=20, verbose_name='标识')
    image = models.ImageField(upload_to='type', verbose_name='商品类型图片')

    class Meta:
        db_table = 'ddq_goods_type'
        verbose_name = '商品种类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class GoodsSKU(BaseModel):
    """商品SKU模型类""" # GoodsSKU 通常用于存储商品的具体信息，例如价格、库存、规格等。通过 Django 的 ORM（对象关系映射），它会映射到数据库中的一张表，便于对商品数据进行增删改查操作。
    STATUS_CHOICES = (
        (0, '下线'),
        (1, '上线'),
    )

    type = models.ForeignKey('GoodsType', on_delete=models.CASCADE, verbose_name='商品种类')
    goods = models.ForeignKey('Goods', on_delete=models.CASCADE, verbose_name='商品SPU')
    name = models.CharField(max_length=20, verbose_name='商品名称')
    desc = models.CharField(max_length=256, verbose_name='商品简介')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='商品价格')   # max_digits：最多显示几位；decimal_places：小数点后几位
    unite = models.CharField(max_length=20, verbose_name='商品单位')
    image = models.ImageField(upload_to='goods', verbose_name='商品图片')
    stock = models.IntegerField(default=1, verbose_name='商品库存')
    sales = models.IntegerField(default=0, verbose_name='商品销量')
    status = models.SmallIntegerField(default=1, choices=STATUS_CHOICES, verbose_name='商品状态')

    class Meta:
        db_table = 'ddq_goods_sku'
        verbose_name = '商品'
        verbose_name_plural = verbose_name

    def __str__(self):  # django后台中文显示
        return self.name

class Goods(BaseModel):
    """商品SPU模型类"""   # SPU：Standard Product Unit 标准商品单位
    name = models.CharField(max_length=20, verbose_name='商品SPU名称')
    # 富文本类型:带有格式的文本
    detail = HTMLField(blank=True, verbose_name='商品详情') # blank:指明可以不输入内容(从创建内容有效性)；null:指明数据库能不能为空
    # detail = models.TextField(verbose_name='商品详情')
    class Meta:
        db_table = 'ddq_goods'
        verbose_name = '商品SPU'
        verbose_name_plural = verbose_name

    def __str__(self):  # django后台中文显示
        return self.name

class GoodsImage(BaseModel):
    """商品图片模型类"""
    sku = models.ForeignKey(GoodsSKU, on_delete=models.CASCADE, verbose_name='商品')
    image = models.ImageField(upload_to='goods', verbose_name='图片路径')

    class Meta:
        db_table = 'ddq_goods_image'
        verbose_name = '商品图片'
        verbose_name_plural = verbose_name

class IndexGoodsBanner(BaseModel):
    """首页轮播商品展示模型类"""
    sku = models.ForeignKey(GoodsSKU, on_delete=models.CASCADE, verbose_name='商品')
    image = models.ImageField(upload_to='banner', verbose_name='图片')
    index = models.SmallIntegerField(default=0, verbose_name='展示顺序')

    class Meta:
        db_table = 'ddq_index_banner'
        verbose_name = '首页轮播商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.sku.name









































# =============  未使用 ==============
class IndexTypeGoodsBanner(BaseModel):
    """首页分类商品展示模型类"""
    DISPLAY_TYPE_CHOICES = (
        (0, "标题"),
        (1, "图片")
    )

    type = models.ForeignKey(GoodsType, on_delete=models.CASCADE, verbose_name='商品类型')
    sku = models.ForeignKey(GoodsSKU, on_delete=models.CASCADE, verbose_name='商品SKU')
    display_type = models.SmallIntegerField(default=1, choices=DISPLAY_TYPE_CHOICES, verbose_name='展示类型')
    index = models.SmallIntegerField(default=0, verbose_name='展示顺序')

    class Meta:
        db_table = 'ddq_index_type_goods'
        verbose_name = "主页分类展示商品"
        verbose_name_plural = verbose_name

    def __str__(self):  # django后台中文显示
        return self.name

# =============  未使用 ==============
class IndexPromotionBanner(BaseModel):
    """首页促销活动模型类"""
    name = models.CharField(max_length=20, verbose_name='活动名称')
    url = models.CharField(max_length=256,  verbose_name='活动链接')
    '''
    将df_goods/models中的IndexPromotionBanner首页促销活动模型类的url字段的类型修改为CharField类型
    因为URLField类型，在admin中注册后，在django管理后台进行添加时，会去解析URL链接地址是否有效
    并且该字段是必须填写的，所以修改为CharField类型，就可填可不填，并且不用去解析
    '''
    image = models.ImageField(upload_to='banner', verbose_name='活动图片')
    index = models.SmallIntegerField(default=0, verbose_name='展示顺序')

    class Meta:
        db_table = 'ddq_index_promotion'
        verbose_name = "主页促销活动"
        verbose_name_plural = verbose_name

    def __str__(self):  # django后台中文显示
        return self.name