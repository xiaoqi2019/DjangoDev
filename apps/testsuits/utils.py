# -*- coding: utf-8 -*-
from testcases.models import Testcases
from utils.format_time import format_time

def modify_output(datas):
	"""
	1:对时间格式化
	:param datas:
	:return:
	"""
	datas_list = []
	for item in datas:
		item['create_time'] = format_time(item['create_time'])
		item['update_time'] = format_time(item['update_time'])
		datas_list.append(item)
	return datas_list

def get_testcases_by_interface_ids(ids_list):
	"""
	通过接口id获取用例
	:param ids_list:
	:return:
	"""
	one_list = []
	for intreface_id in ids_list:
		testcases_qs = Testcases.objects.values_list('id', flat=True).filter(intreface_id=intreface_id)
		one_list.extend(list(testcases_qs))
	return one_list