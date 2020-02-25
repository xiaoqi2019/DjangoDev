from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import GenericAPIView
from .models import Projects
from .serializers import ProjectModelSerializer
from rest_framework import mixins
from rest_framework import generics


# 1.要实现过滤排序分页功能，需要继承DRF中的GenericAPIView
# 先继承mixins的拓展类，需要放在GenericAPIView的前面继承
class ProjectList(generics.ListCreateAPIView):
	queryset = Projects.objects.all()
	serializer_class = ProjectModelSerializer
	filter_backends = [DjangoFilterBackend, OrderingFilter]
	filterset_fields = ['name', 'leader', 'tester']
	ordering_fields = ['id', 'name', 'leader']


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Projects.objects.all()
	serializer_class = ProjectModelSerializer

