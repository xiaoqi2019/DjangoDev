# Create your views here.
from django.views import View
from .models import Interfaces
from django.http import JsonResponse, Http404
from .serializers import InterfaceModelSerializer


class InterfaceList(View):
	def get(self, request):
		"""
		获取接口列表
		:param request:
		:return:
		"""
		# 获取信息并返回列表，并进行排序
		#interfaces = [i for i in Interfaces.objects.filter().values().order_by("project_id")] #Interfaces.objects.filter().values() # 返回的是字典
		# 返回参数
		interface_qs = Interfaces.objects.all()
		serializer = InterfaceModelSerializer(instance=interface_qs, many=True)
		return JsonResponse(serializer.data, safe=False) # 特别注意，这里返回的是列表集合，需要safe=False

	def post(self, request):
		"""
		创建接口
		:param request:
		:return:
		"""
		pass

class InterfaceDetail(View):
	def get_onject(self, pk):
		try:
			return Interfaces.objects.get(pk=pk)
		except Exception:
			raise Http404
	def get(self, request, pk):
		"""
		获取接口详情
		:param request:
		:param pk:
		:return:
		"""
		one_interface = self.get_onject(pk)
		serializer = InterfaceModelSerializer(instance=one_interface)
		return JsonResponse(serializer.data)

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
