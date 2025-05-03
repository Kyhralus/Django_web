from django.contrib.auth import get_user_model
User = get_user_model()
print(User)  # 应输出 <class 'DjangoWebApps.user.models.User'>

# 直接导入模型验证
from DjangoWebApps.user.models import User
print(User)  # 应与上面结果一致