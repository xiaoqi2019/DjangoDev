from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

# from projects.models import Projects # 导入方法1
from interfaces.models import Interfaces
from .models import Projects # 导入方法2（常用）

def index(request):
	"""视图函数
	：:param request:
	:return:
	"""
	return HttpResponse("<h1>hello,python测开大佬!</h1>")

class IndexView(View):
	def get(self, request):
		# 查询方法
		# 获取一张表中的所有记录
		# 1：调用all()方法返回QuerySet对象
		# 2：QuerySet对象相当于是一个高性能的列表（惰性加载）
		# 3：支持列表的数字索引功能（返回的是一个模型类对象），切片操作（返回依然是模型类对象），不支持负索引
		# 4：QuerySet对象.first（）可以获取第一个元素，.last（）获取最后一个元素
		qs = Projects.objects.all()
		# 二：获取某个指定的记录，使用get()
		# 1：如果没有查询到记录会报错，如果查询到了多条也会报错，只有返回一条记录才不会报错
		# 2：返回的是模型类对象
		# 3：get方法：最好使用主键或者唯一键去查询，避免报错
		one_project = Projects.objects.get(id=1)
		# 三：获取多条记录，使用filter()
		# filter获取不到记录时会返回一个空列表，不会抛异常：一般会返回一个列表集：
		qs = Projects.objects.filter(id=1)
		return HttpResponse("查询项目成功")

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