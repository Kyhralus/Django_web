# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from db.base_model import BaseModel

class User(AbstractUser, BaseModel):
    """
    用户模型类，继承自 Django 内置的 AbstractUser 和自定义 BaseModel
    """
    class Meta:
        db_table = 'ddq_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

class Address(BaseModel):
    """
    地址模型类，关联到用户
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,  # 必需参数：用户删除时地址级联删除
        related_name='addresses',  # 添加反向关联名称
        verbose_name='所属账户'
    )
    receiver = models.CharField(max_length=20, verbose_name='收件人')
    addr = models.CharField(max_length=256, verbose_name='收件地址')
    zip_code = models.CharField(max_length=6, blank=True, null=True, verbose_name='邮政编码')
    phone = models.CharField(max_length=11, verbose_name='联系电话')
    is_default = models.BooleanField(default=False, verbose_name='是否默认')

    class Meta:
        db_table = 'ddq_address'
        verbose_name = '地址'
        verbose_name_plural = verbose_name
        ordering = ['-is_default', '-create_time']  # 默认排序：默认地址优先，最新创建优先