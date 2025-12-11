from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm, LoginForm


def register_view(request):
    # Show registration form (do not redirect even if user is authenticated)
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')   # namespace removed
    else:
        form = RegisterForm()
    
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    # Show login view (do not auto-redirect even if user is authenticated)
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Welcome back, {user.first_name or user.username}!')
                
                # Redirect to catalog home after login
                next_page = request.GET.get('next', 'home')
                return redirect(next_page)
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')   # namespace removed


@login_required(login_url='login')   # namespace removed
def profile_view(request):
    context = {
        'user': request.user,
    }
    return render(request, 'accounts/profile.html', context)