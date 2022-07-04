from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType 
from django.contrib.contenttypes.fields import GenericForeignKey



# Create your models here.




class Avatar(models.Model):

    user = models.ForeignKey(User, related_name='avatar', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    def __str__(self):
        return f" Usuario: {self.user}"

