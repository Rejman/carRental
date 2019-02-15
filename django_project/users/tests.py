from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from users.views import register, profile, contact
from users.models import Contact




class TestUrls(SimpleTestCase):

    def test_register_url_is_resolves(self):
        url = reverse('register')
        print(resolve(url))
        self.assertEquals(resolve(url).func, register)

    def test_profile_url_is_resolves(self):
        url = reverse('profile')
        print(resolve(url))
        self.assertEquals(resolve(url).func, profile)

    def test_contact_url_is_resolves(self):
        url = reverse('contact')
        print(resolve(url))
        self.assertEquals(resolve(url).func, contact)

