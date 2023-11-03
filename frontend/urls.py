from django.urls import path
from . import views

urlpatterns =[
    path('', views.timetest, name='time_test'),
    path('views/tasklist', views.tasklist, name ='tasklist'),
    path('views/tasklist/<str:username>', views.userstasks, name ='userstasks'),
    path('views/tasklist/frontend/<str:username>', views.frontend_view, name ='frontend_userstasks'),
    path('views/login', views.loginView, name='userlogin'), 
    
    
   ]

htmxpatterns  =[
    path('load_content/', views.load_content, name='load_content'),
]

urlpatterns += htmxpatterns