from django.db import models
from shared.models import CommonModel
from inventory.models import Product
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum

class BillBase(CommonModel):
    fecha = models.DateTimeField(auto_now_add=True)
    sub_total = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    total = models.FloatField(default=0)

    def __str__(self):
        return '{}' .format(self.id)

    def save(self):
        self.total = self.sub_total - self.descuento
        super(BillBase, self).save()

class BillDetalle(CommonModel):
    factura = models.ForeignKey(BillBase, on_delete=models.CASCADE)
    producto = models.ForeignKey(Product, on_delete=models.CASCADE)
    cantidad = models.BigIntegerField(default=0)
    precio = models.FloatField(default=0)
    sub_total = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    total = models.FloatField(default=0)

    def __str__(self):
        return '{}' .format(self.producto)

    def save(self):
        self.sub_total = float(float(int(self.cantidad)) * float(self.precio))
        self.total = self.sub_total - float(self.descuento)
        super(BillDetalle, self).save()

@receiver(post_save, sender=BillDetalle)
def detalle_fac_guardar(sender, instance, **kwargs):
    factura_id = instance.factura.id
    producto_id = instance.producto.id

    enc = BillBase.objects.get(pk=factura_id)
    if enc:
        sub_total = BillDetalle.objects \
            .filter(factura=factura_id) \
            .aggregate(sub_total=Sum('sub_total')) \
            .get('sub_total', 0.00)

        descuento = BillDetalle.objects \
            .filter(factura=factura_id) \
            .aggregate(descuento=Sum('descuento')) \
            .get('descuento', 0.00)

        enc.sub_total = sub_total
        enc.descuento = descuento
        enc.save()

        prod = Product.objects.filter(pk=producto_id).first()
        if prod:
            cantidad = int(prod.existencia) - int(instance.cantidad)
            prod.existencia = cantidad
            prod.save()