import json

from django.http import HttpResponse, JsonResponse, request, Http404

# Create your views here.
from django.views import View

from django_filters.rest_framework import DjangoFilterBackend # 导入过滤
from rest_framework import status
from rest_framework.filters import OrderingFilter
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from interfaces.models import Interfaces
from .models import Projects # 导入
from .serializers import ProjectModelSerializer # 导入序列化类
from rest_framework.views import APIView
from rest_framework import mixins


# 1.要实现过滤排序分页功能，需要继承DRF中的GenericAPIView
class ProjectList(mixins.ListModelMixin,
                  GenericAPIView):  # 相同url --get /projects  post /projects
	# 往往要指定queryset查询集类属性
	queryset = Projects.objects.all()
	# 往往需要serializer_class指定，要是用的序列化器类
	serializer_class = ProjectModelSerializer
	# filter_backends指定过滤引擎和排序引擎
	# 如果在全局配置变量中指定了，这里无需再次指认
	# filter_backends = [DjangoFilterBackend, OrderingFilter] # 列表，可以些多个过滤引擎
	# pagination_class = [PageNumberPagination] # 指定分页引擎
	# filterset_fields指定可以过滤的字段，只能是模型类定义字段，而且是全匹配，不是模糊匹配
	filterset_fields = ['name', 'leader', 'tester']
	# 指定排序字段，默认使用ordering作为key，指定字段名为value，默认升序，需要降序，字段前加减号
	ordering_fields = ['id', 'name', 'leader'] # 指定排序字段

	# def get(self, request):
	# 	"""获取项目列表数据
	# 	:param request
	# 	:return:
	# 	"""
	# 	# 使用get_queryset方法获取查询集对象
	# 	# project_qs = self.get_queryset() # 查询集对象中有100条项目模型对象
	# 	project_qs = self.filter_queryset(self.get_queryset()) # 过滤之后可能只有20条
	# 	page = self.paginate_queryset(project_qs)
	# 	if page is not None:
	# 		serializer = self.get_serializer(instance=page, many=True)
	# 		return self.get_paginated_response(serializer.data)
	# 	# name = request.query_params.get('name')
	# 	# if name is not None:
	# 	# 	project_qs = project_qs.filter(name_contains=name)
	# 	# 返回多条数据（列表数据）那么many=True
	# 	# 以后获取需要使用的序列化器类，不要用serializer_class,而使用get_serializer()
	# 	serializer = self.get_serializer(instance=project_qs, many=True) #序列化传参需要instance接收参数（接收json格式）
	# 	return Response(serializer.data, status=status.HTTP_200_OK) # safe=False返回只要是非字典都要添加

	def get(self, request):
		return self.list(request)

	def post(self, request):
		"""创建一个项目
		:param request:
		:return:"""
		# q1:前端传参，以哪种形式传参-json
		# q2:接收参数转化成python的基本类型&参数校验-校验过程比较复杂，当前省略
		# json_data = request.body
		# python_data = json.loads(json_data, encoding='utf-8') # 转成字典
		# 继承DRF框架中APIView之后，request是DRF框架中的Request对象
		#
		serializer = ProjectModelSerializer(data=request.data) # 反序列化传参使用data接收参数（接收字典）
		try:
			serializer.is_valid(raise_exception=True)
		except Exception:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		# project = Projects.objects.create(**serialize.validated_data)
		# 创建序列化对象时，给data传参
		# 调用save(),会自动调用create()方法
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProjectDetail(GenericAPIView):
	# 往往要指定queryset查询集类属性
	queryset = Projects.objects.all()
	# 往往需要serializer_class指定，要是用的序列化器类
	serializer_class = ProjectModelSerializer

	def get(self, request, pk):
		"""
		获取指定项目的信息
		:param request:
		:param pk:
		:return:
		"""
		one_project = self.get_object()
		serialize = self.get_serializer(instance=one_project)
		return Response(serialize.data, status=status.HTTP_200_OK)

	def put(self, request, pk):
		"""
		更新指定项目
		:param request:
		:param pk:
		:return:
		"""
		# 1.校验PK值
		# 2.获取指定pk值的项目
		one_project = self.get_object()
		# 3.q1:前端传参，以哪种形式传参-json
		# q2:接收参数转化成python的基本类型&参数校验-校验过程比较复杂，当前省略
		# json_data = request.body
		# python_data = json.loads(json_data, encoding='utf-8') # 转成字典
		serializer = self.get_serializer(data=request.data, instance=one_project)
		try:
			serializer.is_valid(raise_exception=True)
		except Exception:
			raise Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		# 更新项目创建序列化对象时，给instance和data同时传参
		# 调用save(),会自动调用update()方法
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)

	def delete(self, request, pk):
		"""
		删除指定项目
		:param request:
		:param pk:
		:return:
		"""
		# 1.校验前端传递的pk值
		# 2.获取指定pk的项目
		one_project = self.get_object()
		one_project.delete()
		return Response(None, status=status.HTTP_204_NO_CONTENT)



