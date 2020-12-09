# -*- coding: utf-8 -*-
import os
import unittest
import HTMLTestRunner

from bases.demo import RunRequest

PWD = os.getcwd()
print(PWD)


"""使用unittest测试框架, 必须继承Testcase"""


class TestRequest(unittest.TestCase):
	"""执行每条测试用例都要执行一遍"""
	def setUp(self) -> None:
		print("This is SetUp")

	"""执行每条测试用例之后都要执行一遍"""
	def tearDown(self) -> None:
		print("This is TearDown")

	"""setupClass为类方法, 每次执行同一个类中的测试方法之前仅执行一次"""
	@classmethod
	def setUpClass(cls) -> None:
		print("This is SetUpClass")

	"""tearDownClass为类方法, 每次执行同一个类中的所有测试方法之后仅执行一次"""
	@classmethod
	def tearDownClass(cls) -> None:
		print("this is tearDownClass")

	def test_1(self):
		print("this is first test")

	def test_2(self):
		print("this is second test")

	def test_3(self):
		print("this is third test")


if __name__ == '__main__':
	# send_post(url, data)
	# run = TestRequest()
	data = {
		'username': 'my_test',
		'password': '123456'
	}

	url = 'http://127.0.0.1:8000/login/'

	print(TestRequest(url, "GET", data).res)

	"""全部测试用例从头执行一遍"""
	# unittest.main()

	"""使用测试套件的方式依次加载测试用例"""
	suite = unittest.TestSuite()
	"""一条一条的测试用例添加"""
	# suite.addTest(TestRequest('test_2'))
	"""同时添加多条测试用例, 两种方式添加"""
	# suite.addTests([TestRequest('test_1'), TestRequest('test_2')])
	# suite.addTests(map(TestRequest, ['test_1', 'test_2']))

	"""通过TestLoader方法加载测试case"""
	"""所述TestLoader类被用来创建类和模块的测试套件。
	通常不需要创建该类的实例。unittest框架提供了一个可以共享的实例unittest.defaultTestLoader"""
	loader = unittest.TestLoader()
	# unittest.defaultTestLoader.discover()

	"""通过遍历路径的方法加载测试case, pattern=test*.py, 必须以test开头, start_dir为顶层目录, 从顶层目录开始依次递归遍历文件"""
	# https://www.cnblogs.com/imyalost/p/9048386.html
	# 如果一个测试文件的名称符合pattern，将检查该文件是否包含 load_tests() 函数，如果 load_tests() 函数存在，则由该函数负责加载本文件中的测试用例。
	# 如果不存在，就会执行loadTestsFromModule()，查找该文件中派生自TestCase 的类包含的 test 开头的方法
	# test_case1 = loader.discover(start_dir=PWD)

	"""通过loader_runner的from name方法加载测试case, 注：名称要写全, 文件名.类名.测试方法名"""
	"""name是一个string，string需要是是这种格式的“module.class.method"""
	test_case1 = loader.loadTestsFromName('request_test.TestRequest.test_1')
	test_case2 = loader.loadTestsFromName('request_test.TestRequest.test_2')

	"""通过loader_runner的Module模块进行test case所在的module"""
	# test_case1 = loader.loadTestsFromModule('request_test')

	"""testCaseClass必须是TestCase的子类（或孙类也行）"""
	# test_case2 = loader.loadTestsFromTestCase('test_1')
	suite.addTests([test_case1, test_case2])

	"""运行测试用例"""
	# runner = unittest.TextTestRunner(verbosity=2)
	"""TextTestRunner中参数verbosity表示测试结果信息复杂度的参数,有三个值0,1,2
	0:静默模式, 只获得总的测试用例数和总的结果
	1:默认模式, 在每个成功的用例前面加个., 每个失败的用例前面有F
	2：详细模式, 测试结果会显示测试用例的所有相关信息"""

	# runner.run(suite)

	report_dir = os.path.join(PWD, 'report')
	report_result = os.path.join(report_dir, 'my_test_report1.html')
	fp = open(report_result, 'wb+')

	"""使用HTMLTestRunner生成测试报告"""
	runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title="我的测试报告", description="用例执行情况")
	runner.run(suite)

	fp.close()
