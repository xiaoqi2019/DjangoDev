from django.shortcuts import render
from requests import Response
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from django.contrib.auth.models import User
from . import serializers


class RegisterView(CreateAPIView):
	"""
	注册接口
	"""
	serializer_class = serializers.RegisterSerializer

class UsernameCountView(APIView):
	"""
	验证用户名是否存在
	"""
	def get(self, request, username):
		"""
		获取指定用户名数量
		:param request:
		:param username:
		:return:
		"""
		count = User.objects.filter(username=username).count()
		data = {
			"username": username,
			"count": count
		}
		return Response(data=data)


class EmailCountView(APIView):
	"""
	验证邮箱是否存在
	"""

	def get(self, request, email):
		"""
		获取指定用户名数量
		:param request:
		:param username:
		:return:
		"""
		count = User.objects.filter(username=email).count()
		data = {
			"email": email,
			"count": count
		}
		return Response(data=data)



