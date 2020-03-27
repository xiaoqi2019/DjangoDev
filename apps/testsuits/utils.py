# -*- coding: utf-8 -*-
from testsuits.models import Testsuits

def get_count_by_testsuit(datas):
	"""
	1:对时间格式化
	:param datas:
	:return:
	"""
	for item in datas:
		item['create_time'] = format_time(item['create_time'])
		item['update_time'] = format_time(item['update_time'])
	return datas

def format_time(stime):
	"""
	对时间格式化输出
	:param stime:
	:return:
	"""
	create_time_list = stime.split('T')
	first_part = create_time_list[0]
	second_part = create_time_list[1].split('.')[0]
	f_time = first_part + ' ' + second_part
	return f_time



