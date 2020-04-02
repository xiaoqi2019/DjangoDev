import logging
import os
from datetime import datetime

from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response

from envs.models import Envs
from testcases.models import Testcases
from utils import common
from .models import Projects
from interfaces.models import Interfaces
from .serializers import ProjectsModelSerializer, ProjectsRunSerializer
from .serializers import ProjectNamesSerializer
from rest_framework import permissions
from rest_framework import viewsets
from .utils import get_count_by_project
from rest_framework import status

logger = logging.getLogger('test')


class ProjectsViewSet(viewsets.ModelViewSet):
	"""
	list:
	获取项目列表数据

	create:
	创建项目

	destroy:
	删除项目

	update:
	完整更新项目

	partial_update:
	部分更新项目

	retrieve:
	获取项目详情数据

	names:
	获取所有项目ID和项目名

	interfaces:
	获取某个项目下的所有接口信息

	"""
	queryset = Projects.objects.all()
	serializer_class = ProjectsModelSerializer
	# 需要分页过滤排序可以加上下面的三行
	# filter_backends = [DjangoFilterBackend, OrderingFilter]
	# filterset_fields = ['name', 'leader', 'tester']
	ordering_fields = ['id', 'name', 'leader']
	permission_classes = [permissions.IsAuthenticated]

	def list(self, request, *args, **kwargs):
		response = super().list(request, *args, **kwargs)  # 调用父类修改返回值
		response.data['results'] = get_count_by_project(response.data['results'])
		return response

	@action(methods=['get'], detail=False)
	def names(self, request, *args, **kwargs):
		queryset = self.get_queryset()
		serializer = self.get_serializer(instance=queryset, many=True)
		return Response(serializer.data)

	@action(detail=True)
	def interfaces(self, request, pk=None):
		# 方法1：使用序列化器
		# instance = self.get_object()
		# serializer = self.get_serializer(instance=instance)
		# return Response(serializer.data)
		# 方法2：不适用序列器--返回列表形式
		interface_obj = Interfaces.objects.filter(project_id=pk)
		one_list = []
		for obj in interface_obj:
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
		env_id = datas.get('env_id')
		env = Envs.objects.get(id=env_id)

		# 创建测试用例所在目录名
		testcase_dir_path = os.path.join(settings.SUITES_DIR,
		                                 datetime.strftime(datetime.now(), "%Y%m%d%H%M%S%f"))
		if not os.path.exists(testcase_dir_path):
			os.mkdir(testcase_dir_path)

		interface_objs = Interfaces.objects.filter(project=instance)
		if not interface_objs.exists():  # 如果此项目下没有接口, 则无法运行
			data_dict = {
				"detail": "此项目下无接口, 无法运行!"
			}
			return Response(data_dict, status=status.HTTP_400_BAD_REQUEST)

		for inter_obj in interface_objs:
			testcase_objs = Testcases.objects.filter(interface=inter_obj)

			for one_obj in testcase_objs:
				common.generate_testcase_files(one_obj, env, testcase_dir_path)

		# 运行用例
		return common.run_testcase(instance, testcase_dir_path)





	def get_serializer_class(self):
		"""
		不同的action选择不同的序列化器
		:return:
		"""
		if self.action == 'names':
			return ProjectNamesSerializer
		elif self.action == 'run':
			return ProjectsRunSerializer
		else:
			return self.serializer_class

