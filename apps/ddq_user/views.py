from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib import messages
import re
# Create your views here.
# /user/register
'''
有待优化部分
'''
User = get_user_model()  # 获取项目中使用的用户模型

def register(request):  # ，request: HttpRequest 可以简化为 request，因为在 Django 中，request 参数的类型是隐式约定的，不需要显式声明类型注解
    """显示注册页面"""
    return render(request, "register.html") # 将给定的模板与给定的上下文字典组合在一起，并以渲染的文本返回一个 HttpResponse 对象。

# /user/register/handle
def register_handle(request):
    """处理用户注册数据"""
    # 1. 获取数据
    username = request.POST.get("user_name")
    password = request.POST.get("pwd")
    email = request.POST.get("email")
    allow = request.POST.get("allow")
    # 2. 数据校验
    if not all([username, password, email]):   # 判断是否有空值
        return render(request, "register.html", {"error_msg": "数据不完整"})
    if not re.match(r"^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$", email):   # 正则表达式匹配邮箱格式
        return render(request, "register.html", {"error_msg": "邮箱格式不正确"})
    if allow != "on":       # 如果没有勾选同意协议
        return render(request, "register.html", {"error_msg": "请勾选同意"})
    # 3. 注册用户
    '''
    进行用户注册，将数据保存在数据库用户名中。
    因为在执行迁移文件时，在settings中配置了django认证系统指定的模型类为df_user.User
    所以可以不使用传统方式向类中添加属性再保存到数据库，
    而是直接使用django认证系统封装好的create_user函数将数据直接保存到数据库
    '''

    user = User.objects.create_user(username, email, password)
    # 4. 注册成功，跳转到登录页面
    return redirect(reverse("goods:index"))  #  使用反向解析跳转到首页 reverse(根基urls中的主页的namespace:goods模块中的urls主页的name)