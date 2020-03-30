# -*- coding: utf-8 -*-
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
router.register(r"projects", views.ProjectsViewSet)
urlpatterns = []
urlpatterns += router.urls # 写法2--常用


