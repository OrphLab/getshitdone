from django.shortcuts import render
from .models import Task    
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.


class CreateTaskView(CreateView):
    model = Task
    fields = ['name', 'category', 'creation', 'deadline', 'content', 'importance', 'owner']
    template_name = 'task_create.html'
    success_url = reverse_lazy('frontend:dashboard')
    
    def form_valid(self, form):
        form.instance.task_created_by = self.request.user
        return super().form_valid(form)

class UpdateTaskView(UpdateView):
    model = Task
    fields = ['name', 'category', 'creation', 'deadline', 'content', 'importance', 'owner']
    template_name = 'task_update.html'
    success_url = reverse_lazy('frontend:dashboard')

class DeleteTaskView(DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('frontend:dashboard')


