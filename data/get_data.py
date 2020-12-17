# -*- coding:utf-8 -*-
# @Author: yang
# @File：get_data.py
# @Time: 2020-12-13
# @IDE: Pycharm
# @Function: Get data value

from util.operation_json import OperationJson
from util.operation_xls import OperationExcel
from data.data_constant import *


class GetData(object):
	def __init__(self):
		self.opera_excel = OperationExcel(EXCEL_FILE, 0)
		self.opera_json = OperationJson()

	"""取得测试case的总数目"""
	def get_cases(self):
		return self.opera_excel.get_rows

	"""取得测试case的id"""
	def get_case_id(self, row):
		return self.opera_excel.get_cell_value(row, int(get_id()))

	"""取得测试case的描述"""
	def get_case_description(self, row):
		return self.opera_excel.get_cell_value(row, int(get_name()))

	"""取得测试case的接口地址"""
	def get_case_url(self, row):
		return self.opera_excel.get_cell_value(row, int(get_url()))

	"""判定当前测试case是否执行"""
	def get_case_is_run(self, row):
		flag = None
		run_value = self.opera_excel.get_cell_value(row, int(get_run()))
		if run_value.strip().lower() == 'yes':
			flag = True
		else:
			flag = False
		return flag

	"""取得测试case的接口请求类型"""
	def get_case_request_type(self, row):
		return self.opera_excel.get_cell_value(row, int(get_request_type()))

	"""取得测试case的header信息"""
	def get_case_cookie(self, row):
		cookie = self.opera_excel.get_cell_value(row, int(get_cookie()))
		if cookie:
			return cookie
		else:
			return None

	"""取得测试case是否有依赖"""
	def get_case_is_depend(self, row):
		depend_id = self.opera_excel.get_cell_value(row, int(get_depend_id()))
		if depend_id:
			return depend_id
		else:
			return None

	"""取得测试case的依赖key"""
	def get_case_depend_key(self, row):
		depend_key = self.opera_excel.get_cell_value(row, int(get_data_depend()))
		if depend_key:
			return depend_key
		else:
			return None

	"""取得测试case的数据依赖字段"""
	def get_case_field_depend(self,row):
		data_field = self.opera_excel.get_cell_value(row, int(get_field_depend()))
		if data_field:
			return data_field
		else:
			return None

	"""取得测试case的请求数据"""
	def get_case_request_data(self, row):
		return self.opera_excel.get_cell_value(row, int(get_request_data()))

	"""取得测试case的json类型数据"""
	def get_case_json_data(self, row):
		return self.opera_json.get_data(self.get_case_request_data(row))

	"""取得测试case的预期结果"""
	def get_case_expect_result(self, row):
		return self.opera_excel.get_cell_value(row, int(get_expect_result()))

	"""取得测试case的实际结果"""
	def get_case_actual_result(self, row):
		return self.opera_excel.get_cell_value(row, int(get_actual_result()))

	"""取得测试case的判定结果"""
	def get_case_cmp_result(self, row):
		return self.opera_excel.get_cell_value(row, int(get_cmp_result()))

	"""取得指定列的内容"""
	def get_case_cols_value(self, id):
		return self.opera_excel.get_cols_value(id)







if __name__ == '__main__':
	data = GetData()
	data.get_cases()
	print(data.get_case_expect_result(3))
	print(data.get_case_request_data(3))
	print(data.get_case_json_data(3))


