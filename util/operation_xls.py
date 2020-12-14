# -*- coding:utf-8 -*-
# @Author: yang
# @File：operation_xls.py
# @Time: 2020-12-13
# @IDE: Pycharm
# @Function: Get xls datas
import xlrd
import os

PWD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXCEL_PATH = PWD + os.sep + 'test_datas' + os.sep + 'InterfaceTestCases.xls'


class OperationExcel(object):
	"""读取excel信息"""
	def __init__(self, dir_path=None, sheet_index=None):
		if None != dir_path:
			self.file_name = dir_path
			self.sheet_index = sheet_index
		else:
			self.file_name = EXCEL_PATH
			self.sheet_index = 0

		self.datas = self.get_excel_datas()

	"""获取制定sheet的内容"""
	def get_excel_datas(self):
		workbook = xlrd.open_workbook(self.file_name)
		table = workbook.sheet_by_index(self.sheet_index)
		# table = workbook.sheets()[self.sheet_index]
		return table

	"""获取列数"""
	@property
	def get_cols(self):
		return self.datas.ncols

	"""获取行数"""
	@property
	def get_rows(self):
		return self.datas.nrows

	"""获取制定单元格内容"""
	def get_cell_value(self, row, col):
		return self.datas.cell_value(row, col)

	"""获取指定列的内容"""
	def get_cols_value(self, col=None):
		if None != col:
			return self.datas.col_values(col)
		else:
			return self.datas.col_values(0)

	"""获取指定行的内容"""
	def get_rows_value(self, row=None):
		if None != row:
			return self.datas.row_values(row)
		else:
			return self.datas.row_values(0)

	"""通过case_id获取该case的行号"""
	def get_row_id(self, case_id):
		for i, val in enumerate(self.get_cols_value()):
			if case_id == val:
				return i
			else:
				continue


if __name__ == '__main__':
	opera_datas = OperationExcel()
	print(opera_datas.get_cols(), opera_datas.get_rows())