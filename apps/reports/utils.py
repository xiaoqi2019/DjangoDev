# -*- coding: utf-8 -*-
from utils.format_time import format_time

def get_count_by_report(datas):
	"""
	1:对时间格式化
	:param datas:
	:return:
	"""
	for item in datas:
		item['create_time'] = format_time(item['create_time'])
	return datas


def get_file_content(filename):
	"""
	读取文件，返回一个生成器对象
	:param filename:
	:return:
	"""
	with open(filename, encoding='utf-8') as f:
		while True:
			line = f.read(512)  # 每次只读512kb,读到文件末尾返回None
			if line:
				yield line  # yield存在，改函数就是生成器对象
			else:  # 如果line为None，那么说明已经读取到文件末尾
				break





