# -*- coding:utf-8 -*-
# @Author: yang
# @File：data_constant.py
# @Time: 2020-12-13
# @IDE: Pycharm
# @Function: Get Constant Data
import os

PWD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEST_DATA_PATH = PWD + os.sep + 'test_datas'
EXCEL_FILE = TEST_DATA_PATH + os.sep + 'InterfaceTestCases.xls'
JSON_FILE = TEST_DATA_PATH + os.sep + 'RequestData.json'
COOKIE_JSON_FILE = TEST_DATA_PATH + os.sep + 'Cookie.json'
RESULT_PATH = PWD + os.sep + 'results'

MAIL_HOST = 'smtp.qq.com'  # 设置服务器
MAIL_USER = '614865872@qq.com'
MAIL_PASSWORD = 'lnwixkqzcvbmbfcc'
SENDER = '614865872@qq.com'
MAIL_LISTS = 'zhaoyang2031@sina.com'


class ConstantVal:
	id = '0'
	model = '1'
	url = '2'
	run = '3'
	request_type = '4'
	cookie = '5'
	case_depend = '6'
	data_depend = '7'
	field_depend = '8'
	request_data = '9'
	expect_result = '10'
	actual_result = '11'
	cmp_result = '12'


def get_id():
	"""获取id"""
	return ConstantVal.id


def get_name():
	return ConstantVal.model


def get_url():
	return ConstantVal.url


def get_run():
	return ConstantVal.run


def get_request_type():
	return ConstantVal.request_type


def get_cookie():
	return ConstantVal.cookie


def get_depend_id():
	return ConstantVal.case_depend


def get_field_depend():
	return ConstantVal.field_depend


def get_data_depend():
	return ConstantVal.data_depend


def get_request_data():
	return ConstantVal.request_data


def get_expect_result():
	return ConstantVal.expect_result


def get_actual_result():
	return ConstantVal.actual_result


def get_cmp_result():
	return ConstantVal.cmp_result
