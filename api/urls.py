from django.urls import path
from . import views
from .views import *



app_name = 'api'

urlpatterns =[
    path('', views.test_view, name='example'),
    path('users/', views.UserListView.as_view(), name = 'user_list'),
    path('users/<pk>', views.UserDetailView.as_view(), name ='user_detail'),
    path('tasks/', views.AllTaskList.as_view(), name = 'task_list'),
    path('tasks/<pk>', views.TaskDetail.as_view(), name='task_detail'), 
    path('users-tasks/<str:username>', views.UserTasksList.as_view(), name = 'users_tasks')
   

]