from django.contrib import admin
from .models import Reporte, Entrada, PerfilOf

class EntradaAdmin(admin.ModelAdmin):
    readonly_fields = ("created", )

class ReporteAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)

# Register your models here.
admin.site.register(Entrada, EntradaAdmin)
admin.site.register(Reporte, ReporteAdmin)
admin.site.register(PerfilOf)