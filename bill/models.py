from django.db import models
from order.models import Product

class Factura(models.Model):
    numero = models.CharField(max_length=20)
    fecha = models.DateField()
    productos = models.ManyToManyField(Product)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.numero
