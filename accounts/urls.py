from django.contrib import admin
from django.contrib.auth import views as authviews
from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', authviews.LoginView.as_view(), name='login'),
    path('logout/', authviews.LogoutView.as_view(), name='logout'),
]
