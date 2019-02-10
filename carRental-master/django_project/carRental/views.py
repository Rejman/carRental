from django.shortcuts import render

from django.contrib.auth.models import User

from .models import CarModel

app_name = "carRental"

carModels = CarModel.objects.all()
marks = set()

for car in carModels:
    marks.add(car.mark)

def home(request, mark='all'):
    
    if mark != 'all':
        carModels = CarModel.objects.filter(mark=mark)
    else:
        carModels = CarModel.objects.all()
    
    context = {
        'marks':marks,
        'carModels': carModels,
        'app_name':app_name,
        'title': 'home'
    }
    
    return render(request, 'carRental/home.html', context)


def desc(request, car_model_id):

    carModel = CarModel.objects.get(pk=car_model_id)
    
    context = {
        'carModel':carModel,
        'app_name':app_name,
        'title': carModel.model,
    }
    
    return render(request, 'carRental/describe.html', context)
