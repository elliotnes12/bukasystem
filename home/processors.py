from django.conf import settings

#Contexto urlBase
def baseUrl(request):
      dir_ctx = {}
      if settings.DEBUG:
          dir_ctx = {'BASE_URL_HTML':'127.0.0.1'}
      else:
          dir_ctx = {'BASE_URL_HTML':'www.bukasystem.com'}
      return dir_ctx 

def redesSociales(request):
     dir_ctx = {
         'URL_FACEBOOK' : 'https://www.facebook.com/bukasystem'
     }
     return dir_ctx
     
    