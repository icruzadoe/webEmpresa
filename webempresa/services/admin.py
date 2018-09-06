from django.contrib import admin
from .models import Service#con el . adelante de models sabemos que estamos haciendo referencia al mismo directorio en este caso portfolio, estamos accediendo a la clase Service del archivo models.py 

# Register your models here.
#Se regitra para que sea accesible desde el panel de administracion
#Modifica el panel del administrador para que muestre la fecha de creacion y la fecha de edicion
class ServiceAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')

#se pasa como parametro la configuracion extendida para que se muestre
admin.site.register(Service, ServiceAdmin)