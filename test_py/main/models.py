from django.db import models

class Car(models.Model):
    title=models.CharField(max_length=30)
    Brand=models.CharField(max_length=30)
    Model=models.CharField(max_length=30)
    Steering_wheel=models.CharField(max_length=30)
    Drive_unit=models.CharField(max_length=30)
    Year=models.CharField(max_length=30)
    Volume=models.CharField(max_length=30)
    text=models.TextField('Description')
    phone=models.CharField(max_length=30)

    def __str__(self):
        return self.title
