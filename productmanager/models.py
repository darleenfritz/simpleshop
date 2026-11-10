from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    product_number = models.IntegerField()
    price_brutto = models.DecimalField(max_digits=5, decimal_places=2)
    price_netto = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return(f"Name: {self.name}"
               f"Produkt Nummer: {self.product_number}"
               f"Preis brutto: {self.price_brutto}"
               f"Preis netto: {self.price_netto}" )

    #alternativ return f"{self.name} (Nr: {self.product_number}) - {self.price_brutto} EUR (Brutto) - {self.price_netto} EUR (Netto)"