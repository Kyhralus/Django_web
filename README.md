1. 激活虚拟环境
```bash
conda activate django5_web
```
2. 创建apps --- 创建后把它们移动到apps文件夹下
```bash
python manage.py startapp <应用名称>
```

# database
username: Kyhralus\
email: alineyiee@shu.edu.cn

网络管理员和内容管理员要分开\
**没用人能从服务器删除任何数据**
- 网络管理员：不会让内容管理员修改任何内容 \
管理员看不到密码

# 会考的命令
```bash
django-admin startproject <项目名称>
python manage.py runserver # 需要在项目文件下运行
# 数据库
python manage.py migrate # 没有编任何app时 ---> 全部初始化
python manage.py makemigrations # 是 Django 项目中用于生成数据库迁移文件的命令
python manage.py createsuperuser
```


# 一些问题
git的配置需要在本地的git bash中运行
