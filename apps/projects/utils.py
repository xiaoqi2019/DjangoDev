# -*- coding: utf-8 -*-

from django.db.models import Count

from interfaces.models import Interfaces
from testcases.models import Testcases
from testsuits.models import Testsuits
from configures.models import Configures


def get_count_by_project(datas):  # datas为嵌套列表的数据
    """
    1. 通过项目中的接口、用例、配置、套件的数量
    2. 对时间进行格式化
    :param datas:
    :return:
    """
    for item in datas:
        create_time_list = item.get('create_time').split('T')  #时间格式："2019-11-06T14:50:30.025310+08:00"
        first_part = create_time_list[0]  # 取年月日
        second_part = create_time_list[1].split('.')[0]  # 取时分秒
        item['create_time'] = first_part + ' ' + second_part  # 新格式时间替换原来的
        project_id = item['id']
        # 用例数集合对象获取
        interfaces_testcases_objs = Interfaces.objects.values('id').annotate(Count('testcases')).\
            filter(project_id=project_id)  # 获取的是每个接口id下面的用例数，列表嵌套字典
        testcases_sum = 0
        for i in interfaces_testcases_objs:
            testcases_sum += i['testcases__count']
        # 配置数
        interfaces_configures_objs = Interfaces.objects.values('id').annotate(Count('configures')).\
            filter(project_id=project_id)
        configures_sum = 0
        for j in interfaces_configures_objs:
            configures_sum += j['configures__count']
        # 接口数
        interfaces_count = Interfaces.objects.filter(project_id=project_id).count()
        # 测试条件数
        testsuits_count = Testsuits.objects.filter(project_id=project_id).count()
        item['interfaces'] = interfaces_count
        item['testsuits'] = testsuits_count
        item['testcases'] = testcases_sum
        item['configures'] = configures_sum
    return datas



