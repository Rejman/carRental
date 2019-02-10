from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    code = models.CharField(max_length=6)
    phone = models.CharField(max_length=9)

    def __str__(self):
        return self.user.username + ' contact'


    
