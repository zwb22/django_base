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
	# render 渲染模板
	# 参数1.request-请求 2.template_name-模板名字 3.context-将视图的数据传递给HTML模板
	# 模拟数据查询
	d_context = {
		'name': '点击有惊喜哦~'
	}
	return render(p_request, 'zwb_book/index.html', context=d_context)