from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    
    title = 'register'
    form = None
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Utworzono użytkownika {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()


    context={
        "title": title,
        "form":form
    }


    return render(request, 'users/register.html', context)
    
