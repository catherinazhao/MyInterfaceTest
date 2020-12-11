# -*- coding:utf-8 -*-
from unittest import mock


"""模拟接口返回数据"""


def mock_demo_data(mock_method, request_data, url, method_type, response_data):
	"""用return_data来模拟接口的返回数据"""
	mock_method = mock.Mock(return_value=response_data)
	mock_res = mock_method(url, method_type, request_data)
	print(mock_res)
	return mock_res
