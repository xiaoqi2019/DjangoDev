from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from . import serializers


class RegisterView(generics.CreateAPIView):
	"""
	注册接口
	"""
	serializer_class = serializers.RegisterSerializer


class UsernameValidateView(APIView):
	"""
	校验用户名
	"""
	def get(self, request, username):
		"""
		获取指定用户名数量
		:param request:
		:param username:
		:return:
		"""
		data_dict = {
			"username": username,
			"count": User.objects.filter(username=username).count()
		}
		return Response(data_dict)


class EmailValidateView(APIView):
	"""
	校验邮箱
	"""

	def get(self, request, email):
		"""
		获取指定用户名数量
		:param request:
		:param username:
		:return:
		"""
		data_dict = {
			"email": email,
			"count": User.objects.filter(email=email).count()
		}
		return Response(data_dict)



