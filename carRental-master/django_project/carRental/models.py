from django.db import models

from django.contrib.auth.models import User

class CarModel(models.Model):

    mark = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    sort = models.CharField(max_length=200)
    doors = models.CharField(max_length=1)
    desc = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    #image = models.ImageField( blank=True, default="default.jpg")

    def __str__(self):
        return self.mark + ' ' + self.model


class Car(models.Model):
    
    plate = models.CharField(max_length=7)
    color = models.CharField(max_length=100)
    carModel = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.plate

class Rental(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    car = models.OneToOneField(Car, on_delete=models.CASCADE)
    dateOfRental = models.DateField()
    dateOfReturn = models.DateField()
    cost = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.user +' '+str(self.car)+' '+ self.cost
    
