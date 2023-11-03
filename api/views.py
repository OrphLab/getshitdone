from rest_framework import generics
from .serializers import UserSerializer, TaskSerializer
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from gsd.models import User, Task
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
def test_view(request):
    return HttpResponse('Test View')

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserTasksList(generics.ListAPIView):
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        username = self.kwargs.get('username')
        user=User.objects.get(username=username)
        tasks = Task.objects.filter(owner = user)
        return tasks

class AllTaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetail(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class =TaskSerializer

