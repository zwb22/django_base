from django.shortcuts import render

# Create your views here.
"""
视图
所谓的视图 其实就是python环境
视图函数有2个要求
	1.视图函数的第一个参数就是接收请求
	2.必须返回一个响应
"""


# p_request
from django.http import HttpRequest
from django.http import HttpResponse


# 期望用户输入http://127.0.0.1:8000/index来访问视图函数
def index(p_request):

	return HttpResponse('ok')