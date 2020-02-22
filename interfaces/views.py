from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from .models import Interfaces


class InterfaceList(View):
	def get(self, request):
		"""
		获取接口列表
		:param request:
		:return:
		"""
		# 获取信息并返回列表，并进行排序
		interfaces = [i for i in Interfaces.objects.filter().values().order_by("project_id")] #Interfaces.objects.filter().values() # 返回的是字典
		# 返回参数
		return JsonResponse(interfaces, safe=False)

	def post(self, request):
		"""
		创建接口
		:param request:
		:return:
		"""
		pass

class InterfaceDetail(View):
	def get(self, request, pk):
		"""
		获取接口详情
		:param request:
		:param pk:
		:return:
		"""
		pass

	def put(self, request, pk):
		"""
		更新接口
		:param request:
		:param pk:
		:return:
		"""

		pass

	def delete(self, request, pk):
		"""
		删除接口
		:param request:
		:param pk:
		:return:
		"""
		pass
