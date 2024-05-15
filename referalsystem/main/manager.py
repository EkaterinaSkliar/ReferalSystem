from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **exstra_field):
        if not phone_number:
            raise ValueError("The given phone_number must be set")
        user = self.model(phone_number=phone_number,  **exstra_field)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create(phone_number, password, **extra_fields)