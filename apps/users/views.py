from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from . import serializers


class RegisterView(CreateAPIView):
	"""
	注册接口
	"""
	serializer_class = serializers.RegisterSerializer

