# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Interfaces
from projects.models import Projects
from utils import validates


class InterfacesSerializer(serializers.ModelSerializer):
	project = serializers.StringRelatedField(label='项目名称', help_text='项目名称')
	project_id = serializers.PrimaryKeyRelatedField(help_text='项目id', queryset=Projects.objects.all(),
																									label='项目id', write_only=True)

	class Meta:
		model = Interfaces
		fields = ('id', 'name', 'tester', 'create_time', 'project', 'project_id', 'desc')

	def create(self, validated_data):
		project = validated_data.pop('project_id')
		validated_data['project'] = project
		interface = Interfaces.objects.create(**validated_data)
		return interface

	def update(self, instance, validated_data):
		if 'project_id' in validated_data:
			project = validated_data.pop('project_id')  # 返回被删除的值-项目名字
			validated_data['project'] = project
		return super().update(instance, validated_data)


class InterfaceNameModelSerializer(serializers.ModelSerializer):
	# 接口列表只返回接口id和接口name
	class Meta:
		model = Interfaces
		fields = ("id", "name")

		extra_kwargs = {
			'create_time': {
				'read_only': True
			},
	}

class InterfaceRunSerializer(serializers.ModelSerializer):
    """
    通过接口来运行测试用例序列化器
    """
    env_id = serializers.IntegerField(write_only=True,
                                      help_text='环境变量ID',
                                      validators=[validates.whether_existed_env_id])

    class Meta:
        model = Interfaces
        fields = ('id', 'env_id')
