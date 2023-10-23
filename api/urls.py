from django.urls import path
from . import views


app_name = 'api'

urlpatterns =[
    path('', views.test_view, name='example'),
    path('users/', views.UserListView.as_view(), name = 'user_list'),
    path('users/<pk>', views.UserDetailView.as_view(), name ='user_detail'),
    path('tasks/', views.TaskList.as_view(), name = 'task_list'),
    path('tasks/<pk>', views.TaskDetail.as_view(), name='task_detail')
]