from django.db import models

# Create your models here.

class customer(models.Model):
    name=models.CharField(max_length=200,null=True)
    address=models.CharField(max_length=250)
    mobilenumber=models.CharField(max_length=100)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    def __str__(self):
        return self.name
    