from django.contrib import auth
from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import MyUser
from django.contrib.auth.hashers import make_password

# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('ecom:home')
    else:
        form = {}
        if request.method == 'POST':
            email = request.POST['email']
            username = request.POST['username']
            password = request.POST['pass1']
            password2 = request.POST['pass2']
            form_data = {"email": email, "username": username, "password": password, "password2": password2, }
            form = RegisterForm(form_data)
            if form.is_valid():
                user = MyUser(email=email, password=make_password(password), username=username)
                user.save()
                user = auth.authenticate(email=email, password=password)
                if user is not None:
                    auth.login(request, user)
                    return redirect('ecom:home')
                return redirect('accounts:register')
            else:
                return render(request, 'accounts/register.html', {"form": form})
        return render(request, 'accounts/register.html', {"form": form})


def login(request):
    form = {}
    if request.user.is_authenticated:
        return redirect('ecom:home')
    else:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            user = auth.authenticate(email=email, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('ecom:home')
            else:
                errors = "User name or password is incorrect"
                return render(request, 'accounts/login.html', {"errors": errors})
        return render(request, 'accounts/login.html', {"form": form})


def logout(request):
    auth.logout(request)
    return redirect('ecom:home')
