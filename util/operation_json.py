# -*- coding:utf-8 -*-
# @Author: yang
# @File：operation_xls.py
# @Time: 2020-12-13
# @IDE: Pycharm
# @Function: Get Json Test Datas
import os
import json

PWD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JSON_FILE = PWD + os.sep + 'test_datas' + os.sep + 'RequestData.json'


class OperationJson(object):
	"""加载json格式数据"""
	def __init__(self, file_name=None):
		if None != file_name:
			self.json_file = file_name
		else:
			self.json_file = JSON_FILE

		self.json_datas = self.load_json()

	"""读取json文件"""
	def load_json(self):
		fp = open(self.json_file, 'r', encoding='utf-8')
		"""加载文件使用json load的方式"""
		datas = json.load(fp)
		return datas

	"""获取制定id的json数据"""
	def get_data(self, id):
		return self.json_datas[id]


if __name__ == '__main__':
	opera_json = OperationJson()
	print(opera_json.get_data('user'))