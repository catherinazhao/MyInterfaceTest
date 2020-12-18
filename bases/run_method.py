# -*- coding:utf-8 -*-
# @Author: yang
# @File：run_method.py
# @Time: 2020-12-13
# @IDE: Pycharm
# @Function: run method
from bases.mock_data import mock_demo_data
import json
import requests


class RunMethod(object):
	"""定义post方法"""
	def post_method(self, url, data, cookie=None):
		res = None
		print(2222222, cookie)
		if cookie:
			"""verify=False: 表示取消安全验证"""
			res = requests.post(url, data=data, cookies=cookie)
		else:
			res = requests.post(url, data=data)

		status_code = res.status_code
		"""cookie只能通过responses.get()方法获取"""
		#print(11111111111111111, res.cookies)
		return res.json()

	"""定义get方法"""
	def get_method(self, url, data=None, cookie=None):
		res = None
		"""
		注：不能写成requests.get(url=url, data=data, cookies=cookie)的形式。
		因为默认方法中没有写默认的key值,所以不能自己添加
		"""
		if cookie:
			res = requests.get(url, data, None)
		else:
			res = requests.get(url, data)
		return res.json()

	"""判定使用post还是get方法"""
	def run_method(self, method, url, data=None, cookie=None):
		res = None
		if method.lower() == 'post':
			res = self.post_method(url, data, cookie)
		else:
			res = self.get_method(url, data, cookie)

		return json.dumps(res, ensure_ascii=False, indent=2, sort_keys=True)
		# return res

