from django.urls import path
from . import views

urlpatterns = [
    
    #path('', views.employees_list, name='employees-list'),
 
    path('create/', views.create_employee, name='create-employee'),
    path('edit/<str:pk>/', views.edit_employee, name='edit-employee'),
    path('delete/<str:pk>/', views.delete_employee, name='delete-employee'),
    path('userlist/', views.user_list, name='user-list'),
    path('usercreate/', views.create_user, name='create-user'),
    path('useredit/<str:pk>/', views.edit_user, name='edit-user'),
    path('userdelete/<str:pk>/', views.delete_user, name='delete-user'),
    path('grouplist/', views.group_list, name='group-list'),
    path('groupcreate/', views.create_group, name='create-group'),
    path('groupedit/<str:pk>/', views.edit_group, name='edit-group'),
    path('groupdelete/<str:pk>/', views.delete_group, name='delete-group'),
    path('usergroupedit/<str:pk>/', views.user_edit_group, name='useredit-group'),
]