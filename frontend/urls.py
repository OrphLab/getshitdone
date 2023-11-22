from django.urls import path
from . import views
from .views import customLoginView
from django.contrib.auth.views import LogoutView, LoginView
from gsd.views import CreateTaskView, UpdateTaskView, DeleteTaskView


app_name = 'frontend'

urlpatterns =[
    path('test', views.timetest, name='time_test'),
    path('dashboard/', views.dashboard, name ='dashboard'),
    path('login', LoginView.as_view(template_name = 'login.html'), name='login'), 
    path('taksdetails', views.taskdetails, name = 'taskdetails'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('taskcreate/', CreateTaskView.as_view(template_name='task_create.html'), name ='taskcreate'),
    path('taskupdate/<int:pk>', UpdateTaskView.as_view(template_name='task_update.html'), name ='taskupdate'),
    path('taskdelete/<int:pk>', DeleteTaskView.as_view(template_name='task_delete.html'), name ='taskdelete'),
   ]

htmxpatterns  =[
    path('load_content/', views.load_content, name='load_content'),
]

urlpatterns += htmxpatterns