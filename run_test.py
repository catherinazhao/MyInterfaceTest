# -*- coding:utf-8 -*-
# @Author: yang
# @File：run_test.py
# @Time: 2020-12-13
# @IDE: Pycharm
# @Function:

from bases.run_method import RunMethod
from data.get_data import GetData
from bases.mock_data import mock_demo_data
from data.depend_data import GetDependData


class RunTest(object):
	def __init__(self):
		self.test_datas = GetData()
		self.run = RunMethod()

	def run_test(self):
		sum_cases = self.test_datas.get_cases()
		print(sum_cases)
		for i in range(1, sum_cases):
			res = None
			url = self.test_datas.get_case_url(i)
			is_run = self.test_datas.get_case_is_run(i)
			data = self.test_datas.get_case_json_data(i)
			cookie = self.test_datas.get_case_cookie(i)
			method = self.test_datas.get_case_request_type(i)
			exp_result = self.test_datas.get_case_expect_result(i)
			depend_id = self.test_datas.get_case_is_depend(i)
			# print(1111111111, depend_id)
			# print(i, " ", method, url, is_run, data, cookie)
			if is_run:
				if None != depend_id:
					print(1111111111111)
					depend_datas = GetDependData(depend_id)
					depend_datas.run_depend_case()

				res = mock_demo_data(self.run.run_method, data, url, method, data)
				# res = self.run.run_method(method, url, data, cookie)
				# print(333333333333, res, type(res))
			else:
				res = None


if __name__ == '__main__':
	runner = RunTest()
	runner.run_test()