from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RentalForm
from .models import CarModel, Car, Rental
from django.contrib import messages
import datetime

app_name = "carRental"



def home(request, mark='all'):

    carModels = CarModel.objects.all()
    marks = set()

    for car in carModels:
        marks.add(car.mark)
    
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
    cars = Car.objects.filter(carModel=car_model_id)
    
    context = {
        'cars': cars,
        'carModel':carModel,
        'app_name':app_name,
        'title': carModel.model,
    }
    
    return render(request, 'carRental/describe.html', context)



#@login_required
@login_required(login_url='/login/')

def rental(request, car_id=0):


    title= 'wypożycz'
    car = Car.objects.get(pk=car_id)
    rental = Rental(user=request.user, car=car, dateOfRental=datetime.datetime.now(), dateOfReturn=datetime.datetime.now())
    form = RentalForm()

    if request.method == 'POST':
        form = RentalForm(request.POST)
        if car.available==False:
            messages.error(request, f'samochód nie jest dostępny')
            return redirect('carRental-home')

        if form.is_valid():
            rental.set_dateOfRental(form.cleaned_data['dateOfRental'])
            rental.set_dateOfReturn(form.cleaned_data['dateOfReturn'])
            rental.save()
            car.available=False
            car.save()
            
            messages.success(request, f'Zarejestrowano wypożyczenie')
            return redirect('carRental-home')
        
    else:
        form = RentalForm()
        
    context={
        "title": title,
        'form': form,

    }
    return render(request, 'carRental/rental.html', context)


    
