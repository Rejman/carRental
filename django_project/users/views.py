from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ContactUpdateForm
from .models import Contact

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
        "form":form,
    }


    return render(request, 'users/register.html', context)

@login_required
def profile(request):
    title = 'profile'

    if request.method == 'POST':
        
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Zaaktualizowano dane!')
            
            return redirect('carRental-home')
    else:
                    
        u_form = UserUpdateForm(instance=request.user)
        

    
    context={
        "title": title,
        'u_form': u_form,

    }

    return render(request, 'users/profile.html', context)

@login_required
def contact(request):

    try:
        contact = Contact.objects.get(user=request.user)
    except Contact.DoesNotExist:
        contact = Contact(user=request.user, street="", code="", city="", phone="")
        contact.save()


    title= 'contact'

    if request.method == 'POST':
        
        c_form = ContactUpdateForm(request.POST, instance=request.user.contact)
        if c_form.is_valid():
            c_form.save()
            messages.success(request, f'Zaaktualizowano dane!')
            
            return redirect('carRental-home')
    else:
                    
        c_form = ContactUpdateForm(instance=request.user.contact)
        

    
    context={
        "title": title,
        'c_form': c_form,

    }

    return render(request, 'users/contact.html', context)
