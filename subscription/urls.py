from django.urls import path

from . import views

app_name = 'subscription'

urlpatterns = [
    path('', views.home, name='home'),
]