# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Testsuits
from projects.models import Projects

class TestsuitesSerializer(serializers.ModelSerializer):
	project = serializers.StringRelatedField(label='项目名称')


	class Meta:
		model = Testsuits
		fields = ('id', 'name', 'create_time', 'update_time', 'project')


