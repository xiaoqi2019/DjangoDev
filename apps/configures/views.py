import json

from django.shortcuts import render
from .serializers import ConfiguresSerializer

# Create your views here.

from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.response import Response
from .models import Configures
from interfaces.models import Interfaces
from utils import handle_datas

class ConfiguresViewSet(ModelViewSet):
    """
    list:
    返回debugtalk（多个）列表数据

    update:
    更新（全）debugtalk

    partial_update:
    更新（部分）debugtalk
    """
    queryset = Configures.objects.all()
    serializer_class = ConfiguresSerializer
    permission_classes = [permissions.IsAuthenticated]
    ordering_fields = ('id', 'name')

    def retrieve(self, request, *args, **kwargs):
      config_obj = self.get_object()
      config_request = json.loads(config_obj.request, encoding='utf-8')

      configure_name = config_request['config']['name']
      selected_interface_id = config_obj.interface_id
      selected_project_id = Interfaces.objects.get(id=selected_interface_id).project_id

      # 处理请求头数据
      configure_header = config_request['config']['request'].get('headers')
      configure_header_list = handle_datas.handle_data4(configure_header)

      # 处理全局变量数据
      configure_variables = config_request['config'].get('variables')  # 注意这里最后一个使用get，因为有时候没有这个参数返回None
      configure_variables_list = handle_datas.handle_data2(configure_variables)

      datas = {
        "author": config_obj.author,
        "configure_name": configure_name,
        "selected_interface_id": selected_interface_id,
        "selected_project_id": selected_project_id,
        "header": configure_header_list,
        "globalVar": configure_variables_list
      }

      return Response(datas)


