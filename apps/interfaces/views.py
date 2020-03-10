import logging
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import Interfaces
from .serializers import InterfaceModelSerializer
from .serializers import InterfaceNameModelSerializer
from rest_framework import mixins, permissions
from rest_framework import generics
from rest_framework import viewsets
# from projects.serializers import ProjectsByProjectIdSerializer

logger = logging.getLogger('test')


class InterfaceViewSet(viewsets.ModelViewSet):
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
	serializer_class = InterfaceModelSerializer
	# 需要分页过滤排序可以加上下面的三行
	filter_backends = [DjangoFilterBackend, OrderingFilter]
	filterset_fields = ['name', 'tester']
	ordering_fields = ['id', 'name']
	# 制定登陆之后才操作接口
	permission_classes = [permissions.IsAuthenticated]


	@action(methods=['get'], detail=False)
	def names(self, request, *args, **kwargs):
		queryset = self.get_queryset()
		serializer = self.get_serializer(instance=queryset, many=True)
		return Response(serializer.data)

	# # 获取某个项目的接口列表
	# @action(detail=True)
	# def projects(self, request, *args, **kwargs):
	# 	instance = self.get_object()
	# 	serializer = self.get_serializer(instance=instance)
	# 	return Response(serializer.data)

	def get_serializer_class(self):
		if self.action == "names":
			return InterfaceNameModelSerializer
		elif self.action == "projects":
			return ProjectsByProjectIdSerializer
		return self.serializer_class

