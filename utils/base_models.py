# -*- coding: utf-8 -*-
from django.db import models

class BaseModel(models.Model):
	"""
	定义公共字段的模型方法
	"""
	# auto_now_add 在新增数据时，会自动添加当前创建的时间（只会添加一次）
	create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间')
	# auto_now 每次更新时，会自动修改更新时间（每次更新都会修改）
	update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间', help_text='更新时间')

	class Meta:
		# 定义为抽象模型-迁移时不会自动创建table表
		abstract = True
		verbose_name = '公共字段'
