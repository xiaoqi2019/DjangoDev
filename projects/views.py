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
		# 创建操作
		# 方法1
		# one_project = Projects(name='国产飞机项目1', leader="XXX院士",tester="测试1",
		#                        programmer="龙的传人",publish_app="国产飞机应用",desc="项目简介")
		# one_project.save()

		# 方法2：
		one_project = Projects.objects.create(name='国产飞机项目4', leader="XXX院士",tester="测试1",
		                       programmer="龙的传人",publish_app="国产飞机应用",desc="项目简介")
		# 关联键方法1
		Interfaces.objects.create(name='国产飞机项目4登陆接口', tester='测试1',project=one_project)
		# 关联键方法2
		# Interfaces.objects.create(name='国产飞机项目4登陆接口',tester='测试1',project_id=one_project.id)
		return HttpResponse("项目创建成功!")

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