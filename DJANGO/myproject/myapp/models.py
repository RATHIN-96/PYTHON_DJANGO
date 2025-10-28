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
    
class File_Upload(models.Model):
    name = models.CharField(max_length=40)
    photo = models.ImageField(upload_to='uploads/')
    class Meta:
        db_table='FILE UPLOAD'

class Teacher(models.Model):
     first_name=models.CharField(max_length=30)
     last_name=models.CharField(max_length=30)
     age=models.IntegerField()
     email=models.EmailField(max_length=50)
    
class Stud(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()

    def __str__(self):
        return self.name
