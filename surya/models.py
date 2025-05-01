from django.db import models

# Create your models here.

class Datas(models.Model):
    Name=models.CharField(max_length=20,default="")
    Phone = models.IntegerField(default="")
    Email = models.EmailField(max_length=50,default="")
    EventDate = models.DateField(max_length=15,default="")
    Venue = models.CharField(max_length=100,default="")
    TypeofEvent = models.CharField(max_length=100,default="")
    Messege = models.CharField(max_length=200,default="")
