# -*- coding: utf-8 -*-
from django.urls import path
from . import views


urlpatterns = [
    # 子路由（子应用下创建的路由表）
    path("projects/", views.ProjectList.as_view()),
    path("projects/<int:pk>", views.ProjectEdit.as_view())
    # path('index_page/',index),
    # # 如果使用类视图，那么path函数的第二个参数为：类视图名.as_view()
    # path('index/',IndexView.as_view()),
    # # 如果要接收路径参数，需要在定义路由时来定义
    # # 路径参数类型转化器（int, slug,uuid）等
    # # pk是路径参数名
    # path('index/<int:pk>/',IndexView.as_view())

]

