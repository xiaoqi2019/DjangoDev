# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Interfaces
from projects.models import Projects

class ProjectModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Projects
		fields = '__all__'

class InterfaceModelSerializer(serializers.ModelSerializer):
	# 会自动化将外键字段生成PrimaryKeyRelatedField类型，返回的是外键表对应的id值
	# project = PrimaryKeyRelatedField(help_text='所属项目', queryset=Projects.objects.all())
	# 会自动调用外键表的__str__方法
	# 子类模型序列化器类会创建子表字段，可以不用创建就可以显示；
	# 方法1-显示接口关联项目的项目名称
	project = serializers.StringRelatedField(label='项目名称')
	# 方法2-接口关联项目的所有字段信息
	# 使用父表的模型序列化器来创建
	# project = ProjectModelSerializer(read_only=True)
	class Meta:
		model = Interfaces
		fields = '__all__'

class InterfaceNameModelSerializer(serializers.ModelSerializer):
	# 接口列表只返回接口id和接口name
	class Meta:
		model = Interfaces
		fields = ("id", "name")
