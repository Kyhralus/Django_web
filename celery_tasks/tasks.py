from celery import Celery
import time
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DongDongQiang.settings")
django.setup()
"""
添加celery异步发送邮件是为了：

1. 提高响应速度：在 Web 应用等场景中，如果同步发送邮件，用户需要等待邮件发送完成才能进行下一步操作，这会造成较长的等待时间。而使用 Celery 异步发送邮件，应用程序可以在发送邮件后立即响应，将邮件发送任务交给 Celery 在后台处理，用户可以继续进行其他操作，大大提高了应用的响应速度和用户体验。
2. 避免阻塞程序：当发送邮件的操作被阻塞（例如由于网络问题或邮件服务器负载过高）时，如果是同步发送，整个程序都会被阻塞，导致其他任务无法执行。而异步发送邮件可以使程序继续执行其他任务，不会因为邮件发送的问题而影响整个系统的正常运行，提高了系统的稳定性和可靠性。
3. 提高系统并发处理能力：在高并发的情况下，多个用户同时请求发送邮件，如果采用同步方式，可能会导致系统资源紧张，甚至出现崩溃。Celery 可以利用多线程或多进程的方式并行处理多个邮件发送任务，充分利用系统资源，提高系统的并发处理能力，确保系统在高并发场景下也能稳定运行。
4. 实现任务队列管理：Celery 提供了任务队列的功能，可以将邮件发送任务按照一定的顺序进行排队处理。这样可以避免因为同时发送大量邮件而对邮件服务器造成过大压力，还可以方便地对任务进行管理，如查看任务状态、重试失败的任务等。
"""

# broker = 'redis://127.0.0.1/5'      # redis数据库5来执行任务 （厨师）
# backend = 'redis://127.0.0.1/6'     # redis数据库6来存储结果 （前台）
app = Celery("celery_tasks.tasks", broker="redis://127.0.0.1:6379/4") # redis数据库4来执行任务 （厨师）

@app.task(name='send_mail')
def send_active_email(to_email, username, token):
    """发送用户激活邮件"""
    print('开始发送邮件......')
    subject = "天天生鲜欢迎你"  # 邮件标题
    message = ''  # 邮件正文
    sender = settings.EMAIL_FROM  # 发件人
    receiver = [to_email]  # 收件人
    html_message = """
                      <h1>%s  恭喜您成为天天生鲜注册会员</h1><br/><h3>请您在1小时内点击以下链接进行账户激活</h3><a href="http://127.0.0.1:8000/user/active/%s">http://127.0.0.1:8000/user/active/%s</a>
           """ % (username, token, token)
    send_mail(subject, message, sender, receiver, html_message=html_message)
    # 为了体现出celery异步完成发送邮件，这里睡眠5秒
    time.sleep(5)  # 说明之所以睡眠5秒是为了体现celery异步的强大
    print('邮件发送完成......')
    return {"status":"发送成功","email":email}