# -*- coding: utf-8 -*-
from .models import DebugTalks
from rest_framework import serializers

class DebugTalksSerializer(serializers.ModelSerializer):
	"""
	DebugTalks序列化器
	"""
	project = serializers.StringRelatedField(help_text='项目名称')

	class Meta:
		model = DebugTalks
		exclude = ('create_time', 'update_time')
		read_only_fields = ('name', 'project')

		extra_kwargs = {
			'debugtalk': {
				'write_only': True
			}
		}