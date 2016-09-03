from django.contrib import admin
from .models import Emergencia, Unidad

# Register your models here.
class EmergenciaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Emergencia,EmergenciaAdmin)
class UnidadAdmin(admin.ModelAdmin):
    pass
admin.site.register(Unidad,UnidadAdmin)
