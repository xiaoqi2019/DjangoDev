from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView

from . import serializers


class RegisterView(CreateAPIView):
	"""
	注册接口
	"""
	serializer_class = serializers.RegisterSerializer

class UserNameView(RetrieveAPIView):
	"""
	验证用户名是否存在接口
	"""
	serializer_class = serializers.UsernameSerializer


class EmailView(RetrieveAPIView):
	"""
	验证邮箱是否存在接口
	"""
	serializer_class = serializers.EmailSerializer



