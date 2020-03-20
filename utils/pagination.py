# -*- coding: utf-8 -*-
from rest_framework.pagination import PageNumberPagination

class ManualPageNumberPagination(PageNumberPagination):
	# 前端用户指定的页面key的名称
	page_query_param = 'page'
	# 前端用户指定的每一条页数key的名称
	page_size_query_param = 'size'
	# 前端指定的每一页最多数据条数（当前不超过100条）
	max_page_size = 20
	# 指定默认每页2条数据
	# page_size = 10