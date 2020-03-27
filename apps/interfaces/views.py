import logging
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import Interfaces
from .serializers import InterfacesSerializer
from rest_framework import mixins, permissions
from rest_framework import viewsets
from .utils import get_count_by_interface
from testcases.models import Testcases
from configures.models import Configures

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
	serializer_class = InterfacesSerializer
	filter_backends = [DjangoFilterBackend, OrderingFilter]
	filterset_fields = ['name', 'tester']
	ordering_fields = ['id', 'name']
	permission_classes = [permissions.IsAuthenticated]

	def list(self, request, *args, **kwargs):
		response = super().list(request, *args, **kwargs)
		response.data['results'] = get_count_by_interface(response.data['results'])
		return response

	# 获取某个接口的用例列表
	@action(detail=True)
	def teastcases(self, request, pk=None):
		testcase_obj = Testcases.objects.filter(interface_id=pk)
		one_list = []
		for obj in testcase_obj:
			one_list.append({
				"id": obj.id,
				"name": obj.name
			})
		return Response(data=one_list)

	# 获取某个接口的配置列表
	@action(detail=True)
	def configures(self, request, pk=None):
		configure_obj = Configures.objects.filter(interface_id=pk)
		one_list = []
		for obj in configure_obj:
			one_list.append({
				"id": obj.id,
				"name": obj.name
			})
		return Response(data=one_list)


