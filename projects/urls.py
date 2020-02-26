# -*- coding: utf-8 -*-
from django.urls import path, include
from . import views
from rest_framework import routers

# # 1.创建SimpleRouter路由对象
# router = routers.SimpleRouter()
# D使用efaultRouter会自动创建一个根路径页面
router = routers.DefaultRouter()
# 2.注册路由
# 第一个参数prefix路由前缀（支持正则表达式），一般添加为应用名即可
# 第二个参数为视图集类（只有视图集类才能支持router）
# 第三个参数basename，指定url别名前缀，一般不用
# router.register(r"projects", views.ProjectViewSet, basename='mm')
router.register(r"projects", views.ProjectViewSet)

urlpatterns = [
    # 写法1 3.使用路由对象.urls属性获取路由条目
    # path('', include(router.urls)),
    # 子路由（子应用下创建的路由表）
    # path(
    #   "projects/", views.ProjectViewSet.as_view({
    #         "get": "list",
    #         "post": "create"
    #     })),
    # path("projects/<int:pk>/", views.ProjectViewSet.as_view({
    #         "get": "retrieve",
    #         "put": "update",
    #         "delete": "destroy"
    #     })),
    # path("projects/names/", views.ProjectViewSet.as_view({
    #          "get": "names"})),
    ]
# 写法2--常用
urlpatterns += router.urls

    # path('index_page/',index),
    # # 如果使用类视图，那么path函数的第二个参数为：类视图名.as_view()
    # path('index/',IndexView.as_view()),
    # # 如果要接收路径参数，需要在定义路由时来定义
    # # 路径参数类型转化器（int, slug,uuid）等
    # # pk是路径参数名
    # path('index/<int:pk>/',IndexView.as_view())


