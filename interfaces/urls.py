# -*- coding: utf-8 -*-
from django.urls import path
from . import views


urlpatterns = [
    # 子路由（子应用下创建的路由表）
    path("interfaces/", views.InterfaceList.as_view()),
    path("interfaces/<int:pk>/", views.InterfaceDetail.as_view())
]

