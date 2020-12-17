# -*- coding:utf-8 -*-
# @Author: yang
# @File：depend_data.py
# @Time: 2020-12-14
# @IDE: Pycharm
# @Function: Get Depend Data
"""jsonpath_rw库用来提取接口返回数据json指定字段数据"""
from jsonpath_rw import parse

from util.operation_xls import OperationExcel
from util.operation_json import OperationJson
from data.get_data import GetData
from bases.run_method import RunMethod
from bases.mock_data import mock_demo_data


class GetDependData(object):
	def __init__(self, case_id):
		self.case_id = case_id
		self.opera_xls = OperationExcel()
		self.data = GetData()
		self.run = RunMethod()

	"""取得依赖case对应的行号"""
	def get_case_row_id(self):
		row_id = self.opera_xls.get_row_id(self.case_id)
		# row_datas = self.opera_xls.get_rows_value(row_id)
		#return row_datas
		return row_id

	"""执行依赖case"""
	def run_depend_case(self):
		row_id = self.get_case_row_id()
		url = self.data.get_case_url(row_id)
		method = self.data.get_case_request_type(row_id)
		cookie = self.data.get_case_cols_value(row_id)
		request_datas = self.data.get_case_json_data(row_id)
		response_data = {
			"data": {
				"_input_charset": "utf-8",
				"body": "慕课网订单-1710141907182334",
				"it_b_pay": "1d",
				"notify_url": "http://order.imooc.com/pay/notifyalipay",
				"out_trade_no": "1710141907182334",
				"partner": "2088002966755334",
				"payment_type": "1",
				"seller_id": "yangyan01@tcl.com",
				"service": "mobile.securitypay.pay",
				"sign": "kZBV53KuiUf5HIrVLBCcBpWDg%2FnzO%2BtyEnBqgVYwwBtDU66Xk8VQUTbVOqDjrNymCupkVhlI%2BkFZq1jOr8C554KsZ7Gk7orC9dDbQlpr%2BaMmdjO30JBgjqjj4mmM%2Flphy9Xwr0Xrv46uSkDKdlQqLDdGAOP7YwOM2dSLyUQX%2Bo4%3D",
				"sign_type": "RSA",
				"string": "_input_charset=utf-8&body=慕课网订单-1710141907182334&it_b_pay=1d&notify_url=http://order.imooc.com/pay/notifyalipay&out_trade_no=1710141907182334&partner=2088002966755334&payment_type=1&seller_id=yangyan01@tcl.com&service=mobile.securitypay.pay&subject=慕课网订单-1710141907182334&total_fee=299&sign=kZBV53KuiUf5HIrVLBCcBpWDg%2FnzO%2BtyEnBqgVYwwBtDU66Xk8VQUTbVOqDjrNymCupkVhlI%2BkFZq1jOr8C554KsZ7Gk7orC9dDbQlpr%2BaMmdjO30JBgjqjj4mmM%2Flphy9Xwr0Xrv46uSkDKdlQqLDdGAOP7YwOM2dSLyUQX%2Bo4%3D&sign_type=RSA",
				"subject": "慕课网订单-1710141907182334",
				"total_fee": 299
			},
			"errorCode": 1000,
			"errorDesc": "成功",
			"status": 1,
			"timestamp": 1507979239100
		}

		res = mock_demo_data(self.run.run_method, request_datas, url, method, response_data)
		return res

	"""取得依赖case的依赖字段的内容"""
	def get_depend_data_key(self, key_value):
		depend_res = self.run_depend_case()
		json_expr = parse(key_value)
		match_list = [match.value for match in json_expr.find(depend_res)]
		# print(match_list)
		return match_list[0]


# if __name__ == '__main__':




