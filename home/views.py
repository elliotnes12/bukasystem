from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Sections,ProjectCategory,Project


class NotFoundException(TemplateView):
      template_name = "home/404.html"

class HomeView(TemplateView):
     template_name = "home/home.html"

     def get(self,request,*args,**kwargs):
         header = Sections.objects.get(slug = 'header')
         somos = Sections.objects.get(slug = 'somos')
         catproject = ProjectCategory.objects.all()
         projects = Project.objects.all()
         return render(
               request,self.template_name,
                   {
                    'header':header, 
                    'somos':somos,
                    'catprojects':catproject,
                    'projects': projects
                   }
                )