from django.contrib.auth.decorators import  login_required
"""
    LoginRequiredMixin类，封装login_required方法
"""

class LoginRequiredMixin(object):
    @classmethod   # 类方法
    def as_view(cls, **initkwargs):
        # 调用父类的as_view
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)
