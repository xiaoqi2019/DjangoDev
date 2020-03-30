import logging
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from .models import Projects
from interfaces.models import Interfaces
from .serializers import ProjectsModelSerializer
from .serializers import ProjectNameSerializer
from rest_framework import permissions
from rest_framework import viewsets
from .utils import get_count_by_project

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
	filter_backends = [DjangoFilterBackend, OrderingFilter]
	filterset_fields = ['name', 'leader', 'tester']
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

	# 获取某个项目的接口列表--定义action尽量使用名词复数
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


	def get_serializer_class(self):
		if self.action == "names":
			return ProjectNameSerializer
		# elif self.action == "interfaces":
		# 	return InterfacesByProjectIdSerializer
		return self.serializer_class

