from django.db import models

# Create your models here.



class User(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone_code = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    country = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
