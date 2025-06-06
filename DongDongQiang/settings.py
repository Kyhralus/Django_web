"""
Django settings for DongDongQiang project.

Generated by 'django-admin startproject' using Django 5.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path
import os,sys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# 引入apps
apps_dire = sys.path.insert(0, os.path.join(BASE_DIR, "apps"))
print("apps dire",sys.path)
'''
['D:\\JetBrains\\PycharmProjects\\DongDongQiang\\apps', 'D:\\JetBrains\\PycharmProjects\\DongDongQiang\\DongDongQiang'
, 'D:\\JetBrains\\PycharmProjects\\DongDongQiang', 'D:\\JetBrains\\PyCharm 2023.3.5\\plugins\\python-ce\\helpers\\pycharm_display'
, 'D:\\anaconda3\\python312.zip', 'D:\\anaconda3\\DLLs', 'D:\\anaconda3\\Lib', 'D:\\anaconda3', 'D:\\JetBrains\\PycharmProjects\\DongDongQiang\\.venv'
, 'D:\\JetBrains\\PycharmProjects\\DongDongQiang\\.venv\\Lib\\site-packages', 'D:\\JetBrains\\PyCharm 2023.3.5\\plugins\\python-ce\\helpers\\pycharm_matplotlib_backend'
, 'D:\\JetBrains\\PyCharm 2023.3.5\\plugins\\python-ce\\helpers\\pycharm_plotly_backend']
'''


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-c-qbpvq!jih=d!i35x#p3e@fq!t6u9!hf9+d&#-vifryiso^+r"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'ddq_cart',  # 购物车模块
    'ddq_goods',  # 商品模块
    'ddq_order',  # 订单模块
    'ddq_user',  # 用户模块
    'tinymce',  # 富文本编辑器
    'haystack',

]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "DongDongQiang.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates']
        ,
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "DongDongQiang.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dongdongqiang',                # 数据库名称
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': 'localhost'
    }
}



# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR /'static']

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# 富文本编辑器配置
TINYMCE_DEFAULT_CONFIG = {
    # 'theme': 'advanced',
    'theme': 'silver',
    'width': 600,
    'height': 400,
}

# django认证系统指定的模型类
AUTH_USER_MODEL = 'ddq_user.User'

'''
登录未激活的账号
这里有一个bug那就是在进行未激活账号登录时一直提示用户名和密码错误
在post方法中通过打印username和password的值查看输入的用户名和密码没错与当初注册时填写的用户名密码对的上
查看django认证系统文档，方法时候啥的都没问题
但是在校验用户名密码时调用的authenticate方法一直返回的是None
这就很奇怪了，通过网上查资料发现需要在settings配置文件中添加如下配置
让django认证系统中的create_user方法再保存用户注册数据时，不关联用户表中的is_active字段
这样再进行登录验证时调用authenticate方法返回错误的None对象
'''
AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.AllowAllUsersModelBackend']
# ============================ 激活邮件token配置 ============================
# 发送邮件配置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 25
# 发送邮件的邮箱
EMAIL_HOST_USER = 'alineyiee@163.com'
# 在邮箱中设置的客户端授权密码
# smtp授权码：JHVDHnqrCm5gmv2b
EMAIL_HOST_PASSWORD = 'JHVDHnqrCm5gmv2b'
# 收件人看到的发件人
EMAIL_FROM = 'dongdongqiang<alineyiee@163.com>'

# ============================ 缓存django-redis配置 ============================
# django缓存配置
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/5",         # redis数据库5来执行任务 （厨师）
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# 使用django-redis 作为 session 储存后端,关闭即可不用redis缓存
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

# 在官网文档中调用login_required方法，设置验证不成功跳转的地址，则需要在项目settings配置文件中配置LOGIN_URL，设置为登录地址
LOGIN_URL = "http://127.0.0.1:8000/user/login?next=/user/"

# 全文检索haystack框架配置
HAYSTACK_CONNECTIONS = {
    'default': {
        # 使用whoosh引擎
        'ENGINE': 'haystack.backends.whoosh_cn_backend.WhooshEngine',
        # 索引文件路径
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    }
}
# 当数据库表 添加、修改、删除数据时，自动生成索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'