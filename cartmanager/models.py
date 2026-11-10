from django.db import models
from customermanager.models import Customer


# Create your models here.
class Cart(models.Model):
    cart_netto = models.DecimalField(max_digits=10, decimal_places=2)
    taxes = models.DecimalField(max_digits=10, decimal_places=2)
    cart_brutto = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return(f"Warenkorb Netto: {self.cart_netto}"
               f"Steueranteil: {self.taxes}"
               f"Warenkorb Brutto: {self.cart_brutto}"
                )

class Entry(models.Model):
    product_id = models.IntegerField(null=False)
    product_name = models.CharField(max_length=50)
    unit_net_price =models.FloatField(null=False)
    unit_gross_price =models.FloatField(null=False)
    quantity = models.IntegerField(null=False)
    net_sum = models.FloatField(null=False)
    gross_sum = models.FloatField(null=False)
    cart = models.ForeignKey(Cart,related_name='entries', on_delete=models.CASCADE)

    def __str__(self):
        return(f"Produkt ID: {self.product_id}"
               f"Product Name: {self.product_name}"
               f"Nettowert pro Stück: {self.unit_net_price}"
               f"Bruttowert pro Stück: {self.unit_gross_price}"
               f"Anzahl: {self.quantity}"
               f"Nettogesamtwert: {self.net_sum}"
               f"Bruttogesamtwert: {self.gross_sum}"
               )


