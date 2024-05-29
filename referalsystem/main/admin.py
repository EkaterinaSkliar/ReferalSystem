from django.contrib import admin
from .models import User, SmsCode

admin.site.register(User)
admin.site.register(SmsCode)