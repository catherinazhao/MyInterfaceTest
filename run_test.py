# -*- coding:utf-8 -*-
# @Author: yang
# @File：run_test.py
# @Time: 2020-12-13
# @IDE: Pycharm
# @Function: Main Method

from bases.run_method import RunMethod
from data.get_data import GetData
from bases.mock_data import mock_demo_data
from data.depend_data import GetDependData
from util.compare_res import CompareResult
from data.write_data import WriteData
from util.send_mail import SendMail


class RunTest(object):
	def __init__(self):
		self.test_datas = GetData()
		self.run = RunMethod()
		self.write_data = WriteData()

	def run_test(self):
		sum_cases = self.test_datas.get_cases()
		print(sum_cases)
		pass_cases = []
		fail_cases = []
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
					depend_key = self.test_datas.get_case_depend_key(i)
					depend_field = self.test_datas.get_case_field_depend(i)

					depend_datas = GetDependData(depend_id)
					data_key = depend_datas.get_depend_data_key(depend_key)
					data[depend_field] = data_key
				res = mock_demo_data(self.run.run_method, data, url, method, data)
				# res = self.run.run_method(method, url, data, cookie)
				cmp_res = CompareResult().cmp_data(exp_result, res)
				if cmp_res:
					self.write_data.write_case_actul_result(i, "PASS", res)
					pass_cases.append(i)
				else:
					self.write_data.write_case_actul_result(i, "FAIL", res)
					fail_cases.append(i)

		SendMail().send_mail(pass_cases, fail_cases)





if __name__ == '__main__':
	runner = RunTest()
	runner.run_test()