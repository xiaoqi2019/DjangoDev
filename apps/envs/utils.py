# -*- coding: utf-8 -*-
from utils.format_time import format_time

def handle_env(datas):
	datas_list = []
	for item in datas:
		# create_time格式化
		item['create_time'] = format_time(item['create_time'])
		datas_list.append(item)
	return datas_list

