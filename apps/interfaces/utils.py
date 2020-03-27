# -*- coding: utf-8 -*-
from testcases.models import Testcases
from configures.models import Configures

def get_count_by_interface(datas):
	"""
	1：返回对接口中用例，配置数量
	2：对时间格式化
	:param datas:
	:return:
	"""
	for item in datas:
		create_time_list = item['create_time'].split('T')
		first_part = create_time_list[0]
		second_part = create_time_list[1].split('.')[0]
		item['create_time'] = first_part + ' ' + second_part
		interface_id = item['id']
		testcases_count = Testcases.objects.filter(interface_id=interface_id).count()
		configures_count = Configures.objects.filter(interface_id=interface_id).count()
		item['testcases'] = testcases_count
		item['configures'] = configures_count
	return datas





