from django.db import models

# Create your models here.


class booking(models.Model):
    Name = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    Quandity = models.CharField(max_length=10)
    Order_Date = models.DateField(auto_now=True)