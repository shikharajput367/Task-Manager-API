from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    
    # Task URLs
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/<int:id>/', views.task_detail, name='task_detail'),
    path('tasks/add/', views.task_add, name='task_add'),
    path('tasks/edit/<int:id>/', views.task_edit, name='task_edit'),
    path('tasks/delete/<int:id>/', views.task_delete, name='task_delete'),
    
    # Admin Panel URL
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    
    # Registration URL
    path('register/<str:token>/', views.register, name='register'),
]
