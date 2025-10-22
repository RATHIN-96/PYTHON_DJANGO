from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User (AbstractUser):
    user_type = models.CharField(max_length=30)
    class Meta:
        db_table = 'USER'


class Department(models.Model):
    department_name = models.CharField(max_length=50)
    class Meta:
        db_table = 'DEPARTMENT'

class Student1(models.Model):
    department_id = models.ForeignKey(Department,on_delete=models.CASCADE)
    stud_id = models.ForeignKey(User,on_delete=models.CASCADE)
    age = models.IntegerField()
    phone = models.BigIntegerField()
    class Meta:
        db_table = 'STUDENT 1'

class Teacher1(models.Model):
    department_id = models.ForeignKey(Department,on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(User,on_delete=models.CASCADE)
    age = models.IntegerField()
    phone = models.BigIntegerField()
    class Meta:
        db_table = 'TEACHER 1'