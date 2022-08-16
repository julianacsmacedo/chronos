from django.contrib import admin
from django.urls import path, include
from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
EMAIL_HOST = config('EMAIL_HOST', default='localhost')
EMAIL_PORT = config('EMAIL_PORT', default=25, cast=int)

urlpatterns = [
    path('', include('gerenciamento.urls')),
    path('admin/', admin.site.urls),
]
