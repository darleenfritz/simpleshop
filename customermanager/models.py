from django.db import models
from django.conf import settings

# Create your models here.
class Customer(models.Model):

    '''firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    email = models.EmailField()'''
    salutation = models.CharField(max_length=5)
    birthday = models.DateField()
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def first_name(self): #funktionsnamen müssen wie attribute oben heißen
        return self.user.first_name

    def last_name(self):
        return self.user.last_name

    def email(self):
        return self.user.email

