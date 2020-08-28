from django.db import models

# Create your models here.
class AnotherClass(models.Model):
    Name = models.CharField(max_length=255)


class AndOneMore(models.Model):
    Name = models.CharField(max_length=255)
    
