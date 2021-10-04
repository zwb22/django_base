from django.contrib import admin
from django.urls import path

from zwb_book.views import index


urlpatterns = [
    # path(路由名，视图函数名 )
    path('index/', index),
]