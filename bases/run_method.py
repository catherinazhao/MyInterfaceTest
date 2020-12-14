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
		print(11111, url)
		print(2222, data)
		print(33333, cookie)
		if cookie:
			"""verify=False: 表示取消安全验证"""
			print(222222222222)
			res = requests.post(url=url, data=data, cookies=None, verify=False)
		else:
			print(1111111111111111111)
			res = requests.post(url=url, data=data, verify=False)

		status_code = res.status_code
		# print(status_code, res.text)
		return res.json()

	"""定义get方法"""
	def get_method(self, url, data, cookie=None):
		res = None
		if cookie:
			res = requests.get(url=url, data=data, cookies=None, verify=False)
		else:
			res = requests.get(url=url, data=data, verify=False)
		return res.json()

	"""判定使用post还是get方法"""
	def run_method(self, method, url, data=None, cookie=None):
		res = None
		print(method, url, data, cookie)
		if method.lower() == 'post':
			res = self.post_method(url, data, cookie)
		else:
			res = self.get_method(url, data, cookie)

		return json.dumps(res, ensure_ascii=False, indent=2, sort_keys=True)
