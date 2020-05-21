import os
from datetime import datetime

from django.conf import settings
from django.shortcuts import render
# Create your views here.
import logging
from rest_framework.response import Response

from envs.models import Envs
from testcases.models import Testcases
from utils import common
from .serializers import TestsuitsSerializer, TestsuitsRunSerializer
from rest_framework import viewsets, permissions, status
from testsuits.models import Testsuits
from .utils import modify_output, get_testcases_by_interface_ids

logger = logging.getLogger('test')

class TestsuitesViewSet(viewsets.ModelViewSet):
	"""
	list:
	获取测试套件列表数据

	create:
	创建测试套件

	destory:
	删除测试套件

	update:
	更新测试套件

	partial_update:
	部分更新测试套件


	"""
	queryset = Testsuits.objects.all()
	serializer_class = TestsuitsSerializer
	permission_classes = [permissions.IsAuthenticated]
	ordering_fields = ('id', 'name')

	def list(self, request, *args, **kwargs):
		response = super().list(request, *args, **kwargs)
		response.data['results'] = modify_output(response.data['results'])
		return response

	def retrieve(self, request, *args, **kwargs):
		testsuit_obj = self.get_object()
		datas = {
			"name": testsuit_obj.name,
			"project_id": testsuit_obj.project_id,
			"include": testsuit_obj.include,
		}
		return Response(datas)

	def run(self, request, pk=None):
		instance = self.get_object()
		serializer = self.get_serializer(instance, data=request.data)
		serializer.is_valid(raiser_exception=True)
		datas = serializer.validated_data
		env_id = datas.get('env_id')
		env = Envs.objects.get(id=env_id)

		# 创建测试用例所在目录
		testcases_dir_path = os.path.join(settings.SUITES_DIR,
		                                  datetime.strftime(datetime.now(), '%Y%m%d%H%m$S%f'))
		if not os.path.exists(testcases_dir_path):
			os.mkdir(testcases_dir_path)

		include = eval(instance.include)

		if len(include) == 0:
			data_dict = {
				'detail': '此套件下未添加用例，无法运行！'
			}
			return Response(data_dict, status=status.HTTP_400_BAD_REQUEST)

		include = get_testcases_by_interface_ids(include)
		for testcase_id in include:
			testcases_obj = Testcases.objects.filter(id=testcase_id).first()
			if testcases_obj:
				common.generate_testcase_files(testcases_obj, env, testcases_dir_path)

		return common.run_testcase(instance, testcases_dir_path)


	def get_serializer_class(self):
		"""
		不同的action选择不同的序列化器
		:return:
		"""
		return TestsuitsRunSerializer if self.action == 'run' else self.serializer_class

