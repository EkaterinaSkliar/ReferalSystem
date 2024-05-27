from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('login/', views.get_sms_code, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('code/', views.sms_code, name='code'),
    path('invite/', views.invite, name='invite'),
    path('home/', views.home, name='home'),
    ]