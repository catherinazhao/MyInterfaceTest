# -*- coding: utf-8 -*-
import requests
import unittest
from unittest import mock

from bases.demo import RunRequest
from bases.mock_data import mock_demo_data

data = {
	'username': 'my_test',
	'password': '123456'
}

url = 'http://127.0.0.1:8000/login/'
url_get = 'http://www.immoc.com/m/web/shizhanapi/loadmorepingjia.html?cart=11'
data_get = {
	'timestamp': '1507006626132',
	'uid': '5249191',
}


"""使用unittest测试框架, 必须继承Testcase"""


class TestMethod(unittest.TestCase):
	"""执行每条测试用例都要执行一遍"""
	def setUp(self) -> None:
		self.run = RunRequest()
		print("This is test1 SetUp")

	"""执行每条测试用例之后都要执行一遍"""
	def tearDown(self) -> None:
		print("This is test1 TearDown")

	"""setupClass为类方法, 每次执行同一个类中的测试方法之前仅执行一次"""
	@classmethod
	def setUpClass(cls) -> None:
		print("This is test1 SetUpClass")

	"""tearDownClass为类方法, 每次执行同一个类中的所有测试方法之后仅执行一次"""
	@classmethod
	def tearDownClass(cls) -> None:
		print("this is test1 tearDownClass")

	def test_1(self):
		print("this is first test1 test")

	def test_2(self):
		print("this is second test1 test")

	def test_3(self):
		print("this is third test1 test")

	def test_send_post(self):
		# 发送post请求
		# res = requests.post(url, data)
		url = 'http://coding.imooc.com/api/cate'
		data = {
			'timestamp': '1507034803124',
			'uid': '5249191',
			'uuid': '5ae7d1a22c82fb89c78f603420870ad7',
			'secrect': '078474b41dd37ddd5efeb04aa591ec12',
			'token': '7d6f14f21ec96d755de41e6c076758dd',
			'cid': '0',
			'errorCode': 1001
		}
		# self.run.test_run = mock.Mock(return_value=data)
		# res = self.run.test_run(url, "POST", data)
		res = mock_demo_data(self.run.test_run, data, url, "POST", data)
		print("Test_send_post", res)
		self.assertEqual(res['errorCode'], 1001, "测试失败")
		# return res

	def test_send_get(self):
		url = 'http://coding.imooc.com/api/cate'
		data = {
			'timestamp': '1507034803124',
			'uid': '5249191',
			'uuid': '5ae7d1a22c82fb89c78f603420870ad7',
			'secrect': '078474b41dd37ddd5efeb04aa591ec12',
			'token': '7d6f14f21ec96d755de41e6c076758dd',
			'cid': '0'
		}

		# res = requests.get(url, data)
		res = self.run.test_run(url, "POST", data)
		print("Test_send_get", res, type(res))
		self.assertEqual(res['errorCode'], 1002, "测试失败")
		# return res

	# def run_test(self):


if __name__ == '__main__':
# 	# send_post(url, data)
# 	#run = TestRequest()
# 	"""全部测试用例从头执行一遍"""
	unittest.main()
#
# 	"""使用测试套件的方式依次加载测试用例"""
# 	suite = unittest.TestSuite()
# 	"""一条一条的测试用例添加"""
# 	# suite.addTest(TestRequest('test_2'))
# 	"""同时添加多条测试用例"""
# 	suite.addTests([TestRequest('test_1'), TestRequest('test_2')])
# 	"""运行测试用例"""
# 	runner = unittest.TextTestRunner()
# 	runner.run(suite)
#
# 	loader = unittest.TestLoader()
# 	loader.discover()
