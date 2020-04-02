# -*- coding: utf-8 -*-
from testcases.models import Testcases
from configures.models import Configures
from utils.format_time import format_time

def get_count_by_interface(datas):
	"""
	1：返回对接口中用例，配置数量
	2：对时间格式化
	:param datas:
	:return:
	"""
	datas_list = []
	for item in datas:
		item['create_time'] = format_time(item['create_time'])
		interface_id = item['id']
		# 计算用例数
		testcase_count = Testcases.objects.filter(interface_id=interface_id).count()
		# 计算配置数
		configure_count = Configures.objects.filter(interface_id=interface_id).count()
		item['testcases'] = testcase_count
		item['configures'] = configure_count
		datas_list.append(item)
	return datas_list





