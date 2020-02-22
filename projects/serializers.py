# -*- coding: utf-8 -*-
from rest_framework import serializers

class ProjectSerializer(serializers.Serializer):
	"""创建项目序列器
	序列化器的作用：
	a.序列化操作 --serialize = ProjectSerializer(instance=one_project)（转成json数据）
	b.反序列化操作 --serialize.data(转成字典)
	"""
	# 1.定义的序列化器，需要继承Serializer或者子类
	# 2. 定义的每一个类属性要与模型类中对应
	# 3.label对应verbose_name
	# 4.默认情况下，定义了哪些属性（序列化器字段），那么就会序列化输出哪些字段和哪些字段需要进行反序列化输入
	# 如果不需要序列化输出，不定义即可
	# 5.如果在定义的字段中，添加write_only=True,那么当前字段只能进行反序列化（数据校验），即只是输入校验不进行输出
	# id = serializers.IntegerField(label='ID', write_only=True)
	name = serializers.CharField(label='项目名称', max_length=200, help_text='项目名称')
	leader = serializers.CharField(label='项目负责人', help_text='项目负责人', max_length=50)
	tester = serializers.CharField(label='测试人员', help_text='测试人员', max_length=50)
	programmer = serializers.CharField(label='开发人员', help_text='开发人员', max_length=50)
	publish_app = serializers.CharField(label='发布应用', help_text='发布应用', max_length=200)
	desc = serializers.CharField(label='简要描述', help_text='简要描述', max_length=200, default='', allow_null=True, allow_blank=True)
