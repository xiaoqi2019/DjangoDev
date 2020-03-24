# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Interfaces
from projects.models import Projects


class InterfaceModelSerializer(serializers.ModelSerializer):
	project = serializers.StringRelatedField(label='项目名称')
	project_id = serializers.PrimaryKeyRelatedField(help_text='项目id', queryset=Projects.objects.all(),
																									label='项目id', write_only=True)

	class Meta:
		model = Interfaces
		fields = ('id', 'name', 'tester', 'create_time', 'project', 'project_id', 'desc')

	def create(self, validated_data):
		pass

	def update(self, instance, validated_data):
		pass


class InterfaceNameModelSerializer(serializers.ModelSerializer):
	# 接口列表只返回接口id和接口name
	class Meta:
		model = Interfaces
		fields = ("id", "name")
