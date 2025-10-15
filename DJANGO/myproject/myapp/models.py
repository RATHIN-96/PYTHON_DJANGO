from django.db import models

# Create your models here.

class student(models.Model):
    first_name=models.CharField(max_length=30)
    second_name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    age=models.IntegerField()
    class Meta:
        db_table='Student'

class Employee(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=30)
    place=models.CharField(max_length=50)
    age=models.IntegerField()
    