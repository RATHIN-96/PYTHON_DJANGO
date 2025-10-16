from django.db import models

# Create your models here.
class stud (models.Model):
    first_name= models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    age=models.IntegerField()
    number=models.IntegerField()
    class Meta:
        db_table='STUDENT DATA'


class employee (models.Model):
    first_name= models.CharField(max_length=20)
    last_name=models.CharField(max_length=20,verbose_name='Sure Name')
    email=models.EmailField(max_length=50)
    age=models.IntegerField()
    number=models.IntegerField()
    class Meta:
        db_table='EMPLOYEE DATA'

class File_Upload(models.Model):
    name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='Uploads/')
    class Meta:
        db_table='UPLOADS'