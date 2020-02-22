"""DjangoDev03 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# 全局路由配置信息
# 1：urlpatterns为固定名称的列表
# 2：列表中的一个元素，代表一条路由信息
# 3：从上往下匹配，如果可以匹配上，Django会自动调用path函数的第二个参数指定的视图（函数视图）
# 4：如果匹配不上，会自动抛出404异常（默认为404.状态码为404）
# 5：一旦匹配成功，不会继续往下匹配
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('index/',index),
    # 6：如果path函数的第二个参数为include，那么会进入子路由中去匹配
    # include往往第一个参数是字符串，子应用名.urls
    path("",include("projects.urls")),
    path("",include("interfaces.urls"))
]
