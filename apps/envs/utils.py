# -*- coding: utf-8 -*-
from utils.format_time import format_time

# def handle_env(datas):
# 	datas_list = []
# 	for item in datas:
# 		# create_time格式化
# 		item['create_time'] = format_time(item['create_time'])
# 		datas_list.append(item)
# 	return datas_list


def handle_env(datas):
    datas_list = []
    for item in datas:
        # create_time格式化
        create_time_list = item.get('create_time').split('T')
        first_part = create_time_list[0]
        second_part = create_time_list[1].split('.')[0]
        item['create_time'] = first_part + ' ' + second_part
        datas_list.append(item)
    return datas_list
