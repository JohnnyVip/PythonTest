#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/7/24 15:46
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : email_demo.py
@Software : PyCharm Community
"""
from functools import wraps
from smtplib import SMTP
from email.mime.text import MIMEText
from email.header import Header

class SendMail:
    def __init__(self,subject,content):
        self.SMTP_host = "smtp.163.com"
        self.from_addr = "m18896732932@163.com"
        self.password = "jxc201901"
        self.to_addrs = ["1169214830@qq.com"]
        self.subject = subject
        self.content = content
        # self.log = Logger()
        # self.()send_email

    def send_email(self):
        try:
            email_client = SMTP(self.SMTP_host)  # 初始化 SMTP类，SMTP服务使用的端口号默认为25，这里默认情况，也可自己设置port参数
            email_client.login(self.from_addr, self.password)  # 登陆服务器
            # 以下在下面的结果图片中再具体标出说明
            msg = MIMEText(self.content, 'plain', 'utf-8')  # 可以理解为发送这个邮箱内容的类，这句话主要是设置这个邮件内容
            msg['Subject'] = Header(self.subject, 'utf-8')  # 设置邮箱主题，也就是标题
            msg['From'] = self.from_addr  # 这个是最后显示的邮件的from
            msg['To'] = "".join(self.to_addrs)  # 这个是最后显示的邮件的to
            email_client.sendmail(self.from_addr, self.to_addrs, msg.as_string())  # 发送信息，将msg转换为string
        except Exception as e:
            print('发送失败')
            # self.log.error("邮件发送失败，请检查邮件配置")
        else:
            print('发送成功')
            # self.log.debug("发送成功")
        finally:
            # email_client.quit()  # 退出服务器
            pass

    def __call__(self,func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            self.send_email()
            return func(*args, **kwargs)
        return wrapped_function


@SendMail(subject="email 装饰器测试",content="hello,email装饰器成功了哦！")
def test_func():
    print("test func is running")
    pass


if __name__ == "__main__":
    test_func()


