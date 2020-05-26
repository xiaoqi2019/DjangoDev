# -*- coding: utf-8 -*-
from rest_framework import serializers

from utils import validates
from .models import Testsuits
from projects.models import Projects

class TestsuitsSerializer(serializers.ModelSerializer):
	"""
	套件序列化器
	"""
	project = serializers.StringRelatedField(label='项目名称', help_text='项目名称')
	project_id = serializers.PrimaryKeyRelatedField(label='项目id', queryset=Projects.objects.all(),
																									write_only=True, help_text='项目id')

	class Meta:
		model = Testsuits
		fields = ('id', 'name','project', 'project_id', 'include', 'create_time', 'update_time')

		extra_kwargs = {
			'create_time': {
				'read_only': True
			},
			'update_time': {
				'read_only': True
			},
			'include': {
				'write_only': True
			},
		}

	def create(self, validated_data):
		project = validated_data.pop('project_id')
		validated_data['project'] = project
		testsuit = Testsuits.objects.create(**validated_data)
		return testsuit

	def update(self, instance, validated_data):
		if 'project_id' in validated_data:
			project = validated_data.pop('project_id')
			validated_data['project'] = project

		return super().update(instance, validated_data)


class TestsuitsRunSerializer(serializers.ModelSerializer):
	"""
	通过测试套件来运行测试用例序列化器
	"""
	env_id = serializers.IntegerField(write_only=True, help_text='环境变量ID',
	                                  validators=[validates.whether_existed_env_id])

	class Meta:
		model = Testsuits
		fields = ('id', 'env_id')


