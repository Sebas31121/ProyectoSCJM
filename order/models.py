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
    autor_usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    total_pedido = models.FloatField("Total pedido", default=0)

class ProductOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1) 

@receiver(post_save, sender = Pedido)
def sumar_total_pedido(sender,instance,**kwargs):
    orderproducts = ProductOrder.objects.filter(order=instance)
    for orderproduct in orderproducts:
        producto = Product.objects.get(id=orderproduct.product_id)
        instance.total_pedido = producto.price * orderproduct.amount
    post_save.disconnect(sumar_total_pedido, sender=Pedido)
    instance.save(update_fields=["total_pedido"])
    post_save.connect(sumar_total_pedido, sender=Pedido)

""" @receiver(pre_save, sender=Pedido)
def verificacion_estado_pedido(sender, instance, **kwargs):
    try:
        latest_order = Pedido.objects.filter(nro_mesa=instance.nro_mesa).latest('fecha_hora')
    except Pedido.DoesNotExist:
        latest_order = None

    if latest_order.estado == "3":
        raise ValueError("No se permite enviar más datos cuando el estado es 3.")
    else:
        return """