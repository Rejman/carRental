from django import forms
from django.contrib.auth.models import User
import datetime


class RentalForm(forms.Form):

    dateOfRental = forms.DateField(initial=datetime.datetime.now())
    dateOfReturn = forms.DateField(initial=datetime.datetime.now())


    labels = {
        "dateOfRental": "data wypożyczenia (format : 01.10.2020)",
        "dateOfReturn": "data zwrotu",
    }


