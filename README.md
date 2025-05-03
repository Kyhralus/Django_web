# 版本和依赖
- python 3.11.7
- django 5.2
    - django-extensions
    - tinymce
    - crispy_forms
    - crispy-bootstrap5
    - cryptography
- Pillow


1. 激活虚拟环境
```bash
conda activate django5_web
```
2. 创建apps --- 创建后把它们移动到apps文件夹下
```bash
python manage.py startapp <应用名称>
```

安装django扩展
```bahs
pip install django-extensions # 用于看urls映射关系等
# 记得在INSTALLED_APPS中添加 'django_extensions',
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
查看url映射
```bash
python manage.py show_urls # 需要安装django-extensions
```

# MYSQL数据库
host=localhost\
username:root\
password: 123456
```bash
create database <数据库名称> charset=utf8;
```
# 一些问题
1. git的配置需要在本地的git bash中运行
2. contributor的显示要有两个人以上，才会在仓库的右侧边栏显示
3. pycharm中如果需要指明提交人，需要在commit界面的右下角齿轮处设置自己的名称和邮箱，然后提交即可


# 附录
```bash
pip list | grep <包名> # 查看安装的包
```
