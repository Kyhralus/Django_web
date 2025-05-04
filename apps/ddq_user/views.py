from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages
from django.views.generic import View
from django.core.mail import send_mail
from DongDongQiang import settings
import re
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
# from celery_tasks.tasks import send_email   # 待添加
# 从其他模块导入函数
from utils.mixin import LoginRequiredMixin
from apps.ddq_user.models import Address, User
from apps.ddq_goods.models import GoodsSKU
from django_redis import get_redis_connection

# 生成令牌
def generate_token(user_id):
    serializer = URLSafeTimedSerializer(settings.SECRET_KEY, salt='account-activation')
    return serializer.dumps({'user_id': user_id})

# 验证令牌
def verify_token(token):
    serializer = URLSafeTimedSerializer(settings.SECRET_KEY, salt='account-activation')
    try:
        data = serializer.loads(token, max_age=3600)  # 有效期1小时
        return data['user_id']
    except SignatureExpired:
        return None

# Create your views here.
# /user/register
'''
有待优化部分
'''

# User = get_user_model()  # 获取项目中使用的用户模型

class RegisterView(View):
    """注册"""
    def get(self, request):
        """显示注册页面"""
        return render(request, "register.html")

    def post(self, request):
        """处理用户注册数据"""
        # 1. 获取数据
        username = request.POST.get("user_name")
        password = request.POST.get("pwd")
        email = request.POST.get("email")
        print(email)
        allow = request.POST.get("allow")
        # 2. 数据校验
        if not all([username, password, email]):  # 判断是否有空值
            return render(request, "register.html", {"error_msg": "数据不完整"})
        if not re.match(r"^[a-zA-Z0-9][\w.\-]*@[a-zA-Z0-9\-]+(\.[a-zA-Z]{2,5}){1,2}$", email):  # 正则表达式匹配邮箱格式
            return render(request, "register.html", {"error_msg": "注册邮箱格式不正确"})
        if allow != "on":  # 如果没有勾选同意协议
            return render(request, "register.html", {"error_msg": "请勾选同意"})
        # 3. 注册用户
        '''
        进行用户注册，将数据保存在数据库用户名中。
        因为在执行迁移文件时，在settings中配置了django认证系统指定的模型类为df_user.User
        所以可以不使用传统方式向类中添加属性再保存到数据库，
        而是直接使用django认证系统封装好的create_user函数将数据直接保存到数据库

        因为使用了django认证系统也就通俗点说在df_user/models中的User类继承了AbstractUser类
        所以django的认证系统已经将用户注册时填写的密码进行加密处理后存到数据库
        这样我们就不用在视图函数中获取密码并加密然后再保存到数据库表中
        '''
        # 3.1 判断用户名是否存在
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            """如果出现该异常说明用户名不存在，则让user对象为空"""
            user = None

        # 如果user对象存在，则表示用户名已存在，返回错误提示信息
        if user:
            return render(request, "register.html", {"error_msg": "用户名已存在"})

        # 3.2 如果用户名不存在，则创建用户
        user = User.objects.create_user(username, email, password)
        # django认证系统默认用户表字段is_active为1（激活），所以这里需要进行设置为0（未激活）
        user.is_active = 0  # 设置用户为未激活状态
        user.save()  # 保存到数据库
        # 3.3 发送激活邮件
        # 3.3.1 生成token
        token = generate_token(user.id)
        # 3.3.2 发送激活邮件
        subject = "咚咚锵欢迎你"  # 邮件标题
        message = ''  # 邮件正文
        sender = settings.EMAIL_FROM  # 发件人
        receiver = [email]  # 收件人
        activation_url = request.build_absolute_uri(
            reverse('user:active', kwargs={'token': token})
        )
        html_message = f"""
                   <h1>{username} 恭喜您成为咚咚锵注册会员</h1><br/><h3>请您在1小时内点击以下链接进行账户激活</h3><a href="{activation_url}">{activation_url}</a>
        """
        send_mail(subject, message, sender, receiver, html_message=html_message)
        '''
         生成用户激活邮件中的token
         定义激活链接为 http://127.0.0.1:8000/user/active/用户id
         如果在链接地址明文显示用户的id值的话，就会出现某些懂技术的用户，修改链接地址中的用户id
         就很有可能去激活其他用户
         所以需要将链接地址中的用户id值进行加密并设置密钥的有效期
        '''

        # 4. 注册成功，跳转到登录页面
        '''
        当点击注册按钮时，此时在会跳转到form表单中的action地址（/user/register）
        匹配df_user/urls中的正则然后调用df_user/views中的register视图函数
        处理完数据后最终重定向到主页（index.html）
        '''
        return redirect(reverse("goods:index"))  # 使用反向解析跳转到首页 reverse(根基urls中的主页的namespace:goods模块中的urls主页的name)


class ActiveView(View):
    """账户激活"""
    def get(self, request, token):
        """进行用户激活"""
        user_id = verify_token(token)
        if user_id:
            try:
                user = User.objects.get(id=user_id)
                if user.is_active:
                    return HttpResponse("账户已激活")
                # 设置该用户对象中的is_active字段的值为1
                user.is_active = 1
                user.save()
                # 使用反向解析跳转到登录页
                return redirect(reverse("user:login"))
            except User.DoesNotExist:
                return HttpResponse("无效的激活链接")
        else:
            # 出现异常表示链接失效
            return HttpResponse("激活链接已过期")


