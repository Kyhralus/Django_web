# 版本和依赖
- python 3.11.7
- django 5.2
    - django-extensions # 用于看urls映射关系等
    - django-haystack # 全文检索框架，用于搜索商品
    - django-redis # 缓存，用于存储历史浏览记录
    - django-tinymce # 富文本编辑，商品详情编写（不实用）
    - django-bootstrap # 用于bootstrap框架，用于美化前端：尤其是主页的弹出显示
- cryptography-44.0.3 # 用于密钥认证：加密算法库，提供哈希、对称加密（AES）、非对称加密（RSA）、数字证书等功能
- Pillow 11.2.1 # 对导入图片操作。主要是生成缩略图、处理用户上传的图片、图片验证码等 Web 应用中的常见需求
- itsdangerous-2.2.0 # 注册激活邮件token
- pymysql-1.1.1 # 数据库
- redis-6.0.0 # redis数据库，主要用于存储历史浏览记录
- redis-py-5.4.0 # 用于redis数据库
- dnspython==2.7.0  # DNS（域名系统）解析库，用于查询和操作 DNS 记录 
- eventlet==0.39.1  # 基于协程的并发框架，实现高并发的网络应用，支持异步 I/O 
- greenlet==3.2.1   # 轻量级协程实现，为 Python 提供用户空间的上下文切换机制。作为 gevent、eventlet 等库的底层协程支持，提升异步任务的切换效率
- itsdangerous==2.2.0 # 安全序列化与签名工具，用于生成安全的令牌、验证数据完整性
- jieba==0.42.1  # 中文分词库，支持精确分词、全模式分词和搜索引擎模式分词
- packaging==25.0  # Python 包版本管理工具，提供版本解析、比较和验证功能
- PyMySQL==1.1.1   # Python 操作 MySQL 数据库的驱动，实现 MySQL 协议的纯 Python 版本
- python-dateutil==2.9.0.post0  # 期和时间处理库，扩展了 Python 标准库 datetime 的功能，支持时区转换、相对日期计算等
- Whoosh==2.7.4   # 纯 Python 实现的全文搜索引擎库，支持索引构建、搜索查询和高亮显示

------------------------------------------
# 实现功能：
1. 商品展示 
- [x] 首页展示：显示商品、首页幻灯片商品、促销活动。
- [x] 详情页展示：显示商品的详细信息、评论信息、新品信息和同 SPU 的其他规格商品。
- [x] 搜索页展示：支持中文模糊搜索。
2. 用户管理
- [x] 注册与登录：用户可以注册新账户，并使用注册的账户登录系统。
- [x] 账户激活：用户注册后需要通过邮箱激活账户才能正常使用。
- [x] 用户中心：包括用户信息展示、订单展示、地址管理、浏览记录和余额充值等功能。
3. 购物车管理
- [x] 添加商品：用户可以将商品添加到购物车中。
- [x] 更新商品数量：用户可以更新购物车中商品的数量。
- [x] 删除商品：用户可以删除购物车中的商品。
- [x] 显示购物车：用户可以查看购物车中的商品信息和总价。
4. 订单管理
- [x] 提交订单：用户可以将购物车中的商品提交生成订单。
- [x] 创建订单：系统根据用户提交的订单信息创建订单记录。
- [x] 支付订单：用户可以使用余额支付订单。
- [x] 订单评论：用户可以对已完成的订单进行评论。
------------------------------------------
# 实现效果
1. 主页

