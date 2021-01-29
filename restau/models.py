from django.db import models
import uuid
# Create your models here.
from django.forms import UUIDField


class Restaurant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,unique=True)
    direction = models.CharField(max_length=200)
    phone = models.IntegerField()

    def __str__(self):
        return self.name

class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,unique=True)
    type = models.CharField(max_length=20)
    ingredient = models.CharField(max_length=200,default="salt")
    def __str__(self):
        return self.name



