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

class AddressManager(models.Manager):
    """地址模型类管理器"""
    '''
    在类中定义一个方法用于操作模型类对应的数据表
    将视图中的UserAddressView类里获取登录后用户的地址对象代码拷贝到此方法中，进行封装
    '''
    # 用于操作模型类对应的数据表
    def get_default_address(self, user):
        try:
            address = self.get(user=user, is_default=True)
        except self.model.DoesNotExist:
            # 出现异常表示该用户还没有设置默认地址
            address = None

        return address

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
    phone = models.CharField(max_length=11, verbose_name='联系电话')
    is_default = models.BooleanField(default=False, verbose_name='是否默认')

    # 自定义一个模型管理器对象
    objects = AddressManager()

    class Meta:   # 是 Django 模型类的一个内部类，用于定义模型的元数据。元数据是关于模型的“数据”，例如数据库表名、排序规则、单复数名称等。
        db_table = 'ddq_address'
        verbose_name = '地址'
        verbose_name_plural = verbose_name
        ordering = ['-is_default', '-create_time']  # 默认排序：默认地址优先，最新创建优先

class BalanceManager(models.Manager):
    """用户余额模型管理器"""

    def get_or_create_balance(self, user):
        """获取用户余额对象，如果不存在则创建"""
        balance, created = self.get_or_create(user=user, defaults={'amount': 0.00})
        return balance

    def get_amount(self, user):
        """获取余额数值"""
        balance = self.get_or_create_balance(user)
        return balance.amount


class Balance(models.Model):
    """单独管理用户余额"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='balance_account')
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=10000.00, verbose_name='余额')

    objects = BalanceManager()  # 指定自定义管理器

    class Meta:
        db_table = 'ddq_user_balance'
        verbose_name = '用户余额'
        verbose_name_plural = verbose_name


