# -*- coding: utf-8 -*-

def format_time(stime):
	"""
	对时间格式化输出
	:param stime:
	:return:
	"""
	time_list = stime.split('T')  #时间格式："2019-11-06T14:50:30.025310+08:00"
	first_part = time_list[0]  # 取年月日
	second_part = time_list[1].split('.')[0]  # 取时分秒
	f_time = first_part + ' ' + second_part  # 新格式时间替换原来的
	return f_time

def modify_output(datas):
	"""
	1:对时间格式化
	:param datas:
	:return:
	"""
	datas_list = []
	for item in datas:
		# if item['create_time']:
		item['create_time'] = format_time(item['create_time'])
		# if item['update_time']:
		item['update_time'] = format_time(item['update_time'])
		datas_list.append(item)
	return datas_list