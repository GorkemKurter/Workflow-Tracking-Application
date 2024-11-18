from django.db import models

# Create your models here.

class RegisterModel(models.Model):
    
    Username = models.CharField(max_length = 150)
    Password = models.CharField(max_length = 30)