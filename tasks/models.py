from django.db import models

# Create your models here.
class Task(models.Model):
    tname=models.CharField(max_length=50)
    tdesc=models.CharField(max_length=100)

    def __str__(self):
        return self.tname
