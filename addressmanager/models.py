from django.db import models

from customermanager.models import Customer


# Create your models here.

class Address(models.Model):
    salutation = models.CharField(max_length=5)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    street = models.CharField(max_length=100)
    housenumber = models.IntegerField()
    zip= models.IntegerField()
    city = models.CharField(max_length=20)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='addresses')


    def __str__(self):
        return( f"Anrede: {self.salutation}"
                f"Vorname: {self.firstname}"
                f"Nachname: {self.lastname}"
                f"Straße: {self.street}"
                f"Hausnummer: {self.housenumber}"
                f"Postleitzahl: {self.zip}"
                f"Ort: {self.city}" )