# class IndexView(View):
# def get(self, request):
	# 	# 查询方法
	# 	# 获取一张表中的所有记录
	# 	# 1：调用all()方法返回QuerySet对象
	# 	# 2：QuerySet对象相当于是一个高性能的列表（惰性加载）
	# 	# 3：支持列表的数字索引功能（返回的是一个模型类对象），切片操作（返回依然是模型类对象），不支持负索引
	# 	# 4：QuerySet对象.first（）可以获取第一个元素，.last（）获取最后一个元素
	# 	qs = Projects.objects.all()
	# 	# 二：获取某个指定的记录，使用get()
	# 	# 1：如果没有查询到记录会报错，如果查询到了多条也会报错，只有返回一条记录才不会报错
	# 	# 2：返回的是模型类对象
	# 	# 3：get方法：最好使用主键或者唯一键去查询，避免报错
	# 	one_project = Projects.objects.get(id=1)
	# 	# 三：获取多条记录，使用filter()
	# 	# filter获取不到记录时会返回一个空列表，不会抛异常：一般会返回一个列表集：
	# 	qs = Projects.objects.filter(id=1)
	# 	return HttpResponse("查询项目成功")

	# def get(self, request):
	# 	# 删除方法
	# 	# 方法1：先获取需要更新的模型对象
	# 	# 然后删除
	# 	# one_project = Projects.objects.get(id=9)
	# 	# 也可使用pk--primary key
	# 	one_project = Projects.objects.get(pk=8)
	# 	one_project.delete()
	# 	return HttpResponse("删除成功")

	# def get(self, request):
	# 	# 修改方法
	# 	# 方法1：先获取需要更新的模型对象
	# 	# 然后修改相关属性
	# 	one_project = Projects.objects.get(id=9)
	# 	one_project.tester = "测试02"
	# 	one_project.save()
	# 	return HttpResponse("修改成功")
	#
	# 	# 修改方法2：更新必须所有字段统一更新，用方法1即可：更新的方法2暂时不用；
	# 	# Projects.objects.update()


	# def get(self, request):
	# 	# 创建操作
	# 	# 方法1
	# 	# one_project = Projects(name='国产飞机项目1', leader="XXX院士",tester="测试1",
	# 	#                        programmer="龙的传人",publish_app="国产飞机应用",desc="项目简介")
	# 	# one_project.save()
	#
	# 	# 方法2：
	# 	one_project = Projects.objects.create(name='国产飞机项目4', leader="XXX院士",tester="测试1",
	# 	                       programmer="龙的传人",publish_app="国产飞机应用",desc="项目简介")
	# 	# 关联键方法1
	# 	Interfaces.objects.create(name='国产飞机项目4登陆接口', tester='测试1',project=one_project)
	# 	# 关联键方法2
	# 	# Interfaces.objects.create(name='国产飞机项目4登陆接口',tester='测试1',project_id=one_project.id)
	# 	return HttpResponse("项目创建成功!")

	# def get(self, request):
	# 	data = [
	# 		{
	# 		'project_name':'前程贷项目',
	# 		'leader':'王小二',
	# 		'app_name':'p2p平台应用'
	# 	},
	# 		{
	# 			'project_name': '火星探索项目',
	# 			'leader': '沃克',
	# 			'app_name': '火星探索应用'
	# 		},
	# 		{
	# 			'project_name': 'XX项目',
	# 		 'leader': '乌尔',
	# 		 'app_name': 'xxx应用'
	# 		}
	# 	]
	# 	# 如果data非字典类型，需要加safe=True
	# 	return JsonResponse(data, safe=True)