from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
	"""视图函数
	：:param request:
	:return:
	"""
	return HttpResponse("<h1>hello,python测开大佬!</h1>")