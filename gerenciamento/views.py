from django.shortcuts import HttpResponse, render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import auth, messages

def index(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    return render(request, 'login.html')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login_django(request, user)
            return render(request, 'home.html')
        else:
            messages.error(request,'usuário e/ou senha inválida')
            return redirect('login')

@login_required(login_url="/login")
def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    return render (request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

