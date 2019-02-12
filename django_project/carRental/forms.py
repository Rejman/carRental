from django import forms
from django.contrib.auth.models import User
from .models import Rental



class RentalForm(forms.ModelForm):

    class Meta:
        model = Rental
        fields = ['dateOfRental', 'dateOfReturn']

        #fields = ("user", "title")
        labels = {
            "dateOfRental": "data wypożyczenia (format : 01.10.2020)",
            "dateOfReturn": "data zwrotu",
        }
