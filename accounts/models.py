from django.contrib.auth.models import AbstractUser
from django.db import models
class User(AbstractUser):
    ROLE_CHOICES = (
        ('RH', 'RH'),
        ('EMPLOYE', 'Employé'),
    )
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='EMPLOYE')
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

# Create your models here.
