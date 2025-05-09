# Register your models here.
from django.contrib import admin
from apps.ddq_goods.models import GoodsType,GoodsSKU,Goods,IndexGoodsBanner,IndexPromotionBanner,IndexTypeGoodsBanner

# 注册商品类型模型类
admin.site.register(GoodsType)
# 注册商品SKU模型类
admin.site.register(GoodsSKU)
# 注册商品类型
admin.site.register(Goods)

admin.site.register(IndexGoodsBanner)

admin.site.register(IndexPromotionBanner)

admin.site.register(IndexTypeGoodsBanner)


#
# admin.site.register(GoodsTypeAdmin)
# admin.site.register(IndexGoodsBannerAdmin)
# admin.site.register(IndexTypeGoodsBannerAdmini)
# admin.site.register(IndexPromotionBannerAdmin)
