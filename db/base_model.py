# -*- coding: utf-8 -*-
from django.db import models

class BaseModel(models.Model):
    """
    抽象模型基类，为所有模型提供公共字段
    - create_time: 自动记录对象创建时间
    - update_time: 自动记录对象最后更新时间
    - is_delete: 逻辑删除标记，代替物理删除
    """
    create_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name="创建时间",
        help_text="对象首次创建的时间"
    )
    update_time = models.DateTimeField(
        auto_now=True,
        verbose_name="更新时间",
        help_text="对象最后一次修改的时间"
    )
    is_delete = models.BooleanField(
        default=False,
        verbose_name="删除标记",
        help_text="设置为True时表示逻辑删除，不实际从数据库中删除"
    )

    class Meta:
        abstract = True  # 指定为抽象基类，不创建数据库表
        verbose_name = "基础模型"
        verbose_name_plural = verbose_name
        ordering = ['-create_time']  # 默认按创建时间倒序排列