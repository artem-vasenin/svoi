from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # phone =  models.TextField(max_length=500, blank=True)
    # birthday = models.CharField(max_length=10, blank=True)
    # reason = models.CharField(max_length=10, blank=True)
    # avatar = models.CharField(max_length=10, blank=True)
