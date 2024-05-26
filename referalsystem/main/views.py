import string
import random

from django.contrib.auth import login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from .forms import UserForm
from .models import User


def user_login(request):
    form = UserForm()
    if request.method == 'POST':
        phone_number = request.POST['phone_number']
        try:
            user = User.objects.get(phone_number=phone_number)
            if user is not None:
                if user.is_active:
                    login(request, user)
                return render(request, 'registration/code.html')
        except ObjectDoesNotExist:
            invite_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            new_user = User.objects.create(
                phone_number=phone_number,
                invite_code=invite_code)
            new_user.save()
            login(request, new_user)
            return render(request, 'registration/code.html')
    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'registration/logout.html')


def sms_code(request):
    return home(request)


def invite(request):
    invite = request.POST['invite']
    try:
        user_invite = User.objects.get(invite_code=invite)
    except ObjectDoesNotExist:
        user_invite = None
    return render(request, 'main/home.html')


def home(request):
    return render(request, 'main/home.html', {})
