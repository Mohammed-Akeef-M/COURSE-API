from django.db import models

# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=200)
    price=models.IntegerField(max_length=10)
    Discount=models.CharField(max_length=20)
    Duration=models.CharField(max_length=10)
    Author=models.CharField(max_length=200)
