from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.contrib.auth.hashers import make_password



class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, phone_code, phone_number, gender, country, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, phone_code=phone_code,
                          phone_number=phone_number, gender=gender, country=country, **extra_fields)
        user.set_password(password)  # Use set_password to hash the password
        user.save(using=self._db)
        return user


    def create_superuser(self, email, first_name, last_name, phone_code, phone_number, gender, country, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        user = self.create_user(email, first_name, last_name, phone_code, phone_number, gender, country, password, **extra_fields)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone_code = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    country = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)

    groups = models.ManyToManyField(Group, related_name='user_auth_groups')
    user_permissions = models.ManyToManyField(
        Permission, related_name='user_auth_permissions'
    )

    objects = UserManager()