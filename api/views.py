from rest_framework import generics
from .serializers import UserSerializer, TaskSerializer
from django.shortcuts import render
from django.http import HttpResponse
from gsd.models import User, Task

# Create your views here.
def test_view(request):
    return HttpResponse('Test View')

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetail(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class =TaskSerializer
