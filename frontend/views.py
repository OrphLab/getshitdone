from django.shortcuts import render, redirect
from gsd.models import  User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse 
from django.shortcuts import render, get_object_or_404
from .forms import LoginForm
from django.urls import reverse
from django.shortcuts import redirect

# Create your views here.

def timetest(request):
    return render(request, 'test.html')

def taskdetails(request):
    content = "Got it"
    return HttpResponse ((content))    

@login_required(login_url='frontend:login')
def dashboard(request):

    user_data = request.user
    print(user_data)  # Retrieve the user by ID or return a 404 page
    context = {
        'user_data:':user_data, 
        'user_task': user_data.task_set.all
        
    }
    return render(request, 'dashboard.html', context)

def customLoginView(request):
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
                url = reverse('frontend:dashboard', args=[user.id])
                return redirect(url)
            else:
                # Handle invalid credentials, display an error message, or return to the login page
                print("nope, no user")
                return render(request, 'login.html', {'form': form, 'error_message': 'Invalid login credentials'})
    else:
        form = LoginForm()

def load_content(request):
    content = "This content is loaded dynamically using HTMX!"
    return HttpResponse(content)






