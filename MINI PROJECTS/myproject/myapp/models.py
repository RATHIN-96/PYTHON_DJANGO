from django.db import models

# Create your models here.

class Leader (models.Model) :
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    place = models.CharField(max_length=50)
    age = models.IntegerField()
    number = models.IntegerField()
    class Meta:
        db_table='Leader table'