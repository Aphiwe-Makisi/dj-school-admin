from django.db import models

# Create your models here.

class CommonFields(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=13)

    class Meta:
        abstract = True

class Student(CommonFields):
    
    def __str__(self):
        return self.first_name