![image](https://github.com/user-attachments/assets/471e6311-9a7b-4f1c-91ff-a5596e7d0203)
![image](https://github.com/user-attachments/assets/d9138f9a-f228-4c96-be04-957760dc55bb)

3. 登录/注册页

![image](https://github.com/user-attachments/assets/e090f362-3177-463d-8550-077f88397dcc)
![image](https://github.com/user-attachments/assets/53d16bb5-d141-4381-b20a-da03da297a34)

5. 用户中心

![image](https://github.com/user-attachments/assets/39f6df9e-3292-4300-bb6a-0036e8ae67e2)

7. 订单管理/提交/支付

![image](https://github.com/user-attachments/assets/ee9111a4-233e-495f-acf8-5035b2a3dfc4)
![image](https://github.com/user-attachments/assets/febb8162-7b40-47ef-8f6b-550f39d3c41b)
![image](https://github.com/user-attachments/assets/d4eb5093-cea6-45d6-b4e8-32b29188b3b0)

9. 浏览历史

![image](https://github.com/user-attachments/assets/17e04a4b-2ad9-484e-9a28-c30d16f2d569)

11. 购物车

![image](https://github.com/user-attachments/assets/6be19434-5897-4151-b9ad-64a924a6f27f)

13. 商品详情/评论

![image](https://github.com/user-attachments/assets/5ccf6145-5ff3-4c46-a1eb-b08327577782)
![image](https://github.com/user-attachments/assets/7c672d7b-7250-466c-90ca-8d32c1f0f18e)

------------------------------------------
参考资料：
https://github.com/Eeyhan/onlinestudy
https://github.com/NothinkingGao/django-eshop
https://github.com/Pad0y/Django2_dailyfresh
https://github.com/geeeeeeeek/python_shop
https://blog.csdn.net/qq_41782425/article/details/88790662
https://github.com/pretendwang/Django-dianshang-proje
https://blog.csdn.net/qq_41782425/article/details/88921322
https://blog.csdn.net/geek_xiong/article/details/90324013
https://www.cnblogs.com/zhangyh-blog/p/15239305.html
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
python manage.py shell
<模型名>.objects.all() # 查看模型的所有obejct
<模型名>.objects.all()[0].<键> # 查看模型第一个对象对应的键值
<模型名>.objects.create()
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

# 常用指令
use dongdongqiang;
show tables;
select * from ddq_user \G;
```

insert
delete
mordify
search
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
8. tab+shift: 多行缩进
------------------------------------------
# clergy
```bash
celery -A <celery实例对象> worker -l info -P eventlet # celery运行tasks.py

```
参考博客：
https://blog.csdn.net/m0_56966142/article/details/123801608
------------------------------------------
# redis 远程字典服务
1. 安装
https://download.csdn.net/blog/column/10939729/115372992
2. 常用指令
```bash
redis-cli # 在cmd中使用，进入数据库# 如不指定IP地址和端口，默认连接本机的6379端口
redis-cli -h <IP地址> -p <端口号> # 连接指定的IP地址和端口
select <redis数据库编号> # 选择redis数据库,本项目中为5
keys * # 查看所有的key
hmset <键名_id> 1  

HMSET key field value field value # 设置多个字段，如hmset cart_2 1 4 2 8 
# cart_2：用户 ID 为 2 的购物车。
#1 4：商品 ID 1 的数量为 4。
#2 8：商品 ID 2 的数量为 8
hmlen <键名_id> # 查看键名_id的长度

```
------------------------------------------
# 考点：
mtv-svc
app创建过程
django命令

------------------------------------------
# html：HyperText Markup Language
https://blog.csdn.net/mr_yuanshen/article/details/147668918
1. 知识点
html中字母大小写并不会影响代码效果
<html>: 定义HTML文档的根元素
<head>: 包含文档的元信息，如字符编码、页面标题、CSS 引用等
<title>: 文档的标题
<body>: 文档的主体内容:包含可见的页面内容（文本、图片、链接等）
<div>:divsion(分割、分区)：作为块级容器，用于组织和布局页面内容
<span>: (跨度)作为行内容器，用于在同一行内显示文本或其他元素
<a>:archor(锚点)：用于创建超链接
<img>:image(图像)：用于嵌入图像
<ul>:unordered list(无序列表)：用于创建无序列表
<ol>:ordered list(有序列表)：用于创建有序列表
<li>:list item(列表项)：用于表示无序列表中的项目
<p>: paragraph(段落)：用于表示文本段落
<h1> - <h6>: Heading(标题)：用于表示不同级别的标题
<br>:break(换行)：用于在文本中插入换行符
<hr>:horizontal rule(水平线)：用于插入水平线
<form>:form(表单)：用于创建html表单,用于用户输入
<input>:input(输入)：用于创建表单输入字段
<select>:select(选择)：用于创建下拉框
<option>:option(选项)：用于定义下拉框中的选项
<button>:button(按钮)：用于创建按钮
<table>:table(表格)：用于创建表格
<tr>:table row(表格行)：用于表示表格中的行
<td>:table data(表格数据)：用于表示表格中的单元格
<th>:table header(表格头)：用于表示表格中的表头单元格
<textarea>:textarea(文本区域)：用于创建多行文本输入框
属性缩写：
id:identifier(标识符)：用于标识元素，通常用于JavaScript操作
class:class(类)：用于为元素指定一个或多个CSS类名
style:style(样式)：直接为元素应用 CSS 样式
src:source(源)：用于指定图像、脚本等资源的URL/路径
href:hypertext reference(超文本引用)：用于指定超链接的目标URL
alt:alternative text(替代文本)：为图像提供替代描述（用于无障碍或加载失败时）
title:title(标题)：为元素提供额外的信息（如工具提示）（悬停时显示）
type:type(类型)：指定元素的类型（如input的类型）
name:name(名称)：为元素命名（常用于表单数据提交）
value:value(值)：指定元素的值（如input的输入值）
disabled:disabled(禁用)：禁用元素（使其不可用）
checked:checked(选中)：指定复选框或单选按钮默认选中
selected:selected(选中)：指定下拉选择框中的默认选项
placeholder:placeholder(占位符)：为输入框提供提示文本（在输入前显示）
method:method(方法)：指定表单提交的方式（如GET或POST）
其他：
<!DOCTYPE html>:Document Type（文档类型）：声明 HTML 文档的类型，确保浏览器正确解析页面
meta:Metadata（元数据）：提供关于 HTML 文档的元数据（如字符编码、页面描述等）
charset:Character Set（字符集）：指定 HTML 文档的字符编码（如UTF-8）


