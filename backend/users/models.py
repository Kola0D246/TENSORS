from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('Management', 'Management'),
        ('HOD', 'HOD'),
        ('Faculty', 'Faculty'),
        ('Student', 'Student')
    ]
    login_id = models.CharField(primary_key= True, max_length=200)
    password = models.CharField(max_length=200)     # encrypt and salt
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.login_id} ({self.password}) ({self.role})"
