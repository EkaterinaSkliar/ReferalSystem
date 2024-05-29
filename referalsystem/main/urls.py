from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.get_sms_code, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('code/', views.confirm_sms_code, name='code'),
    path('invite/', views.invite, name='invite'),
    path('home/', views.home, name='home'),
    ]