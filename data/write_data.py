# -*- coding:utf-8 -*-
# @Author: yang
# @File：get_data.py
# @Time: 2020-12-15
# @IDE: Pycharm
# @Function: Write Test Result
import json

import xlrd
import xlutils
import time

from xlutils import copy
from util.operation_xls import OperationExcel
from data.data_constant import *


class WriteData(object):
	def __init__(self):
		self.opera_xls = OperationExcel()
		self.workbook = xlrd.open_workbook(self.opera_xls.file_name)
		self.xlu_workbook = xlutils.copy.copy(self.workbook)
		self.table = self.xlu_workbook.get_sheet(self.opera_xls.sheet_index)

	"""写入实际测试结果"""
	def write_case_actul_result(self, row, cmp_res, data):
		self.table.write(row, int(get_actual_result()), json.dumps(data, ensure_ascii=False))
		self.table.write(row, int(get_cmp_result()), cmp_res)
		xls_name = RESULT_PATH + os.sep + self.opera_xls.file_name.split(os.sep)[-1]
		self.xlu_workbook.save(xls_name)




