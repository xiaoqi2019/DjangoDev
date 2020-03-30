# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Testcases
from interfaces.models import Interfaces

# 新建一个接口序列化器，可以创建四个参数：
# 项目名称，接口名称：read_only=True
# 项目id， 接口id：write_only=True
class InterfaceAnotherSerializer(serializers.ModelSerializer):
	project = serializers.StringRelatedField(label='项目名称', help_text='项目名称')
	pid = serializers.IntegerField(write_only=True, label='项目id', help_text='项目id')
	iid = serializers.IntegerField(write_only=True, label='接口id', help_text='接口id')

	class Meta:
		model = Interfaces
		fields = ('name', 'project', 'pid', 'iid')

		extra_kwargs = {
			'name': {
				'read_only': True,
			},
		}

	# 需要校验接口id和项目id是否匹配
	def validate(self, attrs):
		pass


class TestcasesSerializer(serializers.ModelSerializer):
	"""
	用例序列化器
	"""
	interface = InterfaceAnotherSerializer(label='所属项目和接口', help_text='所属项目和接口')

	class Meta:
		model = Testcases
		fields = ('id', 'name', 'include', 'author', 'request', 'interface')

		extra_kwargs = {
			'include': {
				'write_only': True
			},
			'request': {
				'write_only': True
			},
		}

	def create(self, validated_data):
		pass
		# project = validated_data.pop('project_id')
		# validated_data['project'] = project
		# testsuit = Testcases.objects.create(**validated_data)
		# return testsuit

	def update(self, instance, validated_data):
		pass
		# if 'pid' in validated_data:
		# 	pid = validated_data.pop('pid')
		# 	validated_data['project_id'] = pid
		#
		# return super().update(instance, validated_data)


