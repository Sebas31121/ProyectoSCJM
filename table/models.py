from django.db import models

class Mesa(models.Model):
    nro_mesa = models.IntegerField("Número de la mesa", help_text="Mesa")
    cant_sillas = models.IntegerField("Cantidad de sillas", help_text="Sillas", default=0)
    is_active = models.BooleanField(default=True)
    def __str__(self) -> str:
        return f"{self.nro_mesa} - {self.cant_sillas}"