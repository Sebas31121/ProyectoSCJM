from django.db import models
from shared.models import CommonModel

class Mesa(models.Model):
    nro_mesa = models.IntegerField("Número de la mesa", help_text="Número de mesa")

class Pedido(models.Model):
    id = models.BigIntegerField(primary_key=True)
    fecha_hora = models.DateTimeField("Fecha y Hora", auto_now_add=True)
    estado = models.BooleanField(default=True,help_text="Estado pedido")
    nro_mesa = models.ForeignKey(Mesa,on_delete=models.CASCADE,related_name="fkmesa")