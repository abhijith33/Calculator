from django.db import models

# Create your models here.

class regmodel(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=20)

