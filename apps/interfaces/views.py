import os
from datetime import datetime

from django.conf import settings
from rest_framework.decorators import action
from rest_framework.response import Response

from envs.models import Envs
from utils import common
from .models import Interfaces
from .serializers import InterfacesSerializer, InterfaceRunSerializer
from rest_framework import permissions, status
from rest_framework import viewsets
from .utils import get_count_by_interface
from testcases.models import Testcases
from configures.models import Configures

class InterfacesViewSet(viewsets.ModelViewSet):
	"""
	list:
	获取接口列表数据

	create:
	创建接口

	destroy:
	删除接口

	update:
	完整更新接口

	partial_update:
	部分更新接口

	retrieve:
	获取接口详情数据

	names:
	获取所有接口ID和接口名

	# projects:
	# 获取某个接口下的所有接口信息

	"""
	queryset = Interfaces.objects.all()
	serializer_class = InterfacesSerializer
	permission_classes = [permissions.IsAuthenticated]
	filterset_fields = ['name', 'tester']
	ordering_fields = ('id', 'name')


	def list(self, request, *args, **kwargs):
		response = super().list(request, *args, **kwargs)
		response.data['results'] = get_count_by_interface(response.data['results'])
		return response

	@action(detail=True)
	def teastcases(self, request, pk=None):
		"""
		 Returns a list of all the testcases names by interface id
		"""
		testcase_objs = Testcases.objects.filter(interface_id=pk)
		one_list = []
		for obj in testcase_objs:
			one_list.append({
				"id": obj.id,
				"name": obj.name
			})
		return Response(data=one_list)

	@action(detail=True, url_path='configs')
	def configures(self, request, pk=None):
		"""
		Returns a list of all the configures names by interface id
		"""
		configure_objs = Configures.objects.filter(interface_id=pk)
		one_list = []
		for obj in configure_objs:
			one_list.append({
				"id": obj.id,
				"name": obj.name
			})
		return Response(data=one_list)

	@action(methods=['post'], detail=True)
	def run(self, request, pk=None):
		instance = self.get_object()
		serializer = self.get_serializer(instance, data=request.data)
		serializer.is_valid(raise_exception=True)
		datas = serializer.validated_data
		env_id = datas.get('env_id')  # 获取环境变量env_id
		env = Envs.objects.get(id=env_id)

		# 创建测试用例所在目录名
		testcase_dir_path = os.path.join(settings.SUITES_DIR,
		                                 datetime.strftime(datetime.now(),
		                                                   "%Y%m%d%H%M%S%f"))
		if not os.path.exists(testcase_dir_path):
			os.makedirs(testcase_dir_path)

		testcase_objs = Testcases.objects.filter(interface=instance)
		if not testcase_objs.exists():  # 如果此接口下没有用例, 则无法运行
			data_dict = {"detail": "此接口下无用例, 无法运行!"}
			return Response(data_dict, status=status.HTTP_400_BAD_REQUEST)

		for one_obj in testcase_objs:
			common.generate_testcase_files(one_obj, env, testcase_dir_path)

		# 运行用例
		return common.run_testcase(instance, testcase_dir_path)

	def get_serializer_class(self):
		"""
		不同的action选择不同的序列化器
		:return:
		"""
		return InterfaceRunSerializer if self.action == 'run' else self.serializer_class


