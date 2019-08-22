from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    asunto = models.CharField(max_length=50)
    mensaje = models.CharField(max_length = 200)
    created = models.DateTimeField(auto_now_add=True,verbose_name = "Creado")
    updated = models.DateTimeField(auto_now=True,verbose_name = "Actualizado")
    
    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
        ordering = ["-created"]
   
    def __str__(self):
        return self.name