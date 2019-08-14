from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
	path('', views.index, name='index'),
	path('integrantes/', views.integrantes, name='integrantes'),
	path('index/', views.index, name='index'),
	path('cursos/', views.cursos, name='cursos'),	
]