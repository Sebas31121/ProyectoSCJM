from django.db import models
from table.models import Mesa

class Table(models.Model):
    table=models.ManyToManyField(Mesa)