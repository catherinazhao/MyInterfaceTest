# -*- coding:utf-8 -*-
# @Author: yang
# @File：operation_cookie.py
# @Time: 2020-12-18
# @IDE: Pycharm
# @Function: get cookie info and write cookie json info
import json
import requests
from requests.utils import dict_from_cookiejar
from data.data_constant import *


class OperationCookie(object):
	def __init__(self, res=None):
		if None !=res:
			self.res = res
		else:
			self.res = None

	"""取得cookie的value值"""
	def get_cookie(self):
		if isinstance(self.res, str):
			response = json.loads(self.res)

		url = response['data']['url'][0]

		"""cookie只能通过responses.get()方法获取, 所以必须重新request获取"""
		cookie = requests.get(url).cookies
		# print(22222222222, cookie)
		return cookie

	"""将cookie写入文件"""
	def write_cookie(self):
		cookie_json = dict_from_cookiejar(self.get_cookie())
		print(11111111, cookie_json)
		with open(COOKIE_JSON_FILE, 'w') as f:
			f.write(json.dumps(cookie_json))

	"""从json文件读取cookie内容"""
	def get_json_cookie(self):
		with open(COOKIE_JSON_FILE, 'r') as f:
			content = f.read()
			print(4444444444, json.loads(content))



