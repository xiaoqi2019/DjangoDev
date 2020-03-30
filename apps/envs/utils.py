# -*- coding: utf-8 -*-
from utils.format_time import format_time

def handle_env(datas):
	"""
	1:对时间格式化
	:param datas:
	:return:
	"""
	datas_list = []
	for item in datas:
		item['create_time'] = format_time(item['create_time'])
		datas_list.append(item)
	return datas_list

