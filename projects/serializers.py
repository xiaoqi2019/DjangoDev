# -*- coding: utf-8 -*-
from rest_framework import serializers
from rest_framework.validators import UniqueValidator # 检验是否唯一
from .models import Projects

# 创建自定义校验器
def is_unique_project_name(value):
	"""
	自定义校验器-校验项目名命名唯一性
	:param value:
	:return:
	"""
	qs = Projects.objects.filter(name=value)
	if qs:
		raise serializers.ValidationError("项目名称不能重复")

def contain_keyword_project_name(value):
	"""
	自定义校验器-校验项目名是否包含“项目”
	:param value:
	:return:
	"""
	if "项目" not in value:
		raise serializers.ValidationError("项目名命名未包含'项目'")

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
	# 正常情况下id不需要数据校验，不需要输入，可能需要输出
	# 6.如果在定义的字段中，添加read_only=True,那么和write_only=True相反，不进行输入校验，只进行输出
	id = serializers.IntegerField(label='ID', read_only=True)
	# 使用自定义校验器-校验顺序按照校验器列表顺序，每个都要校验（不管前面的失败还是成功）-为了查看所有出错的地方
	name = serializers.CharField(label="项目名称", max_length=200, help_text="项目名称",
	                             validators=[is_unique_project_name, contain_keyword_project_name])
	# name = serializers.CharField(label='项目名称', max_length=200, help_text='项目名称',
	#                              validators=[UniqueValidator(queryset=Projects.objects.all(), message='项目名不能重复')])
	# 可以在序列化字段上，添加自定义抛错信息-error_messages选项（字典，校验选项的字符串为key，具体的报错信息为value）
	leader = serializers.CharField(label='项目负责人', help_text='项目负责人', max_length=50,
	                               error_messages={"max_length":"负责人名称的长度不能超过50个字符串"})
	tester = serializers.CharField(label='测试人员', help_text='测试人员', max_length=50)
	programmer = serializers.CharField(label='开发人员', help_text='开发人员', max_length=50)
	publish_app = serializers.CharField(label='发布应用', help_text='发布应用', max_length=200)
	desc = serializers.CharField(label='简要描述', help_text='简要描述', max_length=200, default='', allow_null=True, allow_blank=True)

	# 对单字段在序列化器内部进行检验,方法命名必须是：validate_字段名
	# 校验顺序：先序列化类外面的校验器-》然后类内部单字段校验-》类内部多字段校验
	# 类内部校验器执行是有要求的，有顺序性：  且必须返回检验参数
	# name字段定义时的校验失败以后，类内部的校验方法不再执行
	# 只有在定义字段时所有校验器成功后，才会调用类内部的validate_字段名校验器
	def validate_name(self, value):
		"""
		校验项目名称是否以项目结尾
		:return:
		"""
		if not value.endswith('项目'):
			raise serializers.ValidationError('项目名称必须以"项目"结尾')
		return value

	def validate(self, attrs):
		"""
		多字段联合校验
		:param attrs: 为前端传递的参数内部构成的字典
		:return:
		"""
		name = attrs["name"]
		leader = attrs["leader"]
		if "领导" not in name and "领导" not in leader:
			raise serializers.ValidationError("项目名称或者负责人中至少有一个包含‘小七’")
		return attrs

	def create(self, validated_data):
		"""
		创建项目
		:param validated_data: 校验通过之后的项目数据
		:return: 项目创建成功之后的模型类对象返回
		"""
		project = Projects.objects.create(**validated_data)
		return project

	def update(self, instance, validated_data):
		"""
		更新项目
		:param instance: 待更新的项目模型类对象
		:param validated_data:
		:return:项目更新成功之后的模型类对象返回
		"""
		# 3.更新项目--必须save()
		instance.name = validated_data['name']
		instance.leader = validated_data['leader']
		instance.tester = validated_data['tester']
		instance.programmer = validated_data['programmer']
		instance.publish_app = validated_data['publish_app']
		instance.desc = validated_data['desc']
		instance.save()
		return instance



