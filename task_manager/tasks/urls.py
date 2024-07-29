from django.urls import path
from .views import task_list, task_add, task_edit, task_delete, task_filter_by_priority

urlpatterns = [
    path('', task_list, name='task_list'),
    path('add/', task_add, name='task_add'),
    path('edit/<int:pk>/', task_edit, name='task_edit'),
    path('delete/<int:pk>/', task_delete, name='task_delete'),
    path('filter/<str:priority>/', task_filter_by_priority, name='task_filter_by_priority'),
]
