from django.db import models
from shared.models import CommonModel

class Category(models.Model):
    name=models.CharField("Nombre de la categoria", max_length=80, unique=True)
    def __str__(self) -> str:
        return self.name

class Unity(models.Model):
    name=models.CharField("Unidad de medida", max_length=80, unique=True)
    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name=models.CharField("Nombre del Producto: ",max_length=80)
    description=models.CharField("Descripción: ",max_length=200, blank=True, null=True)
    price=models.FloatField("Precio: ",default=0)
    stock=models.IntegerField("Cantidad: ",default=0)
    img_route=models.ImageField("Subir imagen: ", upload_to="product_images",default="/")
    unity=models.ForeignKey(Unity,on_delete=models.CASCADE,related_name="product_unity",blank=True,null=True,verbose_name="Unidad de medida: ")
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="product_category",blank=True,null=True,verbose_name="Categoria: ")
    is_active=models.BooleanField(default=True)
    def __str__(self) -> str:
        return f"{self.name} - {self.description} - {self.price} - {self.stock}"