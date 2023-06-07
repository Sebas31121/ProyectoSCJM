from django.db import models
from shared.models import CommonModel
from inventory.models import Product
from table.models import Mesa
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

class Pedido(models.Model):
    ESTADO_CHOICES = (
        (1, 'Pendiente'),
        (2, 'Entregado'),
        (3, 'Pagado'),
    )
    fecha_hora = models.DateTimeField("Fecha y Hora", auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    nro_mesa = models.ForeignKey(Mesa,on_delete=models.CASCADE,related_name="fkmesa")
    productos = models.ManyToManyField(Product)
    autor_usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    total_pedido = models.FloatField("Total pedido", default=0)

@receiver(post_save, sender = Pedido)
def sumar_total_pedido(sender,instance,**kwargs):
    total = 0
    for producto in instance.productos.all():
        total = total + producto.price
    instance.total_pedido = total
    post_save.disconnect(sumar_total_pedido, sender=Pedido)
    instance.save(update_fields=["total_pedido"])
    post_save.connect(sumar_total_pedido, sender=Pedido)

@receiver(pre_save, sender = Pedido)
def verificacion_estado_pedido(sender,instance,**kwargs):
    latest_order = Pedido.objects.filter(nro_mesa=instance.nro_mesa).latest('fecha_hora')
    print(latest_order.estado)
    if latest_order.estado == "3":
        pre_save.disconnect(verificacion_estado_pedido, sender=Pedido)
        instance.save()
        pre_save.connect(verificacion_estado_pedido, sender=Pedido)
    else:
        return