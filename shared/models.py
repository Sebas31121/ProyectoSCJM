from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your models here.
class CommonModel(models.Model):
    status=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)
    #user_created=models.ForeignKey(User,on_delete=models.CASCADE)
    user_modified=models.IntegerField(blank=True, null=True)