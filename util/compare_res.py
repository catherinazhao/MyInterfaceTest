# -*- coding:utf-8 -*-
# @Author: yang
# @File：compare_res.py
# @Time: 2020-12-15
# @IDE: Pycharm
# @Function: compare test results
import json


class CompareResult(object):
	"""比较实际结果与预期结果是否相等"""
	def cmp_data(self, expect, actual):
		# print(type(expect), type(actual))
		# print(expect, actual)
		flag = None
		"""转换为字典格式进行比较两个字典是否相等"""
		if isinstance(expect, str):
			expect = json.loads(expect)

		if isinstance(actual, str):
			actual = json.loads(actual)

		# print(type(expect), type(actual))

		if expect == actual:
			flag = True
		else:
			flag = False

		return flag