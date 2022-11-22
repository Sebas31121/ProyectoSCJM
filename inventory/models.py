from django.db import models
from shared.models import CommonModel
# Create your models here.
#Creacion Tablas
class Category(models.Model):
    #Creacion de Atributos
    name=models.CharField(max_length=80,help_text="Nombre de la Categoria", unique=True)
class SubCategory(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="fkcategory")
    name=models.CharField(max_length=80,help_text="Nombre de la Subcategoria", unique=True)
class Product(models.Model):
    name=models.CharField(max_length=80,help_text="Nombre del Producto")
    description=models.CharField(max_length=200,help_text="Descripción del producto")
    price=models.FloatField(default=0,help_text="Precio del producto")
    stock=models.IntegerField(default=0,help_text="En existencia")