from django.db import models

# Create your models here.


# 生成迁移脚本  makemigrations 子应用名称（可添加也可不添加）
# 执行迁移脚本  migrate 子应用名称（可添加也可不添加）
# 默认情况下创建的表名为：子应用名_模型类名小写--可以使用内部类修改表名

# 一个数据库模型类相当于一个数据库表，
# 一个类属性相当于一个字段
# 数据库模型类必须继承Model或者Model子类
class Projects(models.Model):
	"""创建Projects模型类"""
	# 默认会创建一个自动递增的id主键
	# 如果手动创建了一个primary_key=True的属性，那么Django就不会自动创建
	# verbose_name 设置更加人性化的字段名
	# help_text 设置字段的描述信息（在api接口文档）
	# unique来设置当前字段是否唯一，默认False
	# max_length 设置限制字段的最大长度
	id = models.AutoField(verbose_name='id主键', primary_key=True, help_text='id主键')
	name = models.CharField(verbose_name='项目名称', help_text='项目名称', unique=True, max_length=100)
	leader = models.CharField(verbose_name='项目负责人', help_text='项目负责人', max_length=50)
	tester = models.CharField(verbose_name='测试人员', help_text='测试人员', max_length=50)
	programmer = models.CharField(verbose_name='开发人员', help_text='开发人员', max_length=50)
	publish_app = models.CharField(verbose_name='发布应用', help_text='发布应用', max_length=200)
	# default 指定默认值
	# blank 设置在创建项目时前端可以不传此字段
	# null 设置数据库此字段允许为空
	desc = models.CharField(verbose_name='简要描述', help_text='简要描述', max_length=200,
	                        default='', blank=True, null=True)
	# auto_now_add 在新增数据时，会自动添加当前创建的时间（只会添加一次）
	create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间')
	# auto_now 每次更新时，会自动修改更新时间（每次更新都会修改）
	update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间', help_text='更新时间')

	# 创建内部类
	# 定义Meta内部类，用于设置当前数据模型元数据信息
	class Meta:
		# 可以在Meta中使用db_table自定义表名
		db_table = 'tb_projects'
		verbose_name = '项目'
