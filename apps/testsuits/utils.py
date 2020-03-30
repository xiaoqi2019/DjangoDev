# -*- coding: utf-8 -*-
from testsuits.models import Testsuits
from utils.format_time import format_time

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



