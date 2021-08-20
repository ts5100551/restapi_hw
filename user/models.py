from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(unique=True)