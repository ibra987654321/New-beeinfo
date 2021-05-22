from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name if self.user.first_name else self.user.username
 
    class Meta: 
        verbose_name = 'профиль'
        verbose_name_plural = 'профили пользователей'
