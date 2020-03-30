# -*- coding: utf-8 -*-

from django.db.models import Count
from interfaces.models import Interfaces
from testcases.models import Testcases
from testsuits.models import Testsuits
from configures.models import Configures
from utils.format_time import format_time


def get_count_by_project(datas):  # datas为嵌套列表的数据
    """
    1. 通过项目中的接口、用例、配置、套件的数量
    2. 对时间进行格式化
    :param datas:
    :return:
    """
    datas_list = []
    for item in datas:
        item['create_time'] = format_time(item['create_time'])
        project_id = item['id']
        # 用例数集合对象获取
        interfaces_testcases_objs = Interfaces.objects.values('id').annotate(Count('testcases')).\
            filter(project_id=project_id)  # 获取的是每个接口id下面的用例数，列表嵌套字典
        # testcases_sum = 0  # 测试用例数计算方法2
        # for i in interfaces_testcases_objs:
        #     testcases_sum += i['testcases__count']
        interfaces_configures_objs = Interfaces.objects.values('id').annotate(Count('configures')).\
            filter(project_id=project_id)
        # configures_sum = 0  # 配置数计算方法2
        # for j in interfaces_configures_objs:
        #     configures_sum += j['configures__count']
        interfaces_count = Interfaces.objects.filter(project_id=project_id).count()  # 接口数
        testsuits_count = Testsuits.objects.filter(project_id=project_id).count()  # 测试套件数
        item['interfaces'] = interfaces_count
        item['testsuits'] = testsuits_count
        item['testcases'] = sum([i['testcases__count'] for i in interfaces_testcases_objs])
        item['configures'] = sum([j['configures__count'] for j in interfaces_configures_objs])
        datas_list.append(item)
    return datas_list



