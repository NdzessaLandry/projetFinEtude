from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    grade=models.CharField(max_length=50,null=True, blank=True)
    
# Create your models here.
