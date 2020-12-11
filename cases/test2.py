# -*- coding: utf-8 -*-
import requests
import unittest

import json
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


class TestCases(unittest.TestCase):
	"""执行每条测试用例都要执行一遍"""
	def setUp(self) -> None:
		print("This is test2 SetUp")

	"""执行每条测试用例之后都要执行一遍"""
	def tearDown(self) -> None:
		print("This is test2 TearDown")

	"""setupClass为类方法, 每次执行同一个类中的测试方法之前仅执行一次"""
	@classmethod
	def setUpClass(cls) -> None:
		print("This is test2 SetUpClass")

	"""tearDownClass为类方法, 每次执行同一个类中的所有测试方法之后仅执行一次"""
	@classmethod
	def tearDownClass(cls) -> None:
		print("this is test tearDownClass")

	@unittest.skip("skip this case")
	def test_1(self):
		print("this is first test2 test")

	def test_2(self):
		print("this is second test2 test")

	@unittest.skip("skip this case")
	def test_3(self):
		print("this is third test2 test")


	def send_post(self, url, data):
		# 发送post请求
		res = requests.post(url, data)
		return res.json()

	def send_get(self, url, data):
		res = requests.get(url, data)
		return res.json()

	# def run_test(self):


# if __name__ == '__main__':
# 	# send_post(url, data)
# 	#run = TestRequest()
# 	"""全部测试用例从头执行一遍"""
# 	# unittest.main()
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
