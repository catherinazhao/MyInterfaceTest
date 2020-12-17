# -*- coding:utf-8 -*-
# @Author: yang
# @File：send_mail.py
# @Time: 2020-12-16
# @IDE: Pycharm
# @Function: Post Test Result
import smtplib
"""email库为邮件格式组织服务"""
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

from data.data_constant import *

"""邮箱注意要开启SMTP服务,否则无法发送邮件"""


class SendMail(object):
	# def __init__(self):
	def send_mail(self, pass_cases, fail_cases):
		pass_num = float(len(pass_cases))
		fail_num = float(len(fail_cases))
		sum = float(pass_num + fail_num)

		pass_rate = '%.2f%%' %((pass_num/sum)*100)
		fail_rate = '%.2f%%' %((fail_num/sum)*100)

		subject = 'Python SMTP 邮件测试'
		content = '如下是接口测试报告, 测试case共%s, 通过%s, 未通过%s' % (sum, pass_num, fail_num)

		"""三个参数：1：邮件文本内容, 2:设置文本格式, 3: 设置编码格式：utf-8"""
		message = MIMEText(content, _subtype='plain', _charset='utf-8')
		message['From'] = formataddr(["FromTest", SENDER])  # 发送者
		message['To'] = formataddr(["ToTest", MAIL_LISTS]) # 接收者
		message['Subject'] = Header(subject, 'utf-8')

		try:
			"""smtp为简单邮件传输协议"""
			smtp_obj = smtplib.SMTP()
			smtp_obj.connect(MAIL_HOST, 25)  # 连接到服务

			smtp_obj.login(MAIL_USER, MAIL_PASSWORD)  # 登录到邮箱服务
			smtp_obj.sendmail(SENDER, MAIL_LISTS, message.as_string())
			print("发送邮件成功")
			smtp_obj.close()
		except smtplib.SMTPException as e:
			print("Error: It is failed to Send Email! Error is:", e)



