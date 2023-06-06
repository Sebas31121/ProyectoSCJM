from django.db import models

class Proveedor(models.Model):
    nit = models.CharField("NIT", max_length=80, help_text="NIT")
    nombre = models.CharField("Nombre", max_length=80, help_text="Nombre")
    contacto = models.IntegerField("Teléfono o celular", help_text="Teléfono o celular", null=True)
    ubicacion = models.CharField("Localización", max_length=300, help_text="Localización", null=True)
    is_active = models.BooleanField(default=True)
    def __str__(self) -> str:
        return f"{self.nit} - {self.nombre} - {self.contacto} - {self.ubicacion}"