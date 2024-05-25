from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('login/auth', views.user_login, name='auth'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('code/', views.sms_code, name='code'),
    path('invite/', views.invite, name='invite'),
    path('', views.home, name='home'),
    ]