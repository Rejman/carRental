from django.shortcuts import render

from django.contrib.auth.models import User

app_name = "carRental"

def home(request):

    context = {
        'app_name':app_name,
        'title': 'home'
    }
    
    return render(request, 'carRental/home.html', context)

def users(request):

    users = User.objects.all()
    
    context = {
        'app_name':app_name,
        'title': 'users',
        'users': users,
    }
    
    return render(request, 'carRental/users.html', context)
