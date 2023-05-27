from django.db import models

class Cliente(models.Model):
    nickname = models.CharField("Apodo", max_length=80, help_text="Apodo")
    celular = models.CharField("Número de contacto", max_length=80, help_text="Apodo")
    deuda = models.IntegerField("Deuda", help_text="Deuda", null=True)
    abono = models.IntegerField("Abono", help_text="Abono", null=True)
    fecha_hora = models.DateTimeField("Fecha y Hora", auto_now_add=True)
    estado = models.BooleanField(default=True,help_text="Estado cliente")
    is_active = models.BooleanField(default=True)
    def __str__(self) -> str:
        return f"{self.nickname} - {self.celular} - {self.deuda} - {self.abono}"