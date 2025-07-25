from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone =  models.CharField(max_length=12)
    birthday = models.DateField()
    reason = models.CharField(max_length=60)
    avatar = models.ImageField(blank=True)
