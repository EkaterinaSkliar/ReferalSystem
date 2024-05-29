import string
import random

from django.contrib.auth import login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.utils import timezone

from .forms import UserForm
from .models import User, SmsCode

SMS_CODE_LIFE_IN_SECONDS = 180


def get_sms_code(request):
    form = UserForm()
    if request.method == 'POST':
        phone_number = request.POST['phone_number']
        code = ''.join(random.choices(string.digits, k=4))
        sms_code = SmsCode.objects.create(
            phone_number=phone_number,
            code=code
        )
        return render(request, 'registration/code.html', {'sms_code': sms_code})
    return render(request, 'registration/login.html', {'form': form})


def confirm_sms_code(request):
    phone_number = request.POST['phone_number']
    sms_code = request.POST['sms_code']
    verify = SmsCode.objects.filter(phone_number=phone_number).latest('date')
    if verify.code == sms_code:
        code_time = timezone.now() - verify.date
        if verify.used == False and code_time.seconds <= SMS_CODE_LIFE_IN_SECONDS:
            verify.used = True
            try:
                user = User.objects.get(phone_number=phone_number)
            except ObjectDoesNotExist:
                invite_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
                user = User.objects.create(
                                    phone_number=phone_number,
                                    invite_code=invite_code)
            login(request, user)
            return render(request, 'main/home.html', {'user': user})
        else:
            error = 'Смс-код устарел'
            return render(request, 'registration/code.html', {'sms_code': verify, 'error': error })
    error = 'Не верный смс-код'
    return render(request,'registration/code.html', {'sms_code': verify, 'error': error})


def invite(request):
    invite = request.POST['invite']
    try:
        user_invite = User.objects.get(invite_code=invite)
    except ObjectDoesNotExist:
        user_invite = None
    return render(request, 'main/home.html')


def logout_view(request):
    logout(request)
    return render(request, 'registration/logout.html')


def home(request):
    return render(request, 'main/home.html')
