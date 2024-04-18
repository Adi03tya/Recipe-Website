from django.db import models

# Create your models here.

class Student(models.Model):
   
   id = models.AutoField(primary_key=True)
   name =models.CharField(max_length=100)
   roll = models.IntegerField()
   age = models.IntegerField()
   address = models.TextField()
   email = models.EmailField()
   phone = models.IntegerField()
   dob = models.DateField()

   def __str__(self):
        return self.name

class Car(models.Model):
    car_name = models.CharField(max_length=100)
    speed = models.IntegerField()

    def __str__(self):
        return self.car_name 