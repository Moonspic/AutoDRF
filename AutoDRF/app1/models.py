from django.db import models

# Create your models here.
class Class1(models.Model):
    Name = models.CharField(max_length=255)


class Class2(models.Model):
    Name = models.CharField(max_length=255)
    
