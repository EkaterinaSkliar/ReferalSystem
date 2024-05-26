from django.contrib.auth import get_user_model
from django.forms import ModelForm


class UserForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['phone_number']