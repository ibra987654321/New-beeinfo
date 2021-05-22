from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from getpass import getpass
from .urls import *
from .models import Profile
from .ldap import LoginAD
import os


class UserLogin(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.username = input('Ad username: ')
        cls.password = getpass()
        cls.check_ad_credentials_for_console()
        
    @classmethod
    def check_ad_credentials_for_console(cls):
        cls.ad = LoginAD(cls.username, cls.password)
        if not cls.ad.get('displayName'):
            print('WRONG AD CREDENTIALS')
            os._exit(1)
    
    def setUp(self):
        self.client = Client()
        self.right_credentials = {'username': self.username, 'password': self.password}
        self.url = reverse('login')
    
    def test_creating_user_and_profile_via_first_login_with_right_credentials(self):
        response = self.client.post(self.url, self.right_credentials, format='json')
        created_user = User.objects.get(username=self.username)
        created_profile = Profile.objects.get(user__username=self.username)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index')) # TODO: redirect url should be replaced, when home url is ready
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(created_user.username, self.username)
        self.assertFalse(created_user.has_usable_password())
        self.assertEqual(Profile.objects.count(), 1)
        self.assertEqual(created_profile.user_id, created_user.id)

    def test_subsequent_login_with_right_credentials(self):
        user = User.objects.create(username=self.username)
        response = self.client.post(self.url, self.right_credentials, format='json')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index')) # TODO: redirect url should be replaced, when home url is ready
        self.assertQuerysetEqual(User.objects.all(), [user])

    def test_login_with_wrong_credentials(self):
        wrong_credentials = {'username': self.username, 'password': 'wrong_password'}
        response = self.client.post(self.url, wrong_credentials, format='json')
        self.assertContains(response, 'Неправильное имя пользователя или пароль', status_code=200, html=True)
        self.assertQuerysetEqual(User.objects.all(), [])

    def test_login_wihtout_credentials(self):
        response = self.client.post(self.url)
        self.assertContains(response, 'Заполните поля', status_code=200, html=True)
