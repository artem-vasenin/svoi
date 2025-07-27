from django.db import models
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone =  models.CharField(max_length=12)
    birthday = models.DateField()
    reason = models.CharField(max_length=60)
    avatar = models.ImageField(blank=True)

class EmailCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        return timezone.now() > self.created_at + timedelta(minutes=10)

