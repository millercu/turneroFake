from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Identificarse(models.Model):

    usuario = models.ForeignKey(User,
                                       on_delete= models.CASCADE,
                                       null = True,
                                       blank = True
                                       )
    name = models.CharField(max_length=50)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


