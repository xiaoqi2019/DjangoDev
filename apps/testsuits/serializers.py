# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Testsuits
from projects.models import Projects

class TestsuitesSerializer(serializers.ModelSerializer):
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
		pass

	def update(self, instance, validated_data):
		pass


