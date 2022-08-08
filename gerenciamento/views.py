from django.shortcuts import HttpResponse, render

def index(request):
    return render(request, 'gen/login.html')
# Create your views here.

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')

def home(request):
    if request.method == "GET":
        return render(request, 'home.html')