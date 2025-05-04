# 版本和依赖
- python 3.11.7
- django 5.2
    - django-extensions
- tinymce
- cffi-1.17.1 
- cryptography-44.0.3 
- pycparser-2.22
- Pillow 11.2.1
- itsdangerous-2.2.0 # 注册激活邮件token
- django-redis-5.4.0
以下待使用...
- celery-5.5.2 # 异步任务---发送邮件 
- eventlet-0.39.1 # windows下配合celery使用
- redis-6.0.0 # redis数据库，作为celery的消息中间人

要加？
- crispy_forms
- crispy-bootstrap5
------------------------------------------
1. 激活虚拟环境
```bash
conda activate django # 这里的名字是自定义的，需要在conda中安装，即cmd中
```
2. 创建apps --- 创建后把它们移动到apps文件夹下
```bash
python manage.py startapp <应用名称>
```
# Django
安装django扩展
```bahs
pip install django-extensions # 用于看urls映射关系等
# 记得在INSTALLED_APPS中添加 'django_extensions',
```
## 会考的命令
```bash
django-admin startproject <项目名称>
python manage.py runserver # 需要在项目文件下运行
python manage.py makemigrations # 是 Django 项目中用于生成数据库迁移文件的命令
python manage.py migrate # 没有编任何app时 ---> 全部初始化
python manage.py createsuperuser
```
## 一些问题
修改 URL 配置后必须重启服务器，否则更改不会生效：
查看url映射
```bash
python manage.py show_urls # 需要安装django-extensions
```
------------------------------------------
# MYSQL数据库
## 1. 相关知识
username: Kyhralus\
email: alineyiee@shu.edu.cn\
host=localhost\
username:root\
password: 123456\

网络管理员和内容管理员要分开\
**没用人能从服务器删除任何数据**
- 网络管理员：不会让内容管理员修改任何内容 \
管理员看不到密码
## 2. 相关指令
```bash
create database <数据库名称> charset=utf8; # 创建数据库
SHOW DATABASES; # 查看数据库列表
DROP DATABASE <database_name>; # 删除数据库
USE <数据库名称>; # 选择数据库
SHOW TABLES; # 查看数据库中的表
SHOW COLUMNS FROM <数据库名称>; # 查看对应表中的列
DESCRIBE <对应数据库的表名称>; # 查看表的结构
SHOW CREATE TABLE <数据库名称> \G; # 查看表的创建语句

select * from <段名> \G; # 查看表中对应段的所有数据
```
------------------------------------------
# conda
## 1. 相关知识

## 2. 相关指令
```bash
conda env list # 查看所有conda环境
conda remove -n <环境名称> --all # 删除conda环境，与其所有依赖
conda remove --name <环境名称> --all # 删除conda环境
```
------------------------------------------
# pip
## 1. 相关知识
## 2. 相关指令
```bash
pip install <包名> # 安装包
pip uninstall <包名> # 卸载包
pip list # 查看安装的包
pip list | grep <包名> # 查看安装的包
pip freeze > requirements.txt # 导出当前环境的所有包
pip install -r requirements.txt # 安装requirements.txt中的所有包
pip install --upgrade <包名> # 升级包
pip install --upgrade pip # 升级pip
```
------------------------------------------
# github
1. git的配置需要在本地的git bash中运行
2. contributor的显示要有两个人以上，才会在仓库的右侧边栏显示
3. pycharm中如果需要指明提交人，需要在commit界面的右下角齿轮处设置自己的名称和邮箱，然后提交即可
------------------------------------------
# pyhcharm
1. crt+r: 查询字替换
2. ctrl+f: 查找
3. shift+end: 选中光标到行尾
4. shift+home: 选中光标到行首
5. shift+ctrl+end: 选中光标到文件尾
6. shift+ctrl+home: 选中光标到文件首
7. shift+ctrl+方向键: 选中光标到行首或行尾
------------------------------------------
# clergy
```bash
celery -A <celery实例对象> worker -l info -P eventlet # celery运行tasks.py

```
参考博客：
https://blog.csdn.net/m0_56966142/article/details/123801608
------------------------------------------
# redis
```bash
redis-cli # 在cmd中使用
select <redis数据库编号> # 选择redis数据库
keys * # 查看所有的key
    
```