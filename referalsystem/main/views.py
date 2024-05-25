import string
import random
import time

from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from .models import User


def user_login(request):
    if request.method == 'POST':
        phone_number = request.POST['username']
        password = request.POST["password"]
        user = authenticate(request,
                            username=phone_number,
                            password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
        else:
            invite_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            new_user = User.objects.create(
                username=phone_number, #костыль
                phone_number=phone_number,
                password=password,
                invite_code=invite_code)
            new_user.set_password = password
            new_user.save()
            login(request, new_user)
            time.sleep(2)
    return render(request, 'registration/code.html')


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
