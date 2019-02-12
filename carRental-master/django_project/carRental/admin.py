from django.contrib import admin
from .models import Car, CarModel, Rental

admin.site.register(Car)
admin.site.register(CarModel)
admin.site.register(Rental)

