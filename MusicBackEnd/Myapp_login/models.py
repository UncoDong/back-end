from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=128,unique=True)
    password = models.CharField(max_length=258)
    def __str__(self):
        return self.name+','+self.password

class Score(models.Model):
    name = models.CharField(max_length=128,unique=True)
    png_path = models.CharField(max_length=258)
    json_path = models.CharField(max_length=258)
    def __str__(self):
        return self.name+','+self.png_path+','+self.json_path
