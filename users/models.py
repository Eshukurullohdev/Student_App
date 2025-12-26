from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )

    username = None  # ❌ olib tashlaymiz
    email = None     # ❌ majburiy emas

    phone = models.CharField(max_length=15, unique=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, null=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone
