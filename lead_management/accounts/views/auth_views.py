from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

def renderRegisterForm(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Create user (use email as username)
        if User.objects.filter(username=email).exists():
            messages.error(request, "User already exists with this email")
            return redirect('/accounts/register')

        user = User.objects.create_user(
            username=email,   # set username as email
            email=email,
            password=password
        )
        messages.success(request, "Account created successfully! Please login.")
        return redirect('/accounts/login')

    return render(request, 'auth/register.html')


def renderLoginForm(request):
    if request.method == 'POST':
        email = request.POST['email']  # lowercase "email"
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)  # username=email

        if user is not None:
            login(request, user)
            return redirect('/accounts/Dashboard')
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('/accounts/login')

    return render(request, 'auth/login.html')


def forget_password(request):
    return render(request, 'auth/forget.html')
