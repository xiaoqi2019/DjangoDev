from django.db import models
from utils.base_models import BaseModel

# Create your models here.
class Testcases(BaseModel):
	id = models.AutoField('id主键', primary_key=True, help_text='id主键')
	name = models.CharField('用例名称', max_length=50, help_text='用例名称', unique=True)
	interface = models.ForeignKey('interfaces.Interfaces', on_delete=models.CASCADE,
																	help_text='所属接口')
	# TextField为长文本，null=True只有的用例不需要前置用例
	include = models.TextField('前置', null=True, help_text='用例执行前置顺序')
	author = models.CharField('编写人员', max_length=50, help_text='编写人员')
	request = models.TextField('请求信息', help_text='请求信息')

	class Meta:
		db_table = 'tb_testcases'
		verbose_name = '用例信息'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name

