# -*- coding: utf-8 -*-
import requests
import json


class RunRequest(object):
	#def __init__(self, url, method, data=None):
	#def __init__(self):
	#	self.res = self.test_run(url, method, data)

	def send_post(self, url, data):
		# 发送post请求
		res = requests.post(url=url, data=data).json()
		return res

	def send_get(self, url, data):
		res = requests.get(url=url, data=data).json()
		print(111111111, res, type(res))
		return res

	def test_run(self, url, method, data):
		result = None
		if method == "GET":
			result = self.send_get(url, data)
		elif method == "POST":
			result = self.send_post(url, data)

		return result


if __name__ == '__main__':
	url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html'
	data = {
		'cart': '11'
	}

	print(RunRequest(url, "GET", data).res)