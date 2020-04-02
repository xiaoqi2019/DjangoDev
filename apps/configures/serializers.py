# -*- coding: utf-8 -*-
from .models import Configures
from rest_framework import serializers
from interfaces.models import Interfaces

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
		"""
		校验项目ID是否与接口ID一致
		:param attrs:
		:return:
		"""
		if not Interfaces.objects.filter(id=attrs['iid'], project_id=attrs['pid']).exists():
			raise serializers.ValidationError('项目和接口信息不对应！')
		return attrs

class ConfiguresSerializer(serializers.ModelSerializer):
	"""
	配置序列化器
	"""
	interface = InterfaceAnotherSerializer(help_text='所属项目和接口')

	class Meta:
		model = Configures
		fields = ('id', 'name', 'author', 'request', 'interface')
		extra_kwargs = {
			'request': {
				'write_only': True
			}
		}

	def create(self, validated_data):
		interface_dict = validated_data.pop('interface')
		validated_data['interface_id'] = interface_dict['iid']
		return Configures.objects.create(**validated_data)

	def update(self, instance, validated_data):
		if 'interface' in validated_data:
			interface_dict = validated_data.pop('interface')
			validated_data['interface_id'] = interface_dict['iid']
		return super().update(instance, validated_data)
