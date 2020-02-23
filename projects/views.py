import json

from django.http import HttpResponse, JsonResponse, request, Http404

# Create your views here.
from django.views import View
from interfaces.models import Interfaces
from .models import Projects # 导入
from .serializers import ProjectSerializer # 导入序列化类


class ProjectList(View):  # 相同url --get /projects  post /projects
	def get(self, request):
		"""获取项目列表数据
		:param request
		:return:
		"""
		# 从数据库获取所有项目信息
		project_qs = Projects.objects.all()
		# 将模型类对象转化为字典类型，构造嵌套字典的列表
		# project_list = []
		# for project in project_qs:
		# 	project_list.append({
		# 		"id":project.id,
		# 		"name":project.name,
		# 		"leader": project.leader,
		# 		"tester": project.tester,
		# 		"programmer": project.programmer,
		# 		"publish_app":project.publish_app,
		# 		"desc":project.desc
		# 	})
		# 返回多条数据（列表数据）那么many=True
		serialize = ProjectSerializer(instance=project_qs, many=True) #序列化传参需要instance接收参数（接收json格式）
		return JsonResponse(serialize.data, safe=False)

	def post(self, request):
		"""创建一个项目
		:param request:
		:return:"""
		# q1:前端传参，以哪种形式传参-json
		# q2:接收参数转化成python的基本类型&参数校验-校验过程比较复杂，当前省略
		json_data = request.body
		python_data = json.loads(json_data, encoding='utf-8') # 转成字典
		# 1.接收参数（转化为Python中的基本类型&数据校验）
		# 反序列化传参使用data接收参数（接收字典），序列化传参需要instance接收参数（接收json格式）
		# 需要先调用.is_valid()方法，才可以调用.errors()查看错误信息，如果校验正确，那么错误信息为空字典
		# 只有通过序列化器对象调用.is_valid()方法，才可以数据校验（字段参数）
		serialize = ProjectSerializer(data=python_data) # 反序列化传参使用data接收参数（接收字典）
		# 校验方法1
		# if not serialize.is_valid():
		# 	return JsonResponse(serialize.errors, status=400)
		# 校验方法2（常用，代码简介，一个内置参数解决，但是暂时不会抛出异常，需要加一些配置才可以）
		# is_valid()方法中，raise_exception设置为True，那么校验失败后会自动抛出异常，异常信息会被自动处理
		try:
			serialize.is_valid(raise_exception=True)
		except Exception:
			return JsonResponse(serialize.errors, status=400)
		# 向数据库新增项目
		# project_name = python_data["name"]
		# project_leader = python_data["leader"]
		# project_tester = python_data["tester"]
		# project_programmer = python_data["programmer"]
		# project_publish_app = python_data["publish_app"]
		# project_desc = python_data["desc"]

		# 方法1
		# one_project = Projects(name=project_name,
		# 											leader=project_leader,
		#                       tester=project_tester,
		#                        programmer=project_programmer,
		#                        publish_app=project_publish_app,
		#                        desc=project_desc)
		# one_project.save()

		# 方法2--不需要save()
		project = Projects.objects.create(**serialize.validated_data) # 将验证通过后的数据返回
		# project = Projects.objects.create(**python_data)
		# 返回新创建的结果（返回新增项目的数据）
		# one_dict = {
		# 		"id":project.id,
		# 		"name":project.name,
		# 		"leader":project.leader,
		# 		"tester":project.tester,
		# 		"programmer":project.programmer,
		# 		"publish_app":project.publish_app,
		# 		"desc":project.desc
		# }
		serialize = ProjectSerializer(instance=project)
		return JsonResponse(serialize.data, status=201) # 特别注意这里：get方式状态码200，但是post/put/patch需要返回201才算成功；




class ProjectDetail(View):
	def get_object(self, pk):
		try:
			return Projects.objects.get(pk=pk)
		except Projects.DoesNotExist:
			raise Http404
	def get(self, request, pk):
		"""
		获取指定项目的信息
		:param request:
		:param pk:
		:return:
		"""
		# 1.校验PK值
		# 2.获取指定pk值的项目
		one_project = self.get_object(pk)
		# 将模型类对象转化成字段
		# 返回结果
		# one_dict = {
		# 	"id": one_project.id,
		# 	"name": one_project.name,
		# 	"leader": one_project.leader,
		# 	"tester": one_project.tester,
		# 	"programmer": one_project.programmer,
		# 	"publish_app": one_project.publish_app,
		# 	"desc": one_project.desc
		# }

		# 使用序列化类
		serialize = ProjectSerializer(instance=one_project)
		# safe=False只有在返回json格式的数据时需要加，这里one_dict是字典格式不需要加
		return JsonResponse(serialize.data)

	def put(self, request, pk):
		"""
		更新指定项目
		:param request:
		:param pk:
		:return:
		"""
		# 1.校验PK值
		# 2.获取指定pk值的项目
		one_project = self.get_object(pk)
		# 3.q1:前端传参，以哪种形式传参-json
		# q2:接收参数转化成python的基本类型&参数校验-校验过程比较复杂，当前省略
		json_data = request.body
		python_data = json.loads(json_data, encoding='utf-8') # 转成字典
		# 3.更新项目--必须save()
		one_project.name = python_data['name']
		one_project.leader = python_data['leader']
		one_project.tester = python_data['tester']
		one_project.programmer = python_data['programmer']
		one_project.publish_app = python_data['publish_app']
		one_project.desc = python_data['desc']
		one_project.save()
		# 4.返回结果
		# one_dict = {
		# 	"id": one_project.id,
		# 	"name": one_project.name,
		# 	"leader": one_project.leader,
		# 	"tester": one_project.tester,
		# 	"programmer": one_project.programmer,
		# 	"publish_app": one_project.publish_app,
		# 	"desc": one_project.desc}
		serialize = ProjectSerializer(instance=one_project)
		return JsonResponse(serialize.data, status=201) # safe=False只有在返回json格式的数据时需要加，这里one_dict是字典格式不需要加

	def delete(self, request, pk):
		"""
		删除指定项目
		:param request:
		:param pk:
		:return:
		"""
		# 1.校验前端传递的pk值
		# 2.获取指定pk的项目
		one_project = self.get_object(pk)
		# 3.删除项目
		one_project.delete()
		# 4.返回
		return JsonResponse(None, safe=False, status=204)



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