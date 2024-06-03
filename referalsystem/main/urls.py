from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.get_sms_code, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('login/code/', views.confirm_sms_code, name='code'),
    path('home/invite/', views.enter_invite_code, name='invite'),
    path('home/', views.home, name='home'),
    ]