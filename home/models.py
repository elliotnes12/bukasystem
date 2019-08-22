from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.utils.timezone import now
from PIL import Image
from io import BytesIO
import sys
from django.core.files.uploadedfile import InMemoryUploadedFile


class Sections(models.Model):
      name = models.CharField(max_length = 50,verbose_name = "Nombre")
      slug = models.CharField(max_length = 50,verbose_name = "Slug")
      title = models.CharField(max_length = 50,verbose_name = "Titulo")
      description = RichTextField(verbose_name = "Descripcion")
      image = models.ImageField(verbose_name = "Imagen",upload_to = "sections",null = True,blank = True)
      created = models.DateTimeField(auto_now_add=True,verbose_name = "Creado")
      updated = models.DateTimeField(auto_now=True,verbose_name = "Actualizado")


      def save(self, *args, **kwargs):

          img =self.compressImage(self.image)
          if img != False:
                self.image = img

          super(Sections, self).save(*args, **kwargs)

      def compressImage(self,uploadedImage):
          
          try:
            imageTemproary = Image.open(uploadedImage)
            outputIoStream = BytesIO()
            imageTemproaryResized = imageTemproary.resize( (1020,573) )
            imageTemproary.save(outputIoStream , format='JPEG', quality=55)
            outputIoStream.seek(0)
            uploadedImage = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % uploadedImage.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
            return uploadedImage
          except:
            return False
      
      class Meta:
        verbose_name = "Seccion"
        verbose_name_plural = "Secciones"
        ordering = ["-created"]

      def __str__(self):
        return self.name



class ProjectCategory(models.Model):
      name = models.CharField(max_length=50,verbose_name = "Nombre")
      slug = models.CharField(max_length=50,verbose_name = "Slug")
      metadata = models.CharField(max_length=20,verbose_name = "TagName",null = True,blank = True)
      created = models.DateTimeField(auto_now_add=True,verbose_name = "Creado")
      updated = models.DateTimeField(auto_now=True,verbose_name = "Actualizado")


      class Meta:
        verbose_name = "ProyectoCategoria"
        verbose_name_plural = "ProyectoCategorias"
        ordering = ["-created"]

      def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=50,verbose_name= "Titulo")
    description = RichTextField(verbose_name = "Descripcion")
    image = models.FileField(verbose_name = "Imagen",upload_to = "projects")
    link = models.URLField(null = True,blank = True,verbose_name ="url")
    created = models.DateTimeField(auto_now_add=True,verbose_name = "Creado")
    updated = models.DateTimeField(auto_now=True,verbose_name = "Actualizado")
    categoria = models.ForeignKey(ProjectCategory,verbose_name = "categoria",on_delete = models.CASCADE)

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ["-created"]

    def __str__(self):
        return self.title