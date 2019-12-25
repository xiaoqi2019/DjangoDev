from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


def index(request):
	"""视图函数
	：:param request:
	:return:
	"""
	return HttpResponse("<h1>hello,python测开大佬!</h1>")

class IndexView(View):
	def get(self, request):
		data = [
			{
			'project_name':'前程贷项目',
			'leader':'王小二',
			'app_name':'p2p平台应用'
		},
			{
				'project_name': '火星探索项目',
				'leader': '沃克',
				'app_name': '火星探索应用'
			},
			{
				'project_name': 'XX项目',
			 'leader': '乌尔',
			 'app_name': 'xxx应用'
			}
		]
		# 如果data非字典类型，需要加safe=True
		return JsonResponse(data, safe=True)