from django.urls import path
from app.views import task_list, task_add, task_detail
urlpatterns = [
    path('list/', task_list, name='task-list'),
    path('add/', task_add, name='task-add'),
    path('detail/<int:pk>/', task_detail, name='task-detail'),
]
