from django.urls import path
from app.views import task_list, task_add, task_detail
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
urlpatterns = [
    path('list/', task_list, name='task-list'),
    path('add/', task_add, name='task-add'),
    path('detail/<int:pk>/', task_detail, name='task-detail'),
     url(r'^logout/$', auth_views.logout, name='logout'),
   
    
]
