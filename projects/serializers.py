# -*- coding: utf-8 -*-
from rest_framework import serializers
from rest_framework.validators import UniqueValidator # 检验是否唯一
from .models import Projects
from interfaces.models import Interfaces

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

class ProjectModelSerializer(serializers.ModelSerializer):
	# 定义Meta内部类，用于设置当前序列化器类的元数据信息
	# 自带create()和update()方法

	#父类模型序列化器类不会创建子表字段，需要创建才能显示，如下：
	# 子类模型序列化器类会创建子表字段，可以不用创建就可以显示；
	# 如果是按照接口模型类指定的名字：interfaces，下面命名就按照指定的，没有就是interfaces_set
	# 父类关联子类：many=True意思指一个项目下面可能会有多个接口
	interfaces = serializers.StringRelatedField(many=True, read_only=True)

	class Meta:
		# 1.指定参照哪一个模型
		model = Projects
		# 2.指定为模型类的那些字段来生成序列化器字段
		# 3.会将模型类的主键自动添加read_only=True
		# fields = '__all__' # __all__表示输出所有字段
		# fields元祖中指定的是，所有序列化器字段（哪怕模型类中不包含的字段只要在本类定义了也要在fields元祖内指定）
		fields = ('id', 'name', 'leader', 'tester', 'programmer', 'publish_app', 'interfaces')
		# 指定read_only为True的字段
		# read_only_fields = ('desc')
		# 排除不定义的字段--不输出字典
		# exclude = ('create_time','update_time','desc')
		# 如果只是改变某个字段的某个定义值，可以使用extra_kwargs嵌套字典的字典
		extra_kwargs = {
			"name":{
				"min_length":1,
				# "validators":[is_unique_project_name, contain_keyword_project_name]
			}
		}
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

class ProjectNamesModelSerializer(serializers.ModelSerializer):

	class Meta:
		model = Projects
		fields = ("id", "name")

class InterfaceNameModelSerializer(serializers.ModelSerializer):
	# 接口列表只返回接口id和接口name
	class Meta:
		model = Interfaces
		fields = ("id", "name")

# 通过父表获取子表的信息
class InterfacesByProjectIdSerializer(serializers.ModelSerializer):
	interfaces = InterfaceNameModelSerializer(read_only=True, many=True)

	class Meta:
		model = Projects
		fields = ("id", "interfaces")