class LoginView(View):
    """登录"""
    def get(self, request):
        """显示登录页"""
        # 判断是否勾选记住用户名
        if 'username' in request.COOKIES:
            username = request.COOKIES.get("username")
            checked = "checked"
        else:
            username = ''
            checked = ''

        return render(request, "login.html", {"username": username, "checked": checked})

    def post(self, request):
        """登录校验"""
        # 1. 获取数据
        username = request.POST.get("username")
        password = request.POST.get("pwd")
        # 2. 数据校验
        if not all([username, password]):
            print("error_msg: 数据不完整")
            return render(request, "login.html", {"error_msg": "数据不完整"})
        # 3. 校验用户名和密码
        user = authenticate(request, username=username, password=password)  # 正确返回user对象，不正确返回None
        if user is not None:
            # 用户名密码正确
            if user.is_active:
                # 用户已激活
                # 将用户登录成功后状态保存在session，使用django认证系统中的login方法
                login(request, user)
                # # 因为redirect方法返回的是HttpResponseRedirect对象，而这个对象是HttpResponse的子类，所以可以设置cookie
                # response = redirect(reverse("goods:index"))
                '''
                获取请求地址next参数的值
                如果当用户访问的是http://127.0.0.1:8000/user/login登录页面
                则next请求地址参数中的next参数无法获取
                所以设置默认值为反向解析主页地址
                '''
                next_url = request.GET.get("next", reverse("goods:index"))
                response = redirect(next_url)
                # 判断用户是否记勾选记住用户名
                remember = request.POST.get("remember")
                if remember == "on":
                    # 表示勾选了,将用户名保存在cookie中
                    response.set_cookie("username", username, max_age=7 * 24 * 3600)
                else:
                    # 删除cookie
                    response.delete_cookie("username")
                # 重定向到主页
                return response
            else:
                # 用户未激活
                print("error_msg: 账户未激活")
                return render(request, "login.html", {"error_msg": "账户未激活"})
        else:
            # 用户名或密码错误
            print("error_msg: 用户名或密码错误")
            return render(request, "login.html", {"error_msg": "用户名或密码错误"})
        # 4. 登录成功，跳转到主页

class LogoutView(View):
    """退出登录"""
    def get(self, request):
        """退出登录"""
        # 清除用户的session信息
        logout(request)

        # 跳转到首页
        return redirect(reverse('goods:index'))

# /user
class UserInfoView(LoginRequiredMixin, View):
    """用户中心-信息页"""
    def get(self, request):
        """显示"""
        # page='user'
        # 如果用户未登录->AnonymousUser类的一个实例
        # 如果用户登录->User类的一个实例
        # request.user.is_authenticated()
        # 文档地址：https://yiyibooks.cn/xx/django_182/topics/auth/default.html#user-objects
        # 除了你给模板文件传递的模板变量之外，django框架会把request.user也传给模板文件

        # 获取用户的个人信息
        user = request.user
        address = Address.objects.get_default_address(user)

        # 获取用户的历史记录
        # from redis import StrictRedis
        # sr = StrictRedis(host="127.0.0.1", port="6379", db=9)
        con = get_redis_connection('default')

        history_key = 'history_%d' % user.id

        # 获取用户最新浏览的5个商品的id
        sku_ids = con.lrange(history_key, 0, 4)

        # 从数据库中查询用户浏览的商品的具体信息
        #goods_li = GoodsSKU.objects.filter(id__in=sku_ids)

        # 第一种方式
        # goods_res = []
        # for a_id in sku_ids:
        #     for goods in goods_li:
        #         if a_id == goods.id:
        #             goods_res.append(goods)

        # 第二种方式：对应id一个一个的从数据库拿
        goods_li = []
        for id in sku_ids:
            goods = GoodsSKU.objects.get(id=id)
            goods_li.append(goods)

        # 组织上下文
        context = {'page': 'user',
                   'address': address,
                   'goods_li': goods_li}

        return render(request, 'user_center_info.html', context)

class UserOrderView(LoginRequiredMixin, View):
    """用户中心-订单"""
    def get(self, request):
        """显示页面"""
        return render(request, "user_center_info.html", {"page": "order"})

# /user/address
class UserAddressView(LoginRequiredMixin, View):
    """用户中心-地址"""
    def get(self, request):
        """显示"""
        # page='address'
        # 获取登录用户的对应的User对象
        user = request.user

        # 获取用户的默认收货地址
        # try:
        #     address = Address.objects.get(user=user, is_default=True)
        # except Address.DoesNotExist:
        #     # 不存在默认收获地址
        #     address = None
        address = Address.objects.get_default_address(user)    # 通过封装的模型管理器方法获取默认地址对象

        return render(request, 'user_center_site.html', {'page': 'address', 'address': address})

    def post(self, request):
        """地址的添加"""
        # 接受数据
        receiver = request.POST.get('receiver')
        addr = request.POST.get('addr')
        zip_code = request.POST.get('zip_code')
        phone = request.POST.get('phone')

        # 校验数据
        if not all([receiver, addr, phone]):
            return render(request, 'user_center_site.html', {'errmsg': '数据不完整'})

        # 校验数据
        if not re.match(r'^1[3|4|5|7|8][0-9]{9}$', phone):
            return render(request, 'user_center_site.html', {'errmsg': '手机格式不正确'})

        # 业务处理：地址添加
        # 如果用户已存在默认收获地址，添加的地址不作为默认收货地址，否则作为默认收货地址
        # 获取登录用户的对应的User对象
        user = request.user
        # try:
        #     address = Address.objects.get(user=user, is_default=True)
        # except Address.DoesNotExist:
        #     # 不存在默认收获地址
        #     address =None
        address = Address.objects.get_default_address(user)    # 通过封装的模型管理器方法获取默认地址对象

        if address:
            is_default = False
        else:
            is_default = True

        # 添加地址
        Address.objects.create(user=user,
                               receiver=receiver,
                               addr=addr,
                               phone=phone,
                               zip_code=zip_code,
                               is_default=is_default)

        # 返回应答,刷新地址页面 get请求
        return redirect(reverse('user:address'))

