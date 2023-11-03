from django.shortcuts import render, redirect
from gsd.models import Task, User
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm
from .forms import ExampleForm
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.urls import reverse

# Create your views here.

def timetest(request):
    return render(request, 'test.html')
    
def tasklist(request):
    return render(request, 'tasklist.html')

def userstasks(request, username=None):
    if username:
        user = User.objects.filter(username=username).first()
        if user:
            tasks = Task.objects.filter(owner=user)
            return render(request, 'userstasks.html', {'tasks': tasks})
        else:
            return HttpResponse("User not found.")
    else:
        return HttpResponse("No specific task selected.")

@login_required(login_url='views/login')
def frontend_view(request, username = None):
    desired_user = username
    user_data = User.objects.get(username=desired_user)
    return render(request, 'frontend.html', {'user_data':user_data})

def load_content(request):
    content = "This content is loaded dynamically using HTMX!"
    return HttpResponse(content)

def login(request):
    return render(request, 'login.html')

def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, username=email, password=password)

            if user:
                # If the user is authenticated, log them in
                auth_login(request,user )
                print(user )
                redirect_url = reverse('frontend_userstasks', args=[user])
                return HttpResponseRedirect(redirect_url)  # Redirect to the user's page
            else:
                # Handle invalid credentials, display an error message, or return to the login page
                print("nope, no user")
                return render(request, 'login.html', {'form': form, 'error_message': 'Invalid login credentials'})
    else:
        form = LoginForm()
        
    return render(request, 'login.html', {'form': form})
