# -*- coding: utf-8 -*-
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from . import views


urlpatterns = [
	path('login/', obtain_jwt_token),
	path('register/', views.RegisterView.as_view()),
	path('<username>/count/', views.UsernameCountView.as_view()),
	path('<email>/count/', views.EmailCountView.as_view()),
]

