from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse("Hello")
# Create your views here.
