from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import Projects
from .serializers import ProjectModelSerializer
from .serializers import ProjectNamesModelSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets


# 1.要实现过滤排序分页功能，需要继承DRF中的GenericAPIView
# 先继承mixins的拓展类，需要放在GenericAPIView的前面继承
# class ProjectList(generics.ListCreateAPIView):
# 	queryset = Projects.objects.all()
# 	serializer_class = ProjectModelSerializer
# 	filter_backends = [DjangoFilterBackend, OrderingFilter]
# 	filterset_fields = ['name', 'leader', 'tester']
# 	ordering_fields = ['id', 'name', 'leader']
#
#
# class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
# 	queryset = Projects.objects.all()
# 	serializer_class = ProjectModelSerializer

class ProjectViewSet(viewsets.ModelViewSet):
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
	serializer_class = ProjectModelSerializer
	# 需要分页过滤排序可以加上下面的三行
	filter_backends = [DjangoFilterBackend, OrderingFilter]
	filterset_fields = ['name', 'leader', 'tester']
	ordering_fields = ['id', 'name', 'leader']


	@action(methods=['get'], detail=False)
	def names(self, request, *args, **kwargs):
		queryset = self.get_queryset()
		serializer = self.get_serializer(instance=queryset, many=True)
		return Response(serializer.data)

	# 获取某个项目的接口列表
	@action(detail=True)
	def interfaces(self, request, *args, **kwargs):
		pass


	def get_serializer_class(self):
		if self.action == "names":
			return ProjectNamesModelSerializer
		return self.serializer_class

