from django.urls import path
from .views import home, redirect, shorten

urlpatterns = [
    path('', home),
    path('shorten/', shorten, name='shorten'),
    path('<str:link>', redirect, name='redirect'),
]
