from django.db import models

# Create your models here.
class item(models.Model):
    proname=models.CharField(max_length=50)
    prospec=models.CharField(max_length=50)
    proprice=models.IntegerField(default=0)
    proimg=models.ImageField(upload_to='images/')

class contactdet(models.Model):
    name=models.CharField(max_length=50)
    phone=models.IntegerField(default=0)
    emailid=models.EmailField(max_length=50)