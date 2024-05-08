from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Import messages
from .forms import RegisterForm, LoginForm

def register_request(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('homepage')  # Ensure this is a valid named URL
    else:
        form = RegisterForm()
    return render(request, 'user_management/register.html', {'form': form})

def login_request(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('homepage')  # Ensure this is a valid named URL
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'user_management/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('homepage')  # Ensure this is a valid named URL
