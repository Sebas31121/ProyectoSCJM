from django.db import models
from shared.models import CommonModel
from inventory.models import Product
from table.models import Mesa

class Pedido(models.Model):
    ESTADO_CHOICES = (
        (1, 'Pendiente'),
        (2, 'Entregado'),
        (2, 'Listo'),
    )
    fecha_hora = models.DateTimeField("Fecha y Hora", auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    nro_mesa = models.ForeignKey(Mesa,on_delete=models.CASCADE,related_name="fkmesa")
    productos=models.ManyToManyField(Product)