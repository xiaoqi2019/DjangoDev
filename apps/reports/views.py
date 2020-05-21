import json
import os
from django.shortcuts import render
from django.conf import settings
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from .serializers import ReportsSerializer
from rest_framework import permissions, mixins
from rest_framework.response import Response
from django.http import StreamingHttpResponse  # 如果要返回文件流必须用这个
from django.utils.encoding import escape_uri_path

from .models import Reports
from .utils import format_output
from .utils import get_file_content
# Create your views here.

class ReportsViewSet(mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
	"""
	list:
	获取报告列表数据

	retrieve:
	创建报告详情

	destory:
	删除报告
	"""
	queryset = Reports.objects.all()
	serializer_class = ReportsSerializer
	permission_classes = (permissions.IsAuthenticated,)
	ordering_fields = ('id', 'name')

	def list(self, request, *args, **kwargs):
		response = super().list(request, *args, **kwargs)
		response.data['results'] = format_output(response.data['results'])
		return response

	@action(detail=True)
	def download(self, *args, **kwargs):
		# 手动创建报告
		instance = self.get_object()
		html = instance.html
		# 选择报告路径
		report_path = settings.REPORTS_DIR
		report_full_path = os.path.join(report_path, instance.name) + '.html'
		with open(report_full_path, 'w', encoding='utf-8') as file:
			file.write(html)
		# 2.读取创建的报告并返回给前端
		response = StreamingHttpResponse(get_file_content(report_full_path))
		# 对文件名进行转义
		report_path_final = escape_uri_path(instance.name + '.html')
		# 如果要提供前端用户能够下载文件，那么需要在响应头中添加如下字段
		response['Content-Type'] = 'application/octet-stream'
		response['Content-Disposition'] = F"attachment; filename*=UTF-8''{report_path_final}"
		return response

	def retrieve(self, request, *args, **kwargs):
		instance = self.get_object()
		serializer = self.get_serializer(instance)
		datas = serializer.data
		try:
			datas['summary'] = json.loads(datas['summary'], encoding='utf-8')
		except Exception as e:
			pass
		return Response(datas)



