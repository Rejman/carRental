from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from carRental.views import home, desc, rental
from carRental.models import CarModel, Car, Rental
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import json



class TestUrls(SimpleTestCase):

    def test_home_url_is_resolves(self):
        url = reverse('carRental-home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home)

    
    def test_desc_url_is_resolves(self):
        url = reverse('desc', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, desc)

    def test_rental_url_is_resolves(self):
        url = reverse('rental', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, rental)



class TestViews(TestCase):

    def setUp(self):
        
        self.client = Client()
        self.home_url = reverse('carRental-home')
        self.desc_url = reverse('desc', args=[1])
        self.rental_url = reverse('rental', args=[2])

        self.carModel1 = CarModel.objects.create(
            pk=1,
            mark = 'Jaguar',
            model = 'XE',
            sort = 'osobowy',
            doors = 4,
            desc = 'desc',
            price = 450,
        )

        self.car1 = Car.objects.create(
            pk=2,
            plate='RZ1999V',
            color = 'biały',
            available = True,
            carModel=self.carModel1,
        )

        
        


    def test_home_GET(self):

        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'carRental/home.html')

    def test_desc_GET(self):

        response = self.client.get(self.desc_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'carRental/describe.html')

    
