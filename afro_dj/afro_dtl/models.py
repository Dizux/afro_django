from django.db import models

# Create your models here.
class UserAccount(models.Model):
    username = models.CharField(max_length=22)
    email = models.CharField(max_length=30)
    gender = models.CharField(max_length=6)
    password = models.CharField(max_length=22)
    signuptime = models.DateTimeField(auto_now=True)
