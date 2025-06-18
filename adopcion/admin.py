from django.contrib import admin



from django.contrib import admin
from .models import Perro, UsuarioAdoptante, PostulacionAdopcion 

admin.site.register(Perro)
admin.site.register(UsuarioAdoptante)
admin.site.register(PostulacionAdopcion)

