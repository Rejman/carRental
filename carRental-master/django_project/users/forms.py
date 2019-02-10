from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Contact

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):

    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email']


class ContactUpdateForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['street', 'code', 'city', 'phone']
    
