from django.db import models
from shared.models import CommonModel
from inventory.models import Product

class Mesa(models.Model):
    nro_mesa = models.IntegerField("Número de la mesa", help_text="Mesa")
    cant_sillas = models.IntegerField("Cantidad de sillas", help_text="Sillas", default=0)

class Pedido(models.Model):
    fecha_hora = models.DateTimeField("Fecha y Hora", auto_now_add=True)
    estado = models.BooleanField(default=True,help_text="Estado pedido")
    nro_mesa = models.ForeignKey(Mesa,on_delete=models.CASCADE,related_name="fkmesa")
    productos=models.ManyToManyField(Product